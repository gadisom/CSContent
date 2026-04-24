> remember는 recomposition 간 state를 유지하고, rememberSaveable은 configuration change에서도 유지한다. derivedStateOf로 불필요한 recomposition을 줄일 수 있다.

## 정의
- remember: Composable이 initial composition에서 값을 저장하고 recomposition 시 반환하는 API. Composition에서 제거되면 값도 잊힌다.
- rememberSaveable: saved instance state 메커니즘으로 activity/process 재생성(configuration change)에서도 state를 유지한다. 사용자가 직접 종료하면 유지되지 않는다.
- mutableStateOf: Compose Snapshot 시스템에 통합된 Observable MutableState<T>. value가 변경되면 해당 값을 읽는 모든 composable의 recomposition이 스케줄된다.
- stateful/stateless composable: internal state를 가지면 stateful. stateless는 재사용성과 테스트 용이성이 높으며, state hoisting으로 구현한다.
- derivedStateOf: input이 recomposition 필요 빈도보다 자주 변경될 때 불필요한 recomposition을 방지하는 함수. 자체가 비용이 크므로 꼭 필요한 경우에만 사용한다.

## 핵심 포인트
- remember의 key 파라미터가 변경되면 캐시를 무효화하고 calculation lambda를 재실행한다.
- configuration change(화면 회전 등) 시 remember는 초기화되지만 rememberSaveable은 유지된다.
- mutableStateOf 선언은 val, var(by delegate), destructuring 세 방식이 동일하다. by를 쓰려면 getValue/setValue import가 필요하다.
- stateful composable은 재사용성이 낮다. state hoisting으로 state를 상위로 올려 stateless composable을 설계하는 것이 권장된다.
- derivedStateOf는 결과가 변경되지 않는 한 불필요한 recomposition을 막는다. 단, 남용하면 오히려 오버헤드가 생긴다.

## 면접 질문
- remember와 rememberSaveable의 차이는 무엇인가요?
- stateful composable과 stateless composable의 차이와 state hoisting의 목적은?
- derivedStateOf는 어떤 상황에서 사용하나요?

## 확인 문제
- 화면 회전 시 remember로 저장된 값이 유지되나요?
- remember의 key 파라미터가 변경되면 어떤 일이 발생하나요?
- state hoisting이 없는 stateful composable의 단점은 무엇인가요?

## 키워드
Compose, remember, rememberSaveable, mutableStateOf, State Hoisting, derivedStateOf, recomposition, Stateful, Stateless, Snapshot

## 연관 콘텐츠
