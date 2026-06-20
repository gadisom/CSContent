"""
terms/<category>.md -> word_terms upsert + stale row delete

MD 형식:
---
category: network
title: 네트워크 단어장
---

## TTL
- answer: DNS 응답이나 네트워크 정보가 유효한 시간
- detail: Time To Live의 줄임말이다. DNS에서는 캐시된 응답을 얼마나 오래 재사용할 수 있는지 나타낸다.

규칙:
- id는 <category>_<term slug> 형태로 자동 생성
- terms/가 SSOT이므로, 로컬 파일에 없는 같은 category_id의 기존 row는 삭제
- TERMS_DRY_RUN=1 이면 파싱 결과만 출력하고 Supabase 요청은 보내지 않음
"""

import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request
from typing import Optional

SUPABASE_URL = os.environ.get("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")
TABLE = os.environ.get("SUPABASE_WORD_TERMS_TABLE", "word_terms")
DRY_RUN = os.environ.get("TERMS_DRY_RUN") == "1"


def parse_frontmatter(raw: str) -> dict:
    fm_m = re.match(r"^---\n(.*?)\n---\n", raw, re.DOTALL)
    if not fm_m:
        return {}

    meta = {}
    for line in fm_m.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip().strip('"')
    return meta


def term_slug(term: str) -> str:
    slug = term.strip().lower()
    slug = re.sub(r"[^\w]+", "_", slug, flags=re.UNICODE)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug or "term"


def parse_file(filepath: str) -> list[dict]:
    with open(filepath, encoding="utf-8") as f:
        raw = f.read()

    meta = parse_frontmatter(raw)
    category_id = meta.get("category") or os.path.basename(filepath).replace(".md", "")

    body = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.DOTALL)
    sections = re.split(r"^## (.+)$", body, flags=re.MULTILINE)

    rows = []
    display_order = 1000
    for i in range(1, len(sections), 2):
        term = sections[i].strip()
        content = sections[i + 1] if i + 1 < len(sections) else ""
        fields = {}

        for line in content.splitlines():
            line = line.strip()
            if not line.startswith("- ") or ":" not in line:
                continue
            key, _, value = line[2:].partition(":")
            fields[key.strip()] = value.strip()

        answer = fields.get("answer", "")
        detail = fields.get("detail", "")
        if not answer:
            raise ValueError(f"{filepath} / {term}: answer 필드가 필요합니다")

        display_order += 1
        rows.append(
            {
                "id": f"{category_id}_{term_slug(term)}",
                "category_id": category_id,
                "term": term,
                "answer": answer,
                "detail": detail,
                "tag": fields.get("tag", ""),
                "display_order": display_order,
                "is_published": True,
            }
        )

    return rows


def request_json(url: str, method: str = "GET", payload: Optional[dict] = None):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates",
        },
    )
    with urllib.request.urlopen(req) as resp:
        raw = resp.read()
        return json.loads(raw) if raw else None


def upsert_row(row: dict):
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?on_conflict=id"
    return request_json(url, method="POST", payload=row)


def fetch_existing_ids(category_ids: set[str]) -> set[str]:
    existing = set()
    for category_id in sorted(category_ids):
        url = f"{SUPABASE_URL}/rest/v1/{TABLE}?select=id&category_id=eq.{category_id}"
        rows = request_json(url) or []
        existing.update(row["id"] for row in rows)
    return existing


def delete_row(row_id: str):
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?id=eq.{row_id}"
    return request_json(url, method="DELETE")


def main():
    files = sorted(glob.glob("terms/*.md"))
    files = [f for f in files if os.path.basename(f).lower() != "readme.md"]
    if not files:
        print("No .md files found in terms/")
        return

    errors, inserts, updates, deletes = [], [], [], []
    local_ids: set[str] = set()
    local_category_ids: set[str] = set()
    id_sources: dict[str, str] = {}

    if not DRY_RUN and (not SUPABASE_URL or not SUPABASE_KEY):
        print("SUPABASE_URL and SUPABASE_SERVICE_KEY are required")
        sys.exit(1)

    for filepath in files:
        try:
            rows = parse_file(filepath)
            for row in rows:
                row_id = row["id"]
                if row_id in id_sources:
                    raise ValueError(f"중복 word id {row_id}: {id_sources[row_id]} / {filepath}")
                id_sources[row_id] = filepath
                local_ids.add(row_id)
                local_category_ids.add(row["category_id"])

                if DRY_RUN:
                    updates.append(row_id)
                    print(json.dumps(row, ensure_ascii=False))
                    continue

                upsert_row(row)
                updates.append(row_id)
                print(f"↻  UPSERT [{row['display_order']}] {row['category_id']}/{row['term']}")
        except urllib.error.HTTPError as e:
            print(f"✗  {filepath} — HTTP {e.code}: {e.read().decode()}")
            errors.append(filepath)
        except Exception as e:
            print(f"✗  {filepath} — {e}")
            errors.append(filepath)

    if not DRY_RUN and not errors:
        try:
            existing_ids = fetch_existing_ids(local_category_ids)
            stale_ids = sorted(existing_ids - local_ids)
            for row_id in stale_ids:
                delete_row(row_id)
                deletes.append(row_id)
                print(f"✗  DELETE stale word id: {row_id}")
        except urllib.error.HTTPError as e:
            print(f"✗  stale delete — HTTP {e.code}: {e.read().decode()}")
            errors.append("stale delete")
        except Exception as e:
            print(f"✗  stale delete — {e}")
            errors.append("stale delete")

    print(
        f"\n신규/업데이트: {len(updates)}개  삭제: {len(deletes)}개  "
        f"실패: {len(errors)}개"
    )
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
