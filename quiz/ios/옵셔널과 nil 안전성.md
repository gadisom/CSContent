---
category: ios
tag: Optional
---

#### OX | [724]
Swift에서 `String`과 `String?`는 같은 타입이다.
> X
> `String`은 nil을 가질 수 없고, `String?`는 값이 없을 가능성을 타입에 포함한 Optional 타입입니다.

#### OX | [725]
Force Unwrapping은 Optional 값이 nil이면 런타임 크래시를 발생시킬 수 있다.
> O
> `!`는 값이 있다고 강하게 가정하고 꺼내는 방식이므로 nil이면 앱이 크래시될 수 있습니다.

#### 객관식 | [726]
`if let`과 `guard let`의 차이로 가장 알맞은 것은?
1. `if let`은 nil일 때 앱을 종료한다
2. `guard let`은 Optional을 자동으로 강제 언래핑한다
3. ✅ `guard let`은 값이 없을 때 early return 흐름을 만들기 좋다
4. 둘은 문법만 다르고 흐름 차이는 없다
> `if let`은 특정 분기 안에서 값을 쓰기 좋고, `guard let`은 실패 조건을 먼저 빠져나가 정상 흐름을 평평하게 만들기 좋습니다.

#### 객관식 | [727]
`String!`처럼 선언하는 IUO에 대한 설명으로 가장 알맞은 것은?
1. 절대 nil이 될 수 없는 일반 String이다
2. ✅ 사용할 때 자동으로 언래핑되지만 nil이면 크래시가 날 수 있다
3. Optional Chaining과 완전히 같은 의미다
4. 컴파일러가 항상 nil 여부를 보장한다
> IUO는 초기화 시점에는 nil일 수 있지만 사용 시점에는 값이 있다고 가정하는 Optional입니다.

#### OX | [728]
`weak` 참조는 대상 객체가 해제되면 nil이 될 수 있으므로 보통 Optional로 선언된다.
> O
> weak 참조는 참조 대상이 사라졌을 때 자동으로 nil이 될 수 있어 Optional과 함께 쓰이는 경우가 많습니다.
