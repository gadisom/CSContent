---
slug: net-http-methods
order: 4001
related: [HTTP와 HTTPS, REST와 RESTful, CORS]
---

> [HTTP 메서드는 클라이언트가 리소스에 대해 어떤 행위를 원하는지 서버에 알려주는 요청의 의미 체계다.]{.lead}

## 정의
![[http-methods-map.png]]

- [HTTP 메서드]{.term}는 요청 대상 리소스에 수행할 행위를 표현한다.
- [GET]{.term}은 리소스 조회를 의미하며, 같은 요청이 서버 상태를 바꾸지 않는 것이 원칙이다.
- [POST]{.term}는 서버에 처리나 생성을 요청할 때 사용하며, 같은 요청을 반복하면 결과가 달라질 수 있다.
- [PUT]{.term}은 리소스 전체를 교체하거나 지정 위치에 저장하는 의미가 강하다.
- [PATCH]{.term}는 리소스의 일부만 수정하는 의미로 사용된다.
- [DELETE]{.term}는 리소스 삭제를 요청하는 메서드다.
- [HEAD]{.term}는 GET과 비슷하지만 응답 본문 없이 헤더만 받는다.
- [OPTIONS]{.term}는 서버가 지원하는 메서드나 CORS preflight 확인에 사용된다.

## 핵심 포인트
- [메서드 선택의 핵심은 데이터 위치가 아니라 요청의 의미]{.accent}다.
- GET은 [안전한 메서드]{.term}로 분류되며 조회에 사용된다.
- PUT과 DELETE는 보통 [멱등]{.term}하게 설계한다.
- POST는 생성, 제출, 실행처럼 결과가 매번 달라질 수 있는 처리에 적합하다.
- [PUT은 전체 교체, PATCH는 부분 수정]{.accent}에 가깝다.
- [URL에 노출되는지 여부는 보안의 본질이 아니며, 민감한 데이터는 HTTPS와 서버 정책으로 보호해야 한다.]{.warning}
- REST API에서는 [URI가 리소스]{.term}를, [HTTP 메서드가 행위]{.term}를 표현한다.

## 면접 질문
- HTTP 메서드의 역할을 설명해보세요.
- GET과 POST의 차이를 안전성과 멱등성 관점에서 설명해보세요.
- PUT과 PATCH는 어떤 기준으로 구분할 수 있나요?
- REST API에서 URI와 HTTP 메서드는 각각 무엇을 표현하나요?

## 확인 문제
- GET과 POST의 차이는 데이터 길이만으로 결정될까?
- 같은 GET 요청을 여러 번 보내도 서버 상태가 바뀌지 않아야 할까?
- PUT은 보통 같은 요청을 반복해도 최종 상태가 같도록 설계할까?
- PATCH는 리소스 전체 교체보다 부분 수정에 더 가깝게 쓰일까?
- OPTIONS는 CORS preflight와 관련이 있을까?

## 키워드
GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS, HTTP 메서드, 안전성, 멱등성, REST

## 연관 콘텐츠
- [[HTTP와 HTTPS]]
- [[REST와 RESTful]]
- [[CORS]]
