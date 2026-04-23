---
tags: [meta]
---

# 앱 기능 현황 & 데이터 모델

마지막 업데이트: 2026-04-24

---

## 구현 완료된 기능

- **퀴즈** — 퀴즈 생성 및 풀기
- **개념 설명** — 블록 기반 콘텐츠 렌더링

---

## 카테고리 구조

```
category_slug       category_title
─────────────────────────────────
data-structure      자료구조
algorithm           알고리즘
operating-system    운영체제
database            데이터베이스
network             네트워크
```

---

## Block 타입 (UI 렌더링 단위)

| type | 역할 |
|------|------|
| `definition` | 용어 정의 |
| `keyPoints` | 핵심 포인트 bullet |
| `interviewPrompts` | 면접 예상 질문 |
| `checkQuestions` | 복습 확인 질문 |
| `image` | 이미지 URL |

*추가 block type 발견 시 여기에 기록*

---

## Content Item 예시

```json
{
  "id": "3c25c2a9-9ff9-458d-b655-7b97f163e20c",
  "category_slug": "data-structure",
  "category_title": "자료구조",
  "subcategory_slug": "array-linked-list",
  "subcategory_title": "배열과 연결리스트",
  "slug": "ds-array-vs-linked-list",
  "title": "배열과 연결리스트의 차이",
  "summary": "배열은 연속된 메모리를 사용해 인덱스 접근이 빠르고, 연결리스트는 노드 연결 구조라 삽입과 삭제 위치에 따라 더 유연함",
  "blocks": [
    { "type": "definition", "items": ["..."] },
    { "type": "image", "items": ["https://.../image.jpg"] },
    { "type": "keyPoints", "items": ["..."] },
    { "type": "interviewPrompts", "items": ["..."] },
    { "type": "checkQuestions", "items": ["..."] }
  ],
  "keywords": ["배열", "연결리스트", "메모리 연속성", "삽입 삭제", "인덱스 접근"],
  "related_item_ids": ["alg-time-complexity", "ds-stack-vs-queue"],
  "display_order": 1001,
  "is_published": true
}
```

---

## Slug 약어 체계

| category | 약어 | display_order 시작 |
|----------|------|-------------------|
| data-structure | ds | 1001 |
| algorithm | alg | 2001 |
| operating-system | os | 3001 |
| database | db | 4001 |
| network | net | 5001 |

---

## 관련 페이지
- [[meta/content-guidelines]]
- [[overview]]
