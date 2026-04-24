> Publisher가 이벤트를 방출하고 Operator로 변환하며 Subscriber가 소비한다. catch는 스트림을 끊고, flatMap+catch는 스트림을 유지하면서 에러를 처리한다.

## 정의
- Publisher: Output과 Failure 두 associated type을 가진 이벤트 방출 타입. map/decode 등 Operator로 변환 가능하다.
- Subscriber: subscription → value(0개 이상) → completion(최대 1회) 순서로 이벤트를 수신하는 타입
- Operator: Publisher 출력을 변환·조합하는 연산자. map은 Failure가 Never 유지, tryMap은 에러를 Failure로 변환한다.
- Subject: Publisher와 Subscriber 역할을 동시에 수행. PassthroughSubject(구독 이후 값만), CurrentValueSubject(마지막 값 저장) 두 종류가 있다.
- AnyCancellable: 구독을 감싸는 타입. deinit 시 자동으로 cancel()을 호출해 ARC 기반 구독 관리를 지원한다.

## 핵심 포인트
- catch는 에러 발생 시 기존 Publisher를 Recovery Publisher로 교체해 원본 스트림이 끊긴다.
- flatMap + catch 조합은 에러를 처리하면서 upstream과의 연결을 유지한다.
- receive(on:)으로 이벤트 전달 스레드를 지정한다. UI 업데이트는 반드시 RunLoop.main 또는 DispatchQueue.main으로 받아야 한다.
- @Published + ObservableObject 채택만으로 SwiftUI 데이터 바인딩이 완성된다. didSet+PassthroughSubject 방식을 대체한다.
- Subscriber 순서 규칙: subscription 1회 → value 0개 이상 → completion 최대 1회. 완료 이후에는 값을 방출할 수 없다.

## 면접 질문
- catch와 flatMap+catch의 동작 차이를 설명해보세요.
- PassthroughSubject와 CurrentValueSubject는 언제 각각 사용하나요?
- @Published가 내부적으로 Combine과 어떻게 연결되나요?

## 확인 문제
- map과 tryMap의 Failure 타입 차이는 무엇인가요?
- AnyCancellable을 저장하지 않으면 구독에 어떤 일이 생기나요?
- receive(on:) 없이 백그라운드 Publisher 결과를 UI에 바인딩하면 어떤 문제가 생기나요?

## 키워드
Combine, Publisher, Subscriber, Operator, AnyCancellable, Subject, PassthroughSubject, CurrentValueSubject, flatMap, catch, ObservableObject

## 연관 콘텐츠
- [[앱 생명주기]]
