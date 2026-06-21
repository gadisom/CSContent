# CSContent Wiki — 스키마 & 운영 가이드

이 파일은 Codex가 이 위키를 어떻게 유지·관리해야 하는지를 정의한다.
새 세션이 시작되면 항상 이 파일을 먼저 읽어라.

---

## 위키의 목적

이 위키는 **CS 지식 앱(CSContent)** 의 콘텐츠 제작 파이프라인이다.

**핵심 플로우:**
```
Raw 자료 (사용자 제공)
    ↓
[Codex 처리]
    ↓
wiki/concepts/<slug>.md   ← Obsidian에서 보는 지식 문서
wiki/content/<slug>.md    ← JSON 포함 (앱에 전달할 최종 결과물)
```

원칙:
- `wiki/` 는 Codex가 쓰고 관리한다. 사용자는 읽는다.
- `raw/` 는 사용자가 넣는 원본 자료다. Codex는 읽기만 한다.
- 모든 변경은 `wiki/log.md` 에 기록한다.
- 새 세션 시작 시 `wiki/index.md` → `wiki/log.md` → 관련 페이지 순서로 읽어서 컨텍스트를 복원한다.

---

## 앱 데이터 모델

### 카테고리 구조
```
category (대분류)
  └── subcategory (소분류)
        └── content item (개념 콘텐츠)
```

### 대분류 (category) 목록
| category_slug | category_title |
|---------------|---------------|
| data-structure | 자료구조 |
| algorithm | 알고리즘 |
| operating-system | 운영체제 |
| database | 데이터베이스 |
| network | 네트워크 |
| ios | iOS |
| android | Android |
| server | Server |
| oop | 객체지향 |

### Content Item JSON 스키마
```json
{
  "id": "<UUID v4>",
  "category_slug": "<대분류 slug>",
  "category_title": "<대분류 한국어 이름>",
  "subcategory_slug": "<소분류 slug>",
  "subcategory_title": "<소분류 한국어 이름>",
  "slug": "<콘텐츠 고유 slug>",
  "title": "<콘텐츠 제목>",
  "summary": "<한 줄 요약 — 핵심 대비를 담은 문장>",
  "blocks": [ ... ],
  "keywords": ["키워드1", "키워드2", ...],
  "related_item_ids": ["<다른 콘텐츠 slug>", ...],
  "display_order": <숫자>,
  "is_published": false,
  "created_at": "<ISO8601>",
  "updated_at": "<ISO8601>"
}
```

### Block 타입 정의
각 block은 `{ "type": "<타입>", "items": ["..."] }` 형태다.

| type | 역할 | items 형식 |
|------|------|-----------|
| `definition` | 개념 정의 | `["<용어>: <정의>", ...]` |
| `keyPoints` | 핵심 포인트 | `["<포인트 문장>", ...]` |
| `interviewPrompts` | 면접 질문 | `["<질문>", ...]` |
| `checkQuestions` | 확인 문제 | `["<질문>", ...]` |
| `image` | 이미지 | `["<URL>"]` |
| `codeExample` | 코드 예시 | `["<언어>:<코드>"]` (추가 시 확인) |
| `comparison` | 비교표 | (추가 시 확인) |

*알려지지 않은 block type은 사용자에게 확인 후 이 표에 추가한다.*

### Slug 네이밍 규칙
- category slug: `data-structure`, `algorithm`, `operating-system`, `database`, `network`
- subcategory slug: `<약어>-<주제>` (예: `array-linked-list`, `stack-queue`)
- content slug: `<category 약어>-<주제>` (예: `ds-array-vs-linked-list`, `alg-binary-search`)
- category 약어: ds / alg / os / db / net

