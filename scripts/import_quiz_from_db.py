"""
quiz_questions (DB) → quiz/<category>/<concept>.md

MD 형식:
---
category: <category_slug>
tag: <tag>
---

#### OX | [id]
질문
> O/X
> 해설

#### 빈칸 | [id]
질문 (___ 포함)
> 정답
> 해설

#### 객관식 | [id]
질문
1. 선택지
2. ✅ 정답 선택지
3. 선택지
> 해설
"""

import json
import os
import urllib.request
from collections import defaultdict

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY") or os.environ["SUPABASE_PUBLISHABLE_KEY"]

CATEGORY_MAP = {
    "data-structures": "data-structure",
    "algorithms": "algorithms",
    "operating-systems": "operating-system",
    "operating-system": "operating-system",
    "databases": "database",
    "database": "database",
    "networking": "network",
    "network": "network",
}


def fetch_all():
    url = (
        f"{SUPABASE_URL}/rest/v1/quiz_questions"
        f"?select=id,category_id,type,question,choices,correct_index,ox_answer,fill_answer,explanation,concept,tag"
        f"&order=id.asc"
    )
    req = urllib.request.Request(
        url,
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def render_md(category_slug: str, tag: str, rows: list) -> str:
    lines = [
        "---",
        f"category: {category_slug}",
        f"tag: {tag}",
        "---",
        "",
    ]

    for r in rows:
        rid = r.get("id", "")
        q = r["question"]
        exp = (r.get("explanation") or "").strip()

        if r["type"] == "ox":
            answer = r.get("ox_answer") or ""
            lines += [f"#### OX | [{rid}]", q, f"> {answer}", f"> {exp}", ""]

        elif r["type"] == "fill":
            answer = r.get("fill_answer") or ""
            lines += [f"#### 빈칸 | [{rid}]", q, f"> {answer}", f"> {exp}", ""]

        else:
            choices = r.get("choices") or []
            correct_idx = r.get("correct_index", -1)
            lines += [f"#### 객관식 | [{rid}]", q]
            for i, choice in enumerate(choices):
                prefix = f"{i + 1}. ✅" if i == correct_idx else f"{i + 1}."
                lines.append(f"{prefix} {choice}")
            lines += [f"> {exp}", ""]

    return "\n".join(lines)


def main():
    rows = fetch_all()
    print(f"총 {len(rows)}개 퀴즈 항목 조회")

    grouped: dict[tuple, list] = defaultdict(list)
    for r in rows:
        key = (r["category_id"], r["concept"] or "기타")
        grouped[key].append(r)

    created, skipped = [], []

    for (category_id, concept), group in sorted(grouped.items()):
        category_slug = CATEGORY_MAP.get(category_id, category_id)
        tag = group[0].get("tag") or ""

        folder = f"quiz/{category_slug}"
        os.makedirs(folder, exist_ok=True)

        filepath = f"{folder}/{concept}.md"
        if os.path.exists(filepath):
            print(f"SKIP  {filepath}")
            skipped.append(filepath)
            continue

        content = render_md(category_slug, tag, group)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"CREATE {filepath} ({len(group)}개 문항)")
        created.append(filepath)

    print(f"\n생성: {len(created)}개  스킵: {len(skipped)}개")


if __name__ == "__main__":
    main()
