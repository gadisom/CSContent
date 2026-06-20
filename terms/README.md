# Terms — 앱 단어장 초안

`terms/`는 앱의 단어장 기능을 위한 원천 문서다.

현재는 프론트 기능 준비 전 단계이므로 Supabase 동기화 대상이 아니다.
기존 `published/`는 개념 학습 문서, `quiz/`는 문제풀이, `terms/`는 빠른 용어 회상용으로 분리한다.

## 파일 구조

```text
terms/
  network.md
  ios.md
  database.md
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