### display_order 규칙
- 카테고리 내에서 **1000 단위 증분**: 1001, 2001, 3001, ...
- 신규 콘텐츠는 해당 카테고리의 마지막 번호 + 1000
- 예외적으로 같은 소분류 내 연속 항목은 +1 허용 (예: 4001, 4002)
- **반드시 `wiki/index.md` 의 display_order 현황을 먼저 확인한다**
- slug 중복도 index.md에서 확인 후 생성

---

## 디렉토리 구조

```
CSContent/
├── AGENTS.md                  # 이 파일 — 스키마 & 운영 가이드
├── published/                 # ★ 앱에 전달되는 콘텐츠 (폴더 구조 = DB 매핑)
│   ├── data-structure/
│   │   ├── array-linked-list/
│   │   │   └── ds-array-vs-linked-list.json
│   │   └── stack-queue/
│   ├── algorithms/
│   │   └── graph-search/
│   │       └── algo-graph-bfs-dfs.json
│   ├── operating-system/
│   ├── database/
│   └── network/
├── terms/                     # 앱 단어장 원천 문서 (word_terms 동기화)
│   ├── README.md
│   └── network.md
├── wiki/
│   ├── index.md               # 전체 위키 카탈로그 + display_order 현황
│   ├── log.md                 # 활동 로그 (append-only)
│   ├── overview.md            # CS 커버리지 현황 및 로드맵
│   ├── concepts/              # 개념 지식 문서 (읽기용, 앱 전달 X)
│   ├── topics/                # 주제 영역 페이지
│   └── meta/                  # 앱 기능, 운영 가이드
└── raw/                       # 원본 자료 (변경 금지)
    └── assets/
```

### published/ 폴더 규칙
- `published/<category_slug>/<한국어 제목>.md`
- **폴더명** → `category_slug` (자동 매핑)
- **파일명** (`.md` 제외) → `title` = `subcategory_title` (자동)
- **`id`** → 스크립트가 자동 생성 (기존 slug면 기존 UUID 유지, 신규면 uuid4())
- **`is_published`** → 항상 `true` (published/ 안에 있으면 발행된 것)

### terms/ 단어장 규칙
- `terms/<category_slug>.md`
- 파일 하나가 하나의 대분류 단어장을 나타낸다. 예: `terms/network.md`
- 앱에서는 “단어 카드 → 정답 보기 → detail 확인” 흐름으로 사용한다.
- `scripts/sync_terms_to_supabase.py`가 `terms/*.md`를 `word_terms` 테이블에 동기화한다.
- `terms/README.md`는 포맷 설명 파일이므로 동기화 대상에서 제외한다.
- `terms/`가 SSOT이므로, 같은 `category_id`에서 로컬 파일에 없는 기존 단어 row는 동기화 시 삭제된다.
- `id`는 `<category>_<term_slug>` 형태로 스크립트가 자동 생성한다. 예: `network_ttl`
- `display_order`는 파일 내 등장 순서대로 1001, 1002, 1003... 형태로 자동 생성한다.
- `is_published`는 항상 `true`로 동기화한다.

### Terms MD 템플릿

```markdown
---
category: network
title: 네트워크 단어장
---

# 네트워크 단어장

## TTL
- answer: DNS 응답이나 네트워크 정보가 유효한 시간
- detail: Time To Live의 줄임말이다. DNS에서는 캐시된 응답을 얼마나 오래 재사용할 수 있는지 나타낸다.
```

### Terms 필드 규칙
- `## <term>`: 카드 앞면에 표시할 용어다.
- `answer`: 정답 보기에서 먼저 보여줄 짧은 정의다.
- `detail`: 풀네임, 맥락, 예시를 포함한 1~2문장 보충 설명이다.
- `full`, `related`, `tags` 같은 별도 필드는 두지 않는다. 필요한 풀네임은 `detail` 안에 자연스럽게 적는다.
- 단어장은 빠른 회상용이므로 `answer`는 짧게, `detail`도 과하게 길게 쓰지 않는다.

### MD 템플릿 (반드시 이 형식 준수)

