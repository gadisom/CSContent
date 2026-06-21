# Terms — 앱 단어장 초안

`terms/`는 앱의 단어장 기능을 위한 원천 문서다.

`scripts/sync_terms_to_supabase.py`가 `word_terms` 테이블에 동기화한다.
기존 `published/`는 개념 학습 문서, `quiz/`는 문제풀이, `terms/`는 빠른 용어 회상용으로 분리한다.

## 파일 구조

```text
terms/
  algorithms.md
  android.md
  data-structure.md
  database.md
  ios.md
  network.md
  oop.md
  operating-system.md
  server.md
```

## 항목 포맷

```markdown
## TTL
- answer: DNS 응답이나 네트워크 정보가 유효한 시간
- detail: Time To Live의 줄임말이다. DNS에서는 캐시된 응답을 얼마나 오래 재사용할 수 있는지 나타낸다.
```

## 필드

- `answer`: 정답 보기에서 먼저 보여줄 짧은 정의.
- `detail`: 한두 문장 정도의 보충 설명.

## 동기화 규칙

- `terms/*.md`가 동기화 대상이다.
- `terms/README.md`는 설명 파일이므로 제외된다.
- `id`는 `<category>_<term_slug>` 형태로 자동 생성된다.
- `display_order`는 파일 내 등장 순서대로 1001, 1002, 1003... 형태로 생성된다.
- 같은 category에서 로컬 파일에 없는 기존 `word_terms` row는 삭제된다.
