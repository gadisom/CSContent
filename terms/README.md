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
- full: Time To Live
- answer: DNS 응답이나 네트워크 정보가 유효한 시간
- detail: DNS에서는 캐시된 응답을 얼마나 오래 재사용할 수 있는지 나타낸다.
- related: [DNS]
- tags: [DNS, 캐시]
```

## 필드

- `full`: 약어의 풀네임. 풀네임이 없으면 생략할 수 있다.
- `answer`: 정답 보기에서 먼저 보여줄 짧은 정의.
- `detail`: 한두 문장 정도의 보충 설명.
- `related`: 연결할 `published/` 콘텐츠 제목.
- `tags`: 검색과 묶음 학습에 사용할 키워드.
