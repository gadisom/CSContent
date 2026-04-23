# CSContent Wiki — 스키마 & 운영 가이드

이 파일은 Claude Code가 이 위키를 어떻게 유지·관리해야 하는지를 정의한다.
새 세션이 시작되면 항상 이 파일을 먼저 읽어라.

---

## 위키의 목적

이 위키는 **CS 지식 앱(CSContent)** 의 콘텐츠 제작 파이프라인이다.

**핵심 플로우:**
```
Raw 자료 (사용자 제공)
    ↓
[Claude 처리]
    ↓
wiki/concepts/<slug>.md   ← Obsidian에서 보는 지식 문서
wiki/content/<slug>.md    ← JSON 포함 (앱에 전달할 최종 결과물)
```

원칙:
- `wiki/` 는 Claude가 쓰고 관리한다. 사용자는 읽는다.
- `raw/` 는 사용자가 넣는 원본 자료다. Claude는 읽기만 한다.
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
├── CLAUDE.md                  # 이 파일 — 스키마 & 운영 가이드
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
4. `published/<category>/<subcategory>/<slug>.json` 생성 — 앱 전달용 순수 JSON
5. `wiki/concepts/<slug>.md` 생성 — 지식 문서 (읽기용)
6. `wiki/index.md` 업데이트 (새 항목 추가, display_order 현황 갱신)
7. `wiki/log.md` 항목 추가

**주의:**
- slug 중복 여부를 index.md에서 반드시 확인
- display_order: 해당 category 마지막 번호 + 1000
- is_published 기본값: true

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
