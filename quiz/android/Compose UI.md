---
category: android
tag: Compose
---

#### OX | [613]
remember로 저장된 state는 화면 회전 같은 configuration change에서도 유지된다.
> X
> remember는 Composition 내에서만 유지된다. configuration change 시 activity가 재생성되어 초기값으로 리셋된다. 유지하려면 rememberSaveable을 사용해야 한다.

#### OX | [614]
stateless composable은 state hoisting을 통해 구현할 수 있다.
> O
> state hoisting은 composable의 state를 상위 호출자로 올리는 패턴이다. 이를 통해 composable 자체는 state를 보유하지 않는 stateless 구조가 된다.

#### 빈칸 | [615]
Compose에서 configuration change에서도 state를 유지하려면 ___ 를 사용한다.
> rememberSaveable
> rememberSaveable은 saved instance state 메커니즘을 사용해 activity/process 재생성에서도 state를 보존한다. 단, 사용자가 직접 앱을 종료하면 유지되지 않는다.

#### 빈칸 | [616]
input이 recomposition 필요 빈도보다 자주 변경될 때 불필요한 recomposition을 방지하는 API는 ___ 이다.
> derivedStateOf
> derivedStateOf는 결과값이 실제로 변경된 경우에만 recomposition을 트리거한다. 단, 자체 비용이 크므로 실제로 불필요한 recomposition이 있을 때만 사용한다.

#### 객관식 | [617]
remember와 rememberSaveable의 차이로 올바른 것은?
1. remember는 비동기, rememberSaveable은 동기로 동작한다
2. ✅ remember는 configuration change 시 state를 잃지만, rememberSaveable은 saved instance state로 유지한다
3. 둘은 동일하며 rememberSaveable이 remember를 완전히 대체한다
4. rememberSaveable은 사용자가 앱을 직접 종료해도 state를 유지한다
> rememberSaveable은 activity/process 재생성(화면 회전 등)에서 state를 유지하지만, 사용자가 직접 앱을 dismiss한 경우에는 유지하지 않는다.

#### 객관식 | [618]
derivedStateOf 사용에 대한 설명으로 올바른 것은?
1. state가 변경될 때마다 사용하는 기본 API다
2. 비용이 없으므로 자유롭게 사용할 수 있다
3. ✅ input이 recomposition 필요 빈도보다 자주 변경될 때만 사용해야 하며, 자체가 비용이 큰 연산이다
4. remember와 동일한 기능을 한다
> derivedStateOf 자체가 비용이 큰 연산이므로 불필요한 recomposition이 실제로 발생하는 경우에만 사용해야 한다. 남용하면 오히려 오버헤드가 증가한다.
