> [Optional은 값의 존재 여부를 타입으로 드러내 nil을 안전하게 다루게 하는 Swift의 핵심 문법이다.]{.lead}

## 정의
- [Optional]{.term}은 값이 있을 수도 있고 없을 수도 있음을 표현하는 Swift 타입이다.
- `String`과 `String?`는 다른 타입이며, `String?`만 `nil`을 가질 수 있다.
- Optional은 개념적으로 값이 있는 [some]{.term} 상태와 값이 없는 [none]{.term} 상태를 가진다.
- `nil`은 값이 없다는 상태이며 Optional의 none에 해당한다.
- [Unwrapping]{.term}은 Optional 안에 값이 있는지 확인하고 실제 값을 꺼내는 과정이다.
- [Implicitly Unwrapped Optional]{.term}은 `String!`처럼 사용할 때 자동으로 꺼내지는 Optional이다.

## 핵심 포인트
- [nil 가능성을 타입에 드러내면 컴파일 단계에서 누락 처리를 발견하기 쉽다.]{.accent}
- `if let`은 특정 분기 안에서 값을 안전하게 사용하고, `guard let`은 값이 없을 때 빠르게 흐름을 종료한다.
- [Optional Chaining]{.term}은 중간 값이 `nil`이면 전체 결과를 `nil`로 돌려준다.
- [Nil-Coalescing]{.term} `??`는 값이 없을 때 사용할 기본값을 지정한다.
- [Force Unwrapping]{.danger} `!`은 값이 없으면 런타임 크래시가 발생한다.
- UIKit의 `@IBOutlet weak var label: UILabel!`는 스토리보드 연결 이후 값이 있다고 가정하는 IUO 패턴이다.
- `weak` 참조는 대상이 해제되면 `nil`로 바뀔 수 있으므로 보통 Optional로 선언된다.
- 실패 이유가 필요 없고 값 유무만 중요하면 Optional 반환, 실패 원인을 전달해야 하면 `throw`가 더 적합하다.

## 면접 질문
- Swift에서 Optional이 필요한 이유는 무엇인가요?
- `String`, `String?`, `String!`의 차이를 설명해보세요.
- Optional Binding과 Optional Chaining은 어떤 상황에서 사용하나요?
- `if let`과 `guard let`은 흐름 제어 관점에서 어떻게 다른가요?
- Force Unwrapping이 위험한 이유는 무엇인가요?
- UIKit에서 IBOutlet이 IUO로 선언되는 경우가 많은 이유는 무엇인가요?
- Optional 반환과 `throw`는 각각 어떤 상황에 어울리나요?

## 확인 문제
- 일반 `String` 타입은 `nil`을 가질 수 있을까?
- Optional 값은 사용 전에 안전하게 꺼내는 과정이 필요할까?
- `guard let`은 값이 없을 때 early return 흐름을 만들기 좋을까?
- Force Unwrapping은 값이 없으면 런타임 크래시가 날 수 있을까?
- `weak` 참조는 대상이 해제되면 `nil`이 될 수 있을까?

## 키워드
Swift, Optional, nil, Optional Binding, Optional Chaining, Nil-Coalescing, Force Unwrapping, IUO, weak, IBOutlet

## 연관 콘텐츠
- [[앱 생명주기]]
- [[Combine]]
