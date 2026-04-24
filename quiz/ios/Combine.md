---
category: ios
tag: Combine
---

#### OX | [607]
catch 연산자는 에러 발생 후에도 원래 Publisher와의 스트림 연결을 유지한다.
> X
> catch는 에러 발생 시 기존 Publisher를 Recovery Publisher로 교체해 원본 스트림이 끊긴다. 스트림 유지가 필요하면 flatMap+catch를 사용한다.

#### OX | [608]
AnyCancellable 객체가 메모리에서 해제되면 구독이 자동으로 취소된다.
> O
> AnyCancellable은 deinit 시 자동으로 cancel()을 호출한다. 명시적으로 cancel()을 호출하지 않아도 scope를 벗어나면 구독이 종료된다.

#### 빈칸 | [609]
Combine에서 에러 처리 시 upstream 스트림을 유지하려면 ___ 와 catch를 함께 사용한다.
> flatMap
> catch만 사용하면 에러 발생 시 upstream과의 연결이 끊긴다. flatMap 안에서 catch를 감싸면 내부에서만 에러를 처리하고 upstream은 계속 유지된다.

#### 빈칸 | [610]
Combine에서 Publisher와 Subscriber 역할을 동시에 수행하는 타입은 ___ 이다.
> Subject
> Subject는 upstream을 구독하면서 downstream Subscriber에게 값을 전달할 수 있다. PassthroughSubject와 CurrentValueSubject 두 종류가 있다.

#### 객관식 | [611]
map과 tryMap의 차이로 올바른 것은?
1. ✅ map은 에러를 발생시키지 않아 Failure가 Never 유지, tryMap은 throw된 에러를 Failure 타입으로 변환한다
2. map은 비동기, tryMap은 동기로 동작한다
3. map은 값을 변환하고 tryMap은 필터링만 한다
4. 둘은 동일한 연산자다
> map의 Failure 타입은 upstream과 동일하게 유지된다. tryMap은 클로저 내에서 throw를 허용하고 에러를 Failure로 변환해 스트림에 흘려보낸다.

#### 객관식 | [612]
PassthroughSubject와 CurrentValueSubject의 차이로 올바른 것은?
1. PassthroughSubject는 에러를 처리하고 CurrentValueSubject는 처리할 수 없다
2. ✅ CurrentValueSubject는 마지막 값을 저장해 새 구독자도 즉시 받을 수 있고, PassthroughSubject는 구독 이후 값만 받는다
3. PassthroughSubject는 멀티캐스트, CurrentValueSubject는 유니캐스트다
4. 둘은 기능이 동일하다
> PassthroughSubject는 구독 시점 이후 방출된 값만 수신한다. CurrentValueSubject는 초기값을 가지며 새 구독자에게 즉시 마지막 값을 전달한다.
