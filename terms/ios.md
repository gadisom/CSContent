---
category: ios
title: iOS 단어장
---

# iOS 단어장

## App Lifecycle
- answer: 앱이 실행, 활성화, 백그라운드, 종료 상태로 이동하는 흐름
- detail: 앱 생명주기는 사용자의 실행, 홈 이동, 시스템 자원 상황에 따라 변한다. 각 상태에 맞춰 저장, 복원, 네트워크 작업을 관리한다.

## Foreground
- answer: 앱이 화면에 보이고 사용자와 상호작용할 수 있는 상태
- detail: 포그라운드에서는 UI 업데이트와 사용자 입력 처리가 가능하다. 활성 상태인지 비활성 상태인지에 따라 세부 동작이 달라질 수 있다.

## Background
- answer: 앱이 화면에는 보이지 않지만 제한적으로 작업할 수 있는 상태
- detail: 백그라운드에서는 실행 시간이 제한된다. 위치, 오디오, 백그라운드 작업처럼 허용된 작업만 계속될 수 있다.

## Suspended
- answer: 앱이 메모리에 남아 있지만 코드는 실행되지 않는 상태
- detail: Suspended 상태의 앱은 빠르게 복귀할 수 있다. 시스템 메모리가 부족하면 예고 없이 종료될 수 있다.

## Optional
- answer: 값이 있을 수도 없을 수도 있음을 표현하는 Swift 타입
- detail: Optional은 nil 가능성을 타입에 드러내 안전한 처리를 강제한다. 값이 있으면 some, 없으면 none 상태로 볼 수 있다.

## Optional Binding
- answer: Optional 값을 안전하게 꺼내 상수나 변수로 사용하는 방식
- detail: if let과 guard let이 대표적이다. 값이 있을 때만 실제 값을 사용할 수 있게 해 강제 언래핑을 줄인다.

## Optional Chaining
- answer: Optional이 nil이면 뒤의 접근을 중단하고 nil을 반환하는 방식
- detail: 여러 단계의 프로퍼티나 메서드 접근에서 중간 값이 없을 수 있을 때 사용한다. 실패해도 크래시 대신 nil 결과를 얻는다.

## Nil-Coalescing
- answer: Optional이 nil일 때 사용할 기본값을 정하는 연산
- detail: ?? 연산자를 사용한다. Optional 값이 있으면 그 값을 쓰고, 없으면 오른쪽 기본값을 사용한다.

## Force Unwrapping
- answer: Optional에 값이 있다고 가정하고 강제로 꺼내는 방식
- detail: ! 연산자를 사용하며 값이 nil이면 런타임 크래시가 발생한다. 값이 확실한 경우가 아니라면 피하는 것이 좋다.

## IUO
- answer: 사용할 때 자동으로 언래핑되는 Optional
- detail: Implicitly Unwrapped Optional의 줄임말이다. UIKit IBOutlet처럼 초기 연결 뒤에는 값이 있다고 가정하는 경우에 자주 보인다.

## Value Type
- answer: 할당이나 전달 시 독립된 값처럼 다뤄지는 타입
- detail: Swift의 struct, enum, 기본 컬렉션이 대표적이다. 의도치 않은 공유 변경을 줄이고 데이터 흐름을 예측하기 좋다.

## Reference Type
- answer: 여러 변수가 같은 인스턴스를 함께 가리킬 수 있는 타입
- detail: Swift의 class가 대표적이다. 공유 상태와 식별성이 필요할 때 유용하지만 메모리 관리와 동시성에 주의해야 한다.

## Value Semantics
- answer: 값이 같으면 같은 의미로 다뤄지고 변경이 다른 값에 영향을 주지 않는 성질
- detail: 값 타입이 항상 완전한 Value Semantics를 보장하는 것은 아니다. 내부에 참조 타입을 저장하면 공유 상태가 생길 수 있다.

## Reference Semantics
- answer: 객체의 값뿐 아니라 같은 객체인지와 생명주기가 중요한 성질
- detail: class 인스턴스는 여러 참조가 같은 객체를 가리킬 수 있다. 동일성, 공유 상태, ARC 관리와 연결된다.

## struct
- answer: Swift에서 값 타입을 정의할 때 주로 사용하는 타입 선언
- detail: struct 인스턴스는 값처럼 복사되어 다뤄진다. SwiftUI View도 주로 struct로 선언된다.

## class
- answer: Swift에서 참조 타입을 정의하는 타입 선언
- detail: class 인스턴스는 여러 참조가 같은 객체를 가리킬 수 있다. 상속, 동일성 비교, ARC 메모리 관리와 관련된다.

## Copy-on-Write
- answer: 실제 변경 전까지 값 타입 내부 저장소 복사를 미루는 최적화
- detail: Array와 Dictionary 같은 Swift 컬렉션은 값 타입이지만 불필요한 전체 복사를 줄이기 위해 Copy-on-Write를 사용한다.

## Identity
- answer: 두 참조가 같은 객체 자체를 가리키는지 나타내는 성질
- detail: class 인스턴스는 값이 같아 보여도 서로 다른 객체일 수 있다. Swift에서는 === 연산자로 동일성을 비교한다.

## Equality
- answer: 두 값이 의미상 같은지 비교하는 성질
- detail: Swift에서는 보통 Equatable의 == 연산자로 표현한다. Identity가 같은 객체인지 보는 것이라면 Equality는 값의 동등성을 본다.

## Combine
- answer: 시간에 따라 발생하는 값의 흐름을 선언적으로 처리하는 프레임워크
- detail: Combine은 Publisher와 Subscriber를 연결해 비동기 이벤트를 처리한다. 네트워크 응답, 사용자 입력, 상태 변화 등을 스트림처럼 다룰 수 있다.

## Publisher
- answer: 값이나 완료 이벤트를 내보내는 Combine 구성 요소
- detail: Publisher는 Subscriber에게 값을 전달한다. 비동기 작업의 결과나 연속적인 이벤트를 표현하는 데 사용된다.

## Subscriber
- answer: Publisher가 내보낸 값을 받아 처리하는 Combine 구성 요소
- detail: Subscriber는 값을 얼마나 받을지 요청하고, 전달된 값과 완료 이벤트를 처리한다.

## Subscription
- answer: Publisher와 Subscriber 사이의 연결과 수요를 관리하는 객체
- detail: Subscription은 데이터 흐름을 시작하거나 취소하는 역할을 한다. Combine의 backpressure 처리와도 관련된다.

## Operator
- answer: Publisher의 값을 변환하거나 조합하는 Combine 연산
- detail: map, filter, debounce, merge 같은 연산자가 있다. 여러 비동기 흐름을 읽기 쉬운 파이프라인으로 만들 수 있다.

## AnyCancellable
- answer: Combine 구독을 취소할 수 있게 보관하는 타입
- detail: AnyCancellable이 해제되면 연결된 구독도 취소된다. 보통 프로퍼티에 저장해 구독 생명주기를 관리한다.

## Main Thread
- answer: iOS에서 UI 작업을 처리해야 하는 주 실행 흐름
- detail: UIKit과 SwiftUI의 UI 변경은 메인 스레드에서 수행해야 한다. 비동기 작업 결과를 화면에 반영할 때 메인 스레드 전환이 필요하다.

## RunLoop
- answer: 입력 이벤트와 타이머 같은 작업을 반복적으로 처리하는 이벤트 루프
- detail: RunLoop는 스레드가 이벤트를 기다리고 처리하도록 돕는다. 타이머나 특정 스케줄링 동작과 관련해 자주 등장한다.
