> Prepared Statement는 SQL 구조를 미리 컴파일하고 값을 바인딩해 실행하므로, 재사용성과 보안 측면에서 일반 Statement보다 유리하다.

## 정의
- Statement는 SQL 문자열을 매번 완성해서 실행하는 방식이다. 동적으로 만들기 쉽지만, 입력값을 그대로 문자열에 이어 붙이면 보안 문제가 생기기 쉽다.
- Prepared Statement는 SQL 구조를 먼저 준비하고 값만 바꿔 넣는 방식이다. 반복 실행에 유리하고, 파라미터 바인딩을 통해 SQL Injection 위험을 낮출 수 있다.
- 면접에서는 성능만 강조하지 말고, 구조와 데이터를 분리해 다루는 설계적 장점을 함께 설명하는 것이 좋다.

## 핵심 포인트
- Prepared Statement는 값 바인딩 기반 실행이다.
- SQL 구조와 데이터를 분리해 보안에 유리하다.
- 반복 실행 시 재사용 이점이 있다.

## 면접 질문
- Statement와 Prepared Statement를 비교해보세요.
- Prepared Statement가 보안에 유리한 이유는 무엇인가요?

## 확인 문제
- 입력값을 문자열 결합으로 붙이면 위험할 수 있을까?
- Prepared Statement는 값만 바꿔 반복 실행하기 좋을까?

## 키워드
Statement, Prepared Statement, 바인딩, SQL Injection, 재사용

## 연관 콘텐츠
- [[SQL Injection]]
- [[데이터베이스 기본]]
