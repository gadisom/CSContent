"""
wiki/content/*.md 파일에서 JSON 블록을 추출해 Supabase에 upsert한다.
slug를 기준으로 충돌 해결 (이미 있으면 업데이트, 없으면 insert).

필요한 GitHub Secrets:
  SUPABASE_URL         — https://<project-ref>.supabase.co
  SUPABASE_SERVICE_KEY — service_role 키 (anon 키 아님)
  SUPABASE_TABLE       — 테이블 이름 (예: content_items)
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


def extract_json(filepath: str) -> dict | None:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"```json\s*\n(.*?)\n```", content, re.DOTALL)
    if not match:
        return None
    return json.loads(match.group(1))


def is_placeholder(data: dict) -> bool:
    id_val = str(data.get("id", ""))
    return "UUID" in id_val or "생성" in id_val or not id_val


def fetch_existing_slugs() -> set:
    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?select=slug"
    req = urllib.request.Request(
        url,
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        rows = json.loads(resp.read())
        return {row["slug"] for row in rows}


def upsert(data: dict) -> int:
    if is_placeholder(data):
        data["id"] = str(uuid.uuid4())

    url = f"{SUPABASE_URL}/rest/v1/{TABLE}?on_conflict=slug"
    payload = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
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
    files = sorted(glob.glob("wiki/content/*.md"))
    if not files:
        print("No content files found.")
        return

    existing_slugs = fetch_existing_slugs()
    print(f"DB에 기존 콘텐츠 {len(existing_slugs)}개 확인\n")

    errors = []
    inserts = []
    updates = []

    for filepath in files:
        try:
            data = extract_json(filepath)
            if data is None:
                print(f"⚠  Skip (no JSON block): {filepath}")
                continue

            slug = data["slug"]
            is_new = slug not in existing_slugs

            upsert(data)

            if is_new:
                inserts.append(slug)
                print(f"✚  INSERT: {slug}")
            else:
                updates.append(slug)
                print(f"↻  UPDATE: {slug}")

        except urllib.error.HTTPError as e:
            body = e.read().decode()
            print(f"✗  {filepath} — HTTP {e.code}: {body}")
            errors.append(filepath)
        except Exception as e:
            print(f"✗  {filepath} — {e}")
            errors.append(filepath)

    print(f"\n신규 insert: {len(inserts)}개, 업데이트: {len(updates)}개, 실패: {len(errors)}개")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