```markdown
---
slug: <영어-슬러그>
order: <숫자>
related: [slug1, slug2]
---

> 한 줄 요약

## 정의
- 항목1
- 항목2

## 핵심 포인트
- 항목1

## 면접 질문
- 질문1

## 확인 문제
- 질문1

## 키워드
키워드1, 키워드2, 키워드3
```

### 섹션 → block type 매핑
| MD 섹션 | block type |
|---------|-----------|
| `## 정의` | `definition` |
| `## 핵심 포인트` | `keyPoints` |
| `## 면접 질문` | `interviewPrompts` |
| `## 확인 문제` | `checkQuestions` |
| `## 키워드` | keywords 배열 (block 아님) |
| `> 텍스트` | summary (block 아님) |

### 콘텐츠 문체 규칙
- `## 정의`에는 개념의 의미, 역할, 구성 요소만 적는다.
- `## 정의`와 `## 핵심 포인트`에는 `면접에서는`, `면접에선`, `인터뷰에서는`처럼 면접 상황을 직접 언급하는 문장을 넣지 않는다.
- 면접 답변 요령이나 답변 관점은 `## 면접 질문`의 질문으로 유도하거나, wiki/concepts 문서의 `## 면접 포인트`에서만 다룬다.
- published/ 문서는 앱 학습 콘텐츠이므로 본문 설명에는 시험/면접 조언 문체를 섞지 않는다.

### SDUI semantic token 규칙
- published/ 문서를 생성하거나 보강할 때 핵심 용어와 중요한 문장은 semantic token으로 표시할 수 있다.
- 직접 색상값(`#FF0000`)이나 글자 크기(`18px`, `24px`)처럼 디자인 시스템을 침범하는 값을 MD에 쓰지 않는다.
- 허용 토큰: `{.accent}`, `{.danger}`, `{.success}`, `{.warning}`, `{.muted}`, `{.term}`, `{.lead}`, `{.caption}`.
- 기술 용어는 `[TCP]{.term}`, 핵심 강조는 `[핵심 문장]{.accent}`, 주의는 `[주의할 점]{.warning}`처럼 작성한다.
- 한 줄 요약에는 필요한 경우 `> [요약 문장]{.lead}`를 사용할 수 있다.
- 코드/용어 백틱과 semantic token을 섞지 않는다. 금지: `` `[4-tuple]{.term}` ``. 허용: `[4-tuple]{.term}`.
- 토큰은 의미가 있는 부분에만 사용하고, 모든 단어를 장식하지 않는다.
- 현재 sync 구조에서는 토큰 문법이 block item 문자열로 그대로 전달되므로, 클라이언트가 파싱 가능한 위 문법만 사용한다.

---

## 페이지 포맷

### wiki/concepts/<slug>.md — 개념 지식 문서
```markdown
---
tags: [concept]
category: <category_slug>
subcategory: <subcategory_slug>
difficulty: <beginner|intermediate|advanced>
content_slug: <연결된 content slug>
---

# <개념 제목>

## 핵심 요약

## 상세 설명

## 키포인트

## 면접 포인트

## 관련 개념
- [[concepts/<slug>]]

## 연결된 콘텐츠
- [[content/<slug>]]
```

### wiki/content/<slug>.md — 앱 전달용 콘텐츠
```markdown
---
tags: [content]
category: <category_slug>
subcategory: <subcategory_slug>
status: <draft|published>
created: <YYYY-MM-DD>
---

# <제목>

## 요약
<summary 문장>

## 키워드
<keywords>

## 연관 콘텐츠
<related_item_ids>

---

## 앱 JSON

\`\`\`json
{
  ... (완성된 JSON)
}
\`\`\`
```

---

## 운영 워크플로우

### Ingest (원자료 → 문서 + JSON)
트리거: 사용자가 raw 자료를 주고 처리를 요청할 때

