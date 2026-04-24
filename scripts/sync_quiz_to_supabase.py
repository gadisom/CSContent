"""
quiz/<category>/<concept>.md → quiz_questions upsert

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
질문
> 정답
> 해설

#### 객관식 | [id]
질문
1. 선택지
2. ✅ 정답 선택지
3. 선택지
> 해설

규칙:
- [id] 있으면 upsert (on_conflict=id)
- [] 이면 신규 insert
"""

import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SERVICE_KEY"]

CATEGORY_ID_MAP = {
    "data-structure": "data-structures",
    "algorithms": "algorithms",
    "operating-system": "operating-systems",
    "database": "databases",
    "network": "networking",
    "android": "android",
    "server": "server",
}

HEADER_RE = re.compile(r"^#### (OX|빈칸|객관식) \| \[(\d*)\]$")
CHOICE_RE = re.compile(r"^(\d+)\.\s*(✅\s*)?(.+)$")


def parse_file(filepath: str) -> list[dict]:
    with open(filepath, encoding="utf-8") as f:
        raw = f.read()

    fm_m = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
    tag = ""
    if fm_m:
        tag_m = re.search(r"^tag:\s*(.+)$", fm_m.group(1), re.MULTILINE)
        tag = tag_m.group(1).strip() if tag_m else ""

    concept = os.path.basename(filepath).replace(".md", "")
    category_slug = filepath.replace("\\", "/").split("/")[1]
    category_id = CATEGORY_ID_MAP.get(category_slug, category_slug)

    body = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.DOTALL)
    lines = body.splitlines()

    rows = []
    i = 0
    while i < len(lines):
        h = HEADER_RE.match(lines[i].strip())
        if not h:
            i += 1
            continue

        qtype_raw, rid_str = h.group(1), h.group(2)
        rid = int(rid_str) if rid_str else None
        i += 1

        # 질문 수집 (> 나 #### 이전까지)
        question_lines = []
        while i < len(lines) and not lines[i].startswith(">") and not HEADER_RE.match(lines[i].strip()) and not CHOICE_RE.match(lines[i].strip()):
            if lines[i].strip():
                question_lines.append(lines[i].strip())
            i += 1
        question = " ".join(question_lines)

        # 객관식: 선택지 수집
        choices = []
        correct_index = -1
        if qtype_raw == "객관식":
            while i < len(lines) and not lines[i].startswith(">") and not HEADER_RE.match(lines[i].strip()):
                cm = CHOICE_RE.match(lines[i].strip())
                if cm:
                    is_correct = bool(cm.group(2))
                    choice_text = cm.group(3).strip()
                    if is_correct:
                        correct_index = len(choices)
                    choices.append(choice_text)
                i += 1

        # > 줄: 첫 번째 = 정답/ox/fill, 두 번째 = 해설
        blockquotes = []
        while i < len(lines) and lines[i].startswith(">"):
            blockquotes.append(lines[i][1:].strip())
            i += 1

        row: dict = {
            "category_id": category_id,
            "concept": concept,
            "tag": tag,
            "question": question,
            "choices": choices,
            "correct_index": correct_index,
            "ox_answer": "",
            "fill_answer": "",
            "explanation": blockquotes[1] if len(blockquotes) > 1 else "",
        }
        if rid is not None:
            row["id"] = rid

        if qtype_raw == "OX":
            row["type"] = "ox"
            row["ox_answer"] = blockquotes[0] if blockquotes else ""
        elif qtype_raw == "빈칸":
            row["type"] = "fill"
            row["fill_answer"] = blockquotes[0] if blockquotes else ""
        else:
            row["type"] = "mcq"
            row["explanation"] = blockquotes[0] if blockquotes else ""

        rows.append(row)

    return rows



def upsert_row(row: dict) -> int:
    if "id" in row:
        url = f"{SUPABASE_URL}/rest/v1/quiz_questions?on_conflict=id"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates",
        }
    else:
        url = f"{SUPABASE_URL}/rest/v1/quiz_questions"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
        }

    req = urllib.request.Request(
        url,
        data=json.dumps(row).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status


def main():
    files = glob.glob("quiz/*/*.md")
    if not files:
        print("No .md files found in quiz/")
        return

    errors, inserts, updates = [], [], []

    for filepath in sorted(files):
        try:
            rows = parse_file(filepath)
            for row in rows:
                is_new = "id" not in row
                if is_new:
                    print(f"⚠  SKIP (id 없음): {filepath} — {row['question'][:40]}")
                    continue

                upsert_row(row)
                label = f"[{row['id']}] {row['question'][:35]}..."
                if is_new:
                    inserts.append(label)
                    print(f"✚  INSERT {label}")
                else:
                    updates.append(label)
                    print(f"↻  UPDATE {label}")
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
