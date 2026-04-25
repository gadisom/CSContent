> Swift OOP는 클래스의 상속·캡슐화에 프로토콜이 더해져 값 타입(struct)으로도 객체지향 설계를 구현할 수 있다.

## 정의
- 객체지향 프로그래밍(OOP): 데이터와 동작을 하나의 객체로 묶고 캡슐화·상속·다형성·추상화 4원칙으로 설계하는 패러다임
- 캡슐화: 내부 상태를 숨기고 공개 인터페이스만 노출하는 것. Swift에서는 private/internal/public/open 접근 제어자로 구현
- 상속: 부모 클래스의 속성과 메서드를 자식 클래스가 물려받는 것. Swift는 단일 상속만 지원하며 class 타입에서만 가능
- final: 클래스나 메서드의 상속·오버라이딩을 금지하는 키워드. 컴파일러가 static dispatch를 적용해 dynamic dispatch 오버헤드를 제거함
- dynamic dispatch: 런타임에 실제 호출할 메서드를 vtable에서 탐색하는 방식. class의 기본 동작
- static dispatch: 컴파일 타임에 호출 메서드가 확정되는 방식. struct·final·@inlinable 등에서 적용

## 핵심 포인트
- Swift의 struct와 enum은 상속을 지원하지 않는다. 상속이 필요한 경우에만 class를 선택한다.
- 단일 상속 한계는 Protocol 다중 채택으로 극복한다. class가 여러 Protocol을 동시에 구현할 수 있다.
- final class는 서브클래싱을 막고 static dispatch를 보장해 성능과 의도를 동시에 명확히 한다.
- 접근 제어 기본값은 internal(같은 모듈 내 공개). 외부 모듈 서브클래싱까지 허용하려면 open이 필요하다.
- 값 타입(struct)은 복사 의미론으로 공유 상태 문제를 원천 차단해 멀티스레드 환경에서 안전하다.

## 면접 질문
- Swift에서 struct와 class의 차이를 설명하고 각각 어떤 상황에 사용하나요?
- final 키워드가 성능에 미치는 영향은 무엇인가요?
- Swift가 다중 상속을 지원하지 않는 이유와 대안은 무엇인가요?

## 확인 문제
- Swift에서 상속이 가능한 타입은 무엇인가요?
- final 클래스에 적용되는 dispatch 방식은 무엇인가요?
- open과 public의 차이는 무엇인가요?

## 키워드
OOP, 객체지향, 캡슐화, 상속, class, struct, final, open, public, dynamic dispatch, static dispatch, override

## 연관 콘텐츠
- [[추상화]]
- [[다형성]]
