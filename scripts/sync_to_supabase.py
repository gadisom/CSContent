"""
published/<category>/<subcategory>/<slug>.json 구조를 읽어 Supabase에 upsert한다.
- category_slug: 상위 폴더명
- subcategory_slug: 하위 폴더명
- slug: 파일명 (.json 제외)

폴더 구조가 DB 매핑의 소스 오브 트루스.
새 소주제 폴더를 만들고 JSON 추가 후 push하면 자동으로 DB에 반영된다.

필요한 GitHub Secrets:
  SUPABASE_URL         — https://<project-ref>.supabase.co
  SUPABASE_SERVICE_KEY — service_role 키
  SUPABASE_TABLE       — 테이블 이름 (예: content_items)
"""

import glob
import json
import os
import sys
import urllib.error
import urllib.request
import uuid

SUPABASE_URL = os.environ["SUPABASE_URL"].rstrip("/")
SUPABASE_KEY = os.environ["SUPABASE_SERVICE_KEY"]
TABLE = os.environ["SUPABASE_TABLE"]


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
        return {row["slug"] for row in json.loads(resp.read())}


def upsert(data: dict):
    if not data.get("id") or "UUID" in str(data["id"]):
        data["id"] = str(uuid.uuid4())

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
    # published/<category>/<subcategory>/<slug>.json
    files = glob.glob("published/*/*/*.json")
    if not files:
        print("No JSON files found in published/")
        return

    existing_slugs = fetch_existing_slugs()
    print(f"DB 기존 콘텐츠: {len(existing_slugs)}개\n")

    errors, inserts, updates = [], [], []

    for filepath in sorted(files):
        parts = filepath.replace("\\", "/").split("/")
        # parts: ['published', '<category>', '<subcategory>', '<slug>.json']
        category_slug = parts[1]
        subcategory_slug = parts[2]
        slug = parts[3].replace(".json", "")

        try:
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)

            # 폴더 구조가 소스 오브 트루스 — JSON 내 값을 덮어씀
            data["category_slug"] = category_slug
            data["subcategory_slug"] = subcategory_slug
            data["slug"] = slug

            is_new = slug not in existing_slugs
            upsert(data)

            if is_new:
                inserts.append(slug)
                print(f"✚  INSERT: {category_slug}/{subcategory_slug}/{slug}")
            else:
                updates.append(slug)
                print(f"↻  UPDATE: {category_slug}/{subcategory_slug}/{slug}")

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
