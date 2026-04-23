"""
published/<category>/<한국어제목>.md → Supabase upsert

MD 템플릿 약속:
  ---
  slug: ds-array-vs-linked-list
  related: [slug1, slug2]
  ---

  > 한 줄 요약 (summary)

  ## 정의        → definition block
  ## 핵심 포인트 → keyPoints block
  ## 면접 질문   → interviewPrompts block
  ## 확인 문제   → checkQuestions block
  ## 키워드      → keywords 배열

display_order: 카테고리 내 파일 정렬 순서로 자동 계산 (1001, 2001, 3001...)
id: DB에 이미 있으면 기존 UUID 유지, 없으면 신규 생성
"""

import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request
import uuid
from collections import defaultdict

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SERVICE_KEY"]
TABLE = os.environ["SUPABASE_TABLE"]

CATEGORY_TITLES = {
    "data-structure": "자료구조",
    "algorithms": "알고리즘",
    "operating-system": "운영체제",
    "database": "데이터베이스",
    "network": "네트워크",
}

SECTION_TO_BLOCK = {
    "정의": "definition",
    "핵심 포인트": "keyPoints",
    "면접 질문": "interviewPrompts",
    "확인 문제": "checkQuestions",
}


def fetch_existing() -> dict:
    """slug → id 매핑 반환"""
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?select=slug,id"
    req = urllib.request.Request(
        url, headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
    )
    with urllib.request.urlopen(req) as resp:
        return {row["slug"]: row["id"] for row in json.loads(resp.read())}


def build_title_to_slug(files: list[str]) -> dict:
    """파일명(title) → slug 매핑 (wikilink 변환용)"""
    mapping = {}
    for filepath in files:
        title = filepath.replace("\\", "/").split("/")[2].replace(".md", "")
        try:
            with open(filepath, encoding="utf-8") as f:
                raw = f.read()
            fm_match = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
            if fm_match:
                slug_m = re.search(r"^slug:\s*(.+)$", fm_match.group(1), re.MULTILINE)
                if slug_m:
                    mapping[title] = slug_m.group(1).strip()
        except Exception:
            pass
    return mapping


def parse_md(filepath: str, title_to_slug: dict) -> dict:
    with open(filepath, encoding="utf-8") as f:
        raw = f.read()

    fm_match = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
    if not fm_match:
        raise ValueError("frontmatter 없음")

    fm_text = fm_match.group(1)
    body = raw[fm_match.end():]

    slug = re.search(r"^slug:\s*(.+)$", fm_text, re.MULTILINE).group(1).strip()

    summary_m = re.search(r"^>\s*(.+)$", body, re.MULTILINE)
    summary = summary_m.group(1).strip() if summary_m else ""

    blocks = []
    keywords = []
    related = []
    sections = re.split(r"^## (.+)$", body, flags=re.MULTILINE)

    for i in range(1, len(sections), 2):
        header = sections[i].strip()
        content = sections[i + 1].strip() if i + 1 < len(sections) else ""
        items = [
            line.lstrip("- ").strip()
            for line in content.splitlines()
            if line.strip().startswith("-")
        ]
        if header == "키워드":
            all_text = " ".join(line.strip() for line in content.splitlines() if line.strip())
            keywords = [k.strip() for k in all_text.split(",") if k.strip()]
        elif header == "연관 콘텐츠":
            # [[파일명]] → slug 변환
            for title in re.findall(r"\[\[(.+?)\]\]", content):
                if title in title_to_slug:
                    related.append(title_to_slug[title])
                else:
                    print(f"  ⚠ 연관 콘텐츠 '{title}' 를 찾을 수 없음 (slug 매핑 없음)")
        elif header in SECTION_TO_BLOCK:
            blocks.append({"type": SECTION_TO_BLOCK[header], "items": items})

    return {"slug": slug, "related": related, "summary": summary, "blocks": blocks, "keywords": keywords}


def upsert(data: dict):
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?on_conflict=slug"
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status


def main():
    all_files = glob.glob("published/*/*.md")
    if not all_files:
        print("No .md files found in published/")
        return

    # 카테고리별 파일 정렬 → display_order 자동 계산
    by_category: dict[str, list[str]] = defaultdict(list)
    for f in all_files:
        category = f.replace("\\", "/").split("/")[1]
        by_category[category].append(f)
    for cat in by_category:
        by_category[cat].sort()

    existing = fetch_existing()
    title_to_slug = build_title_to_slug(all_files)
    print(f"DB 기존 콘텐츠: {len(existing)}개\n")

    errors, inserts, updates = [], [], []

    for category_slug, files in sorted(by_category.items()):
        for idx, filepath in enumerate(files):
            display_order = (idx + 1) * 1000 + 1  # 1001, 2001, 3001...
            subcategory_title = filepath.replace("\\", "/").split("/")[2].replace(".md", "")

            try:
                parsed = parse_md(filepath, title_to_slug)
                slug = parsed["slug"]

                record = {
                    "id": existing.get(slug) or str(uuid.uuid4()),
                    "category_slug": category_slug,
                    "category_title": CATEGORY_TITLES.get(category_slug, category_slug),
                    "subcategory_title": subcategory_title,
                    "slug": slug,
                    "title": subcategory_title,
                    "summary": parsed["summary"],
                    "blocks": parsed["blocks"],
                    "keywords": parsed["keywords"],
                    "related_item_ids": parsed["related"],
                    "display_order": display_order,
                    "is_published": True,
                }

                is_new = slug not in existing
                upsert(record)

                if is_new:
                    inserts.append(slug)
                    print(f"✚  INSERT [{display_order}] {category_slug}/{subcategory_title}")
                else:
                    updates.append(slug)
                    print(f"↻  UPDATE [{display_order}] {category_slug}/{subcategory_title}")

            except urllib.error.HTTPError as e:
                print(f"✗  {filepath} — HTTP {e.code}: {e.read().decode()}")
                errors.append(filepath)
            except Exception as e:
                print(f"✗  {filepath} — {e}")
                errors.append(filepath)

    print(f"\n신규: {len(inserts)}개  업데이트: {len(updates)}개  실패: {len(errors)}개")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