1. 자료 읽기 (raw 파일 또는 사용자가 직접 붙여넣기)
2. `wiki/index.md` 에서 slug 중복 확인 및 display_order 확인
3. category / subcategory / slug 확정
4. `published/<category>/<한국어제목>.md` 생성 또는 수정
5. `quiz/<category>/<개념>.md` 생성 (OX/빈칸/객관식 포함)
6. `wiki/index.md` 업데이트 (새 항목 추가, display_order 현황 갱신)
7. `wiki/log.md` 항목 추가

**주의:**
- slug 중복 여부를 index.md에서 반드시 확인
- display_order: 해당 category 마지막 번호 + 1000
- is_published 기본값: true
- 빈칸 문제 정답은 반드시 단일 단어/용어만 (O(n) 같은 수식 금지)

### 신규 대분류(category) 생성 시 체크리스트
기존 5개 외 새 카테고리가 필요할 때 반드시 아래를 모두 처리한다.

1. `published/<new-category>/` 폴더 생성
2. `quiz/<new-category>/` 폴더 생성
3. 필요한 경우 `terms/<new-category>.md` 생성
4. `scripts/sync_to_supabase.py` → `CATEGORY_TITLES` 딕셔너리에 추가
5. `AGENTS.md` → 대분류 목록 테이블에 추가
6. `wiki/index.md` → display_order 현황 테이블에 추가
7. `wiki/log.md` 에 기록

> `quiz_categories` 테이블은 push 시 `sync_to_supabase.py`가 `published/` 폴더 목록을 읽어 자동 동기화한다. 수동 SQL 불필요.

### Terms (단어장 생성/수정)
트리거: 사용자가 단어장, 용어장, 카드 학습용 용어 정리를 요청할 때

1. 관련 `published/` 문서를 읽어 용어 후보를 뽑는다.
2. 기존 `terms/<category>.md`가 있으면 같은 용어 중복을 확인한다.
3. 용어별로 `answer`와 `detail`만 작성한다.
4. `answer`는 카드 정답으로 바로 보일 짧은 정의로 작성한다.
5. `detail`에는 풀네임, 맥락, 주의점을 1~2문장으로 적는다.
6. `terms/README.md` 포맷을 벗어나지 않는다.
7. `wiki/log.md`에 변경 사항을 기록한다.

**주의:**
- 단어장에는 `full`, `related`, `tags` 필드를 만들지 않는다.
- 단어장 항목은 앱 카드 단위이므로 한 항목에 여러 개념을 섞지 않는다.
- Supabase 업로드는 `scripts/sync_terms_to_supabase.py`와 GitHub Actions가 처리한다.

### Query (현황 파악 / 추천)
트리거: "뭐가 빠져있어?", "다음에 뭘 만들면 좋을까?"

1. `wiki/index.md` 읽기
2. topics 페이지 읽기
3. 갭 분석 후 우선순위 추천

### Lint (위키 건강 검사)
트리거: "위키 정리해줘"

1. orphan 개념 (content 없는 개념 페이지) 탐색
2. related_item_ids 유효성 확인 (존재하지 않는 slug 참조)
3. display_order 충돌 확인
4. `wiki/log.md` 에 lint 결과 기록

---

## 로그 컨벤션

```
## [YYYY-MM-DD] <action> | <title>
<한 줄 요약>
생성/변경된 파일: <목록>
```

action: `ingest`, `query`, `lint`, `meta`

---

## 주의사항

- `raw/` 파일은 절대 수정하지 않는다.
- Obsidian 내부 링크: `[[파일명]]`
- 파일명: 영어 소문자 + 하이픈
- 날짜: 절대 날짜 `YYYY-MM-DD`
- JSON의 `id` 는 매번 새 UUID v4를 생성한다: `python3 -c "import uuid; print(uuid.uuid4())"` 로 생성.
- `is_published: true` 가 기본값. push하면 바로 앱에 노출됨.
