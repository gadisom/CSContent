"""
published/<category>/<제목>.md → Supabase upsert

MD 템플릿 약속:
  ---
  slug: ds-array-vs-linked-list
  order: 1001
  related: [slug1, slug2]
  ---

  > 한 줄 요약 (summary)

  ## 정의        → definition block
  ## 핵심 포인트 → keyPoints block
  ## 면접 질문   → interviewPrompts block
  ## 확인 문제   → checkQuestions block
  ## 키워드      → keywords (쉼표 구분)

규칙:
  - id: DB에 이미 있으면 기존 UUID 유지, 없으면 신규 생성
  - category_slug: 폴더명
  - subcategory_title / title: 파일명 (.md 제외)
  - is_published: 항상 true
"""

import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request
import uuid

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


def parse_md(filepath: str) -> dict:
    with open(filepath, encoding="utf-8") as f:
        raw = f.read()

    # 1. frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
    if not fm_match:
        raise ValueError("frontmatter 없음")

    fm_text = fm_match.group(1)
    body = raw[fm_match.end():]

    slug = re.search(r"^slug:\s*(.+)$", fm_text, re.MULTILINE).group(1).strip()
    order_m = re.search(r"^order:\s*(\d+)$", fm_text, re.MULTILINE)
    order = int(order_m.group(1)) if order_m else None
    related_m = re.search(r"^related:\s*\[(.+)\]$", fm_text, re.MULTILINE)
    related = [s.strip() for s in related_m.group(1).split(",")] if related_m else []

    # 2. summary (첫 번째 blockquote)
    summary_m = re.search(r"^>\s*(.+)$", body, re.MULTILINE)
    summary = summary_m.group(1).strip() if summary_m else ""

    # 3. sections → blocks
    blocks = []
    keywords = []
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
            # 줄바꿈 없이 이어진 텍스트, 쉼표 구분
            all_text = " ".join(
                line.strip() for line in content.splitlines() if line.strip()
            )
            keywords = [k.strip() for k in all_text.split(",") if k.strip()]
        elif header in SECTION_TO_BLOCK:
            blocks.append({"type": SECTION_TO_BLOCK[header], "items": items})

    return {
        "slug": slug,
        "order": order,
        "related": related,
        "summary": summary,
        "blocks": blocks,
        "keywords": keywords,
    }


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
    files = glob.glob("published/*/*.md")
    if not files:
        print("No .md files found in published/")
        return

    existing = fetch_existing()
    print(f"DB 기존 콘텐츠: {len(existing)}개\n")

    errors, inserts, updates = [], [], []

    for filepath in sorted(files):
        parts = filepath.replace("\\", "/").split("/")
        category_slug = parts[1]
        filename = parts[2]
        subcategory_title = filename.replace(".md", "")

        try:
            parsed = parse_md(filepath)
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
                "display_order": parsed["order"],
                "is_published": True,
            }

            is_new = slug not in existing
            upsert(record)

            if is_new:
                inserts.append(slug)
                print(f"✚  INSERT: {category_slug}/{subcategory_title} ({slug})")
            else:
                updates.append(slug)
                print(f"↻  UPDATE: {category_slug}/{subcategory_title} ({slug})")

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
