"""
Supabase content_items → published/<category>/<title>.md

기존 DB 항목을 전부 markdown 파일로 변환해 published/ 폴더를 SSOT로 맞춤.
related_item_ids는 가능하면 [[파일명]] wikilink로, 없으면 그대로 slug 유지.

실행:
  SUPABASE_URL=https://... SUPABASE_SERVICE_KEY=... SUPABASE_TABLE=content_items \
  python3 scripts/import_from_db.py
"""

import json
import os
import re
import urllib.request
from pathlib import Path

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SERVICE_KEY"]
TABLE = os.environ["SUPABASE_TABLE"]

BLOCK_TO_SECTION = {
    "definition": "정의",
    "keyPoints": "핵심 포인트",
    "interviewPrompts": "면접 질문",
    "checkQuestions": "확인 문제",
}


def fetch_all() -> list:
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?select=*&order=category_slug,display_order"
    req = urllib.request.Request(
        url, headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def to_md(item: dict, slug_to_title: dict) -> str:
    lines = []

    # summary
    summary = item.get("summary", "").strip()
    lines.append(f"> {summary}\n")

    # blocks
    for block in item.get("blocks") or []:
        btype = block.get("type", "")
        items = block.get("items") or []
        if btype == "image":
            continue  # 이미지는 URL만 있어서 생략
        section = BLOCK_TO_SECTION.get(btype)
        if not section:
            continue
        lines.append(f"## {section}")
        for it in items:
            lines.append(f"- {it}")
        lines.append("")

    # keywords
    keywords = item.get("keywords") or []
    if keywords:
        lines.append("## 키워드")
        lines.append(", ".join(keywords))
        lines.append("")

    # related
    related = item.get("related_item_ids") or []
    if related:
        lines.append("## 연관 콘텐츠")
        for r in related:
            title = slug_to_title.get(r)
            if title:
                lines.append(f"- [[{title}]]")
            else:
                lines.append(f"- {r}")  # 매핑 없으면 slug 그대로
        lines.append("")

    return "\n".join(lines)


def safe_filename(name: str) -> str:
    # 파일명에 사용 불가한 문자 제거
    return re.sub(r'[<>:"/\\|?*]', "", name).strip()


def main():
    print("DB에서 콘텐츠 가져오는 중...")
    items = fetch_all()
    print(f"총 {len(items)}개 항목\n")

    # slug → subcategory_title 매핑 (related wikilink 변환용)
    slug_to_title = {}
    for item in items:
        slug = item.get("slug", "")
        title = item.get("subcategory_title") or item.get("title") or slug
        if slug and title:
            slug_to_title[slug] = title

    created, skipped = 0, 0

    for item in items:
        category = item.get("category_slug", "unknown")
        title = item.get("subcategory_title") or item.get("title") or item.get("slug")
        filename = safe_filename(title) + ".md"

        folder = Path("published") / category
        folder.mkdir(parents=True, exist_ok=True)

        filepath = folder / filename

        if filepath.exists():
            print(f"⚠  SKIP (이미 있음): {filepath}")
            skipped += 1
            continue

        content = to_md(item, slug_to_title)
        filepath.write_text(content, encoding="utf-8")
        print(f"✓  {category}/{filename}")
        created += 1

    print(f"\n생성: {created}개  건너뜀: {skipped}개")


if __name__ == "__main__":
    main()
