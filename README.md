# CSContent

CS 지식 앱의 콘텐츠 제작 파이프라인. `raw/`에 자료를 넣으면 Claude가 처리해 앱까지 자동 배포된다.

---

## 플로우

```
raw/        ← 팀원이 클리핑/노트를 넣는 곳
    ↓  Claude 처리
published/  ← 앱에 전달되는 콘텐츠 (형식 맞춰 생성)
quiz/       ← 퀴즈 문항 (OX / 빈칸 / 객관식)
    ↓  git push
GitHub Actions → Supabase 자동 동기화
```

---

## 폴더 구조

```
CSContent/
├── raw/                  # 원본 자료 넣는 곳 (수정 금지)
│   └── assets/           # 이미지 파일
├── published/            # 앱 콘텐츠 (카테고리/파일명.md)
│   ├── algorithms/
│   ├── data-structure/
│   ├── database/
│   ├── network/
│   ├── operating-system/
│   ├── ios/
│   ├── android/
│   └── server/
├── quiz/                 # 퀴즈 문항 (카테고리/개념.md)
├── categories/           # 카테고리 메타 (아이콘, 색상)
├── templates/            # Obsidian 자동 템플릿
└── scripts/              # Supabase 동기화 스크립트
```

---

## 콘텐츠 추가하기

### 1. raw에 자료 넣고 Claude에게 요청하기

공부한 내용, 클리핑한 아티클, 직접 작성한 노트 등 형식 무관하게 `raw/`에 넣는다.
이미지가 있으면 `raw/assets/`에 함께 넣는다.

그 다음 Claude Code(이 레포가 열린 터미널)에게 한 줄로 요청한다.

```
raw에 있는 '파일명.md' 추가해줘
```

Claude가 자동으로 아래 작업을 수행한다.

1. raw 파일 내용 분석 → 카테고리·개념 판단
2. `published/<카테고리>/<제목>.md` 생성 (앱 형식에 맞게 재구성)
3. `quiz/<카테고리>/<제목>.md` 생성 (OX·빈칸·객관식 문항 포함)
4. `wiki/index.md`, `wiki/log.md` 자동 업데이트
5. git commit & push → GitHub Actions → Supabase 자동 반영

### 2. published 파일 형식

`published/<카테고리>/<한국어 제목>.md`

```markdown
> 한 줄 요약 (핵심 대비를 담은 문장)

## 정의
- 항목: 설명

## 핵심 포인트
- 포인트

## 면접 질문
- 질문

## 확인 문제
- 질문

## 키워드
키워드1, 키워드2

## 연관 콘텐츠
- [[다른 파일명]]
```

> 파일명 = 앱에 표시되는 제목. `display_order`는 파일명 알파벳 순으로 자동 계산된다.

### 3. 이미지 삽입

```markdown
## 정의
- 설명
![[로컬파일.png]]          ← raw/assets/ 에 있는 이미지

![](https://example.com/img.png)  ← 외부 URL 이미지
```

두 형식 모두 지원된다.

---

## 퀴즈 추가하기

`quiz/<카테고리>/<개념>.md`

```markdown
---
category: algorithms
tag: 탐색
---

#### OX | [id]
질문
> O 또는 X
> 해설

#### 빈칸 | [id]
___ 를 포함한 질문
> 정답 (단일 단어/용어만)
> 해설

#### 객관식 | [id]
질문
1. 선택지
2. ✅ 정답 선택지
3. 선택지
> 해설
```

**규칙:**
- `[id]` 에 숫자가 있으면 upsert, `[]` 면 에러 발생 → **반드시 숫자 id를 넣어야 한다**
- 현재 마지막 id는 `quiz/` 폴더 파일들에서 `grep "| \[" quiz/*/*.md` 로 확인
- 빈칸 정답은 단일 단어/용어만 (수식, 긴 문장 금지)

---

## 카테고리 추가하기

새 카테고리가 필요할 때 아래를 모두 처리한다.

**1. 폴더 생성**
```
published/<slug>/
quiz/<slug>/
```

**2. 카테고리 메타 파일 생성** — `categories/<slug>.md`
```markdown
---
id: <slug>
name: <한국어 또는 영어 이름>
icon: <SF Symbol 이름>
icon_color: "#XXXXXX"
icon_bg_color: "#XXXXXX"
---
```

**3. `scripts/sync_to_supabase.py`** — `CATEGORY_TITLES` 에 추가
```python
"<slug>": "<표시 이름>",
```

**4. `CLAUDE.md`** — 대분류 목록 테이블에 추가

push하면 `quiz_categories` 테이블에 자동 반영된다.

---

## 배포

```bash
git add .
git commit -m "내용 설명"
git push origin main
```

push하면 GitHub Actions가 자동 실행된다.

| 스크립트 | 역할 |
|---------|------|
| `sync_to_supabase.py` | `published/` → `content_items` 테이블 upsert |
| `sync_quiz_to_supabase.py` | `quiz/` → `quiz_questions` 테이블 upsert |
---

