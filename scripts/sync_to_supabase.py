"""
published/<category>/<한국어제목>.md → Supabase upsert

파일명 = slug = title. frontmatter 없음.

MD 템플릿 약속:
  > 한 줄 요약

  ## 정의        → definition block
  ## 핵심 포인트 → keyPoints block
  ## 면접 질문   → interviewPrompts block
  ## 확인 문제   → checkQuestions block
  ## 키워드      → keywords 배열 (쉼표 구분)
  ## 연관 콘텐츠 → [[파일명]] wikilink → slug (= 파일명)

display_order: 카테고리 내 파일명 정렬 순서 (1001, 2001, 3001...)
id: DB에 slug가 있으면 기존 UUID 유지, 없으면 신규 생성
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

GITHUB_RAW = "https://raw.githubusercontent.com/gadisom/CSContent/main/raw/assets"


def fetch_existing() -> dict:
    """slug → id 매핑"""
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?select=slug,id"
    req = urllib.request.Request(
        url, headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
    )
    with urllib.request.urlopen(req) as resp:
        return {row["slug"]: row["id"] for row in json.loads(resp.read())}


def parse_md(filepath: str) -> dict:
    with open(filepath, encoding="utf-8") as f:
        raw = f.read()

    # frontmatter 있으면 제거 (하위 호환)
    body = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.DOTALL).strip()

    summary_m = re.search(r"^>\s*(.+)$", body, re.MULTILINE)
    summary = summary_m.group(1).strip() if summary_m else ""

    blocks, keywords, related = [], [], []
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
            related = re.findall(r"\[\[(.+?)\]\]", content)
        elif header in SECTION_TO_BLOCK:
            blocks.append({"type": SECTION_TO_BLOCK[header], "items": items})
            # 섹션 내 인라인 이미지 감지 → 섹션 블록 바로 뒤에 삽입
            for line in content.splitlines():
                line = line.strip()
                local_m = re.match(r"!\[\[(.+?)\]\]", line)
                if local_m:
                    filename = local_m.group(1)
                    blocks.append({"type": "image", "items": [f"{GITHUB_RAW}/{filename}"]})
                elif re.match(r"https?://\S+\.(png|jpg|jpeg|gif|webp|svg)", line, re.IGNORECASE):
                    blocks.append({"type": "image", "items": [line]})

    return {"summary": summary, "blocks": blocks, "keywords": keywords, "related": related}


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

    by_category: dict[str, list[str]] = defaultdict(list)
    for f in all_files:
        category = f.replace("\\", "/").split("/")[1]
        by_category[category].append(f)
    for cat in by_category:
        by_category[cat].sort()

    existing = fetch_existing()
    print(f"DB 기존 콘텐츠: {len(existing)}개\n")

    errors, inserts, updates = [], [], []

    for category_slug, files in sorted(by_category.items()):
        for idx, filepath in enumerate(files):
            display_order = (idx + 1) * 1000 + 1
            slug = filepath.replace("\\", "/").split("/")[2].replace(".md", "")

            try:
                parsed = parse_md(filepath)

                record = {
                    "id": existing.get(slug) or str(uuid.uuid4()),
                    "category_slug": category_slug,
                    "category_title": CATEGORY_TITLES.get(category_slug, category_slug),
                    "subcategory_slug": slug,
                    "subcategory_title": slug,
                    "slug": slug,
                    "title": slug,
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
                    print(f"✚  INSERT [{display_order}] {category_slug}/{slug}")
                else:
                    updates.append(slug)
                    print(f"↻  UPDATE [{display_order}] {category_slug}/{slug}")

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
