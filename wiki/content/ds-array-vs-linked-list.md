---
tags: [content]
category: data-structure
subcategory: array-linked-list
status: draft
created: 2026-04-24
---

# 배열과 연결리스트의 차이

## 요약
배열은 연속된 메모리를 사용해 인덱스 접근이 빠르고, 연결리스트는 노드 연결 구조라 삽입과 삭제 위치에 따라 더 유연함

## 키워드
배열, 연결리스트, 메모리 연속성, 삽입 삭제, 인덱스 접근, 시간복잡도

## 연관 콘텐츠
- ds-stack-vs-queue
- alg-time-complexity

---

## 앱 JSON

```json
{
  "id": "3829b040-b339-491d-8b23-d9ee03b57242",
  "category_slug": "data-structure",
  "category_title": "자료구조",
  "subcategory_slug": "array-linked-list",
  "subcategory_title": "배열과 연결리스트",
  "slug": "ds-array-vs-linked-list",
  "title": "배열과 연결리스트의 차이",
  "summary": "배열은 연속된 메모리를 사용해 인덱스 접근이 빠르고, 연결리스트는 노드 연결 구조라 삽입과 삭제 위치에 따라 더 유연함",
  "blocks": [
    {
      "type": "definition",
      "items": [
        "배열(Array): 메모리에 연속적으로 저장되는 자료구조. 인덱스로 O(1) 임의 접근 가능",
        "연결리스트(Linked List): 각 노드가 데이터와 다음 노드의 포인터를 가지는 자료구조. 메모리 비연속 저장"
      ]
    },
    {
      "type": "keyPoints",
      "items": [
        "배열은 인덱스 접근 O(1), 중간 삽입·삭제 O(n)",
        "연결리스트는 임의 접근 O(n), 위치를 알 때 삽입·삭제 O(1)",
        "배열은 캐시 지역성이 좋아 실제 성능이 더 빠른 경우가 많음",
        "연결리스트는 포인터 저장을 위한 추가 메모리가 필요함",
        "읽기 위주라면 배열, 삽입·삭제가 빈번하면 연결리스트가 유리"
      ]
    },
    {
      "type": "interviewPrompts",
      "items": [
        "배열과 연결리스트의 차이를 설명해보세요",
        "언제 배열 대신 연결리스트를 선택하나요?",
        "이중 연결리스트는 단순 연결리스트와 어떻게 다른가요?",
        "동적 배열(ArrayList)은 내부적으로 어떻게 동작하나요?"
      ]
    },
    {
      "type": "checkQuestions",
      "items": [
        "배열에서 인덱스 접근이 O(1)인 이유는 무엇인가요?",
        "연결리스트에서 삽입이 O(1)이 되려면 어떤 조건이 필요한가요?",
        "배열의 중간에 원소를 삽입할 때 시간복잡도는?"
      ]
    }
  ],
  "keywords": ["배열", "연결리스트", "메모리 연속성", "삽입 삭제", "인덱스 접근", "시간복잡도"],
  "related_item_ids": ["ds-stack-vs-queue", "alg-time-complexity"],
  "display_order": 1001,
  "is_published": false,
  "created_at": "2026-04-24T00:00:00.000000+00:00",
  "updated_at": "2026-04-24T00:00:00.000000+00:00"
}
```
