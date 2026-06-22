> [Android IPC]{.lead}는 프로세스 간 통신을 위해 [Binder]{.term} 드라이버를 기반으로 동작하며, [AIDL]{.term}·[Messenger]{.term}·[Intent]{.term}·[ContentProvider]{.term} 등 다양한 메커니즘을 제공한다.

## 정의
- [IPC(Inter-Process Communication)]{.term}: 서로 다른 프로세스 간에 데이터를 교환하고 동작을 조율하는 메커니즘. Android에서는 각 앱이 독립된 프로세스로 실행되어 기본적으로 메모리를 공유하지 않는다
- [Binder]{.term}: Android IPC의 핵심 드라이버(`/dev/binder`). 커널 레벨에서 동작하며 프로세스 간 메모리를 복사 없이 한 번만 전달하는 zero-copy에 가까운 구조를 사용한다
- [AIDL(Android Interface Definition Language)]{.term}: 서로 다른 프로세스에서 인터페이스를 공유하기 위한 IDL. 컴파일 시 Binder 통신을 위한 Stub/Proxy 코드가 자동 생성된다
- [Messenger]{.term}: AIDL 없이 단일 스레드 기반의 단방향 IPC를 제공하는 클래스. 내부적으로 Binder와 Handler를 사용한다
- [Intent]{.term}: 앱 컴포넌트(Activity, Service, BroadcastReceiver) 간 데이터와 동작 요청을 전달하는 메시지 객체. 같은 프로세스와 다른 프로세스 모두에 사용 가능하다
- [ContentProvider]{.term}: 구조화된 데이터(주로 DB)를 다른 앱에 안전하게 공유하는 컴포넌트. URI 기반으로 CRUD 동작을 제공한다
- [Bundle]{.term}: Intent나 Binder 통신에서 key-value 쌍으로 데이터를 직렬화해 전달하는 컨테이너

## 핵심 포인트
- [Binder는 단 한 번의 메모리 복사]{.accent}로 IPC를 수행한다. 전통적인 Unix 소켓·파이프(2회 복사)보다 효율적이며, Android 시스템 서비스(AMS, WMS 등)도 모두 Binder로 통신한다
- [AIDL은 멀티스레드 동시 호출을 허용]{.accent}하므로 서비스 측 구현을 스레드 안전하게 작성해야 한다. Messenger는 단일 스레드(Handler) 기반이므로 상대적으로 간단하지만 병렬 처리가 불가능하다
- Intent는 직렬화(Parcelable / Serializable) 가능한 데이터만 전달할 수 있으며, 1MB 미만의 데이터에 적합하다. [TransactionTooLargeException]{.warning}은 Binder 버퍼(1MB)를 초과할 때 발생한다
- ContentProvider는 [권한(Permission) 기반 접근 제어]{.accent}를 제공한다. `android:exported`, `readPermission`, `writePermission`으로 외부 앱의 접근을 제한할 수 있다
- [Bound Service]{.term}는 AIDL 또는 Messenger를 통해 클라이언트와 양방향 통신을 구현할 때 사용한다. `onBind()`에서 IBinder를 반환해 연결한다
- [BroadcastReceiver]{.term}는 시스템 또는 앱이 발행하는 이벤트를 수신하는 단방향 IPC다. Android 8.0(Oreo) 이후 암시적 브로드캐스트는 대부분 제한되어 명시적 브로드캐스트나 LocalBroadcastManager(프로세스 내)를 권장한다

## 면접 질문
- Android에서 IPC가 필요한 상황을 예를 들어 설명해보세요
- Binder가 기존 Unix IPC(소켓, 파이프)보다 Android에 적합한 이유는 무엇인가요?
- AIDL과 Messenger의 차이점과 각각의 적합한 사용 시나리오를 설명해보세요
- TransactionTooLargeException이 발생하는 원인과 해결 방법은 무엇인가요?
- ContentProvider를 통해 다른 앱과 데이터를 공유할 때 보안을 어떻게 제어하나요?

## 확인 문제
- Android IPC의 핵심 메커니즘인 Binder 드라이버가 위치하는 계층은 어디인가요?
- AIDL을 사용할 때 서비스 측 구현에서 스레드 안전성이 필요한 이유는 무엇인가요?
- Intent로 데이터를 전달할 때 사용하는 직렬화 인터페이스 두 가지를 말해보세요
- Binder 트랜잭션 버퍼의 크기 제한은 얼마이며, 초과 시 발생하는 예외는 무엇인가요?

## 키워드
IPC, Binder, AIDL, Messenger, Intent, ContentProvider, BroadcastReceiver, Bound Service, Bundle, Parcelable, IBinder, Stub, Proxy, TransactionTooLargeException

## 연관 콘텐츠
- [[IPC와 동기화]]
- [[Compose UI]]
