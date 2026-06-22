---
category: android
tag: IPC
---

#### OX | [742]
Android IPC의 핵심 기반에는 Binder가 있다.
> O
> Binder는 Android에서 프로세스 간 메서드 호출과 데이터 전달을 가능하게 하는 핵심 IPC 메커니즘입니다.

#### OX | [743]
AIDL은 같은 프로세스 내부의 일반 함수 호출만 표현하기 위해 사용하는 도구다.
> X
> AIDL은 Android Interface Definition Language로, 서로 다른 프로세스 사이에서 호출할 인터페이스를 정의할 때 사용합니다.

#### 빈칸 | [744]
Android에서 Binder를 통해 객체 데이터를 전달할 때 자주 사용하는 직렬화 인터페이스는 ___이다.
> Parcelable
> Parcelable은 Android IPC와 Bundle 전달에 맞춰 객체를 효율적으로 직렬화하기 위한 인터페이스입니다.

#### 빈칸 | [745]
앱 간 구조화된 데이터를 URI 기반으로 공유할 수 있게 하는 Android 컴포넌트는 ___이다.
> ContentProvider
> ContentProvider는 다른 앱이 정해진 URI와 권한을 통해 데이터를 조회하거나 변경할 수 있게 합니다.

#### 객관식 | [746]
Binder에 대한 설명으로 가장 알맞은 것은?
1. 화면 배치를 계산하는 UI 엔진이다
2. SQLite 테이블을 자동으로 생성하는 ORM이다
3. ✅ 프로세스 간 호출과 데이터 전달을 지원하는 Android IPC 기반이다
4. 이미지 압축 포맷이다
> Binder는 앱 프로세스와 시스템 서비스, 또는 앱 간 통신에서 사용되는 Android의 핵심 IPC 기반입니다.

#### 객관식 | [747]
Messenger와 AIDL의 차이로 가장 알맞은 것은?
1. Messenger는 IPC가 아니고 AIDL만 IPC다
2. ✅ Messenger는 Message 기반 단순 통신에 적합하고, AIDL은 타입이 정해진 원격 인터페이스 호출에 적합하다
3. AIDL은 ContentProvider에서만 사용할 수 있다
4. Messenger는 항상 여러 요청을 동시에 병렬 처리한다
> Messenger는 Handler를 통해 Message를 주고받는 단순 IPC에 적합하고, AIDL은 명시적인 메서드 인터페이스가 필요할 때 사용합니다.

#### OX | [748]
Intent extras나 Bundle은 Binder를 거치더라도 크기 제한 없이 큰 데이터를 자유롭게 전달할 수 있다.
> X
> Binder transaction에는 크기 제약이 있으므로 큰 이미지나 대용량 데이터는 파일, URI, 저장소 참조 등으로 전달하는 편이 안전합니다.

#### 객관식 | [749]
PendingIntent의 역할로 가장 알맞은 것은?
1. 앱의 모든 스레드를 중지한다
2. ✅ 다른 앱이나 시스템이 나중에 내 앱의 권한으로 정해진 Intent를 실행할 수 있게 한다
3. ContentProvider의 SQL을 자동 최적화한다
4. Binder transaction 크기를 늘린다
> PendingIntent는 알림, 알람 등에서 시스템이나 다른 앱이 나중에 미리 정의된 작업을 실행하도록 위임할 때 사용합니다.

#### OX | [750]
Binder를 통한 원격 호출은 오래 걸릴 수 있으므로 무거운 작업을 메인 스레드에서 직접 처리하지 않도록 주의해야 한다.
> O
> IPC 호출은 상대 프로세스의 처리와 스레드 상황에 영향을 받을 수 있으므로 UI 멈춤을 피하려면 비동기 처리와 스레드 관리가 중요합니다.
