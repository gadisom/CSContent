---
title: "Combine 연습해보기-(WWDC)"
source: "https://medium.com/@jeongwon.kim64/combine-%EC%97%B0%EC%8A%B5%ED%95%B4%EB%B3%B4%EA%B8%B0-wwdc-38f6634a3830"
author:
  - "[[Garden]]"
published: 2025-01-09
created: 2026-04-24
description: "More"
tags:
  - "clippings"
---
## [WWDC 로 보는 Combine](https://medium.com/@jeongwon.kim64/wwdc-%EB%A1%9C-%EB%B3%B4%EB%8A%94-combine-8c6008723ce3?source=post_page-----38f6634a3830---------------------------------------)

### 기존의 비동기 처리방식(Notification, Center, KVO, URLSession..) 이 혼합되어 사용하다 보니 비동기 처리 방식이 난잡해졌다 -> 통합적인 코드 필요

medium.com

앞서 Combine 을 소개하는 WWDC를 보면서 Combine 의 동작 원리에 대해서 알아보았다. 이번 포스팅에서는 WWDC 의 Combine Practice 부분을 다루도록 하겠다.

> 연습의 예시는 마법학교와 관련된 앱인데, 어떠한 마술 트릭을 다운로드 하는 기능을 Combine 을 통해서 구현하려 한다.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TdNjOCKYsFvroHwb6jVT0g.png)

```c
let trickNamePublisher = NotificationCenter.default.publisher(for: .newTrickDownloaded)

// Notification - Output
// Never -Failure
```
1. trickNamePublisher 는 Notification 이라는 Output과 Failure 를 방출한다.
2. 알림 Publisher 가 활성화 되었지만 정말 원하는 것은?? -> 마술 트릭에 있는 내용
```c
let trickNamePublisher = NotificationCenter.default.publisher(for: .newTrickDownloaded)
  .map { notification in
   return notification.userInfo?["data"] as! Data
  }
```

Combine 은 맵 함수를 제공해 알림을 내부로 가져와 필요한 양식으로 변환할 수 있다.

기존의 Swift map 방식과 매우 유사하다. 이때 Combine 의 map 변환 과정에서 에러를 발생시키지 않는다. 따라서 Failure 타입은 항상 Never 로 유지된다.

```c
let trickNamePublisher = NotificationCenter.default.publisher(for: .newTrickDownloaded)
  .map { notification in
    return notification.userInfo?["data"] as! Data
  }
  .tryMap { data in
    let decoder = JSONDecoder()
    try decoder.decode(MagicTrick.self, from: data)
   }
  //MagicTrick
  //Error
```

Json 파일을 디코딩 하는 tryMap 이다. 이는 map 과 동일하지만 스트림에서 발생한 모든 오류를 실패로 변환하는 기능을 추가한다. 이 과정에서 출력값이 디코딩 된 MagicTrick 이나 Error가 반환된다.

데이터를 디코딩 하는 작업은 매우 흔한 작업이라 이를 처리하는 Operator 가 존재한다. 다음과 같이 바꿔 사용할 수 있다.

```c
let trickNamePublisher = NotificationCenter.default.publisher(for: .newTrickDownloaded)
  .map { notification in
   return notification.userInfo?["data"] as! Data
   }
  .decode(MagicTrick.self, JSONDecoder())
```

## Error Handling

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*w7L0z-D1PVTKp-83YxC7gQ.png)

지금까지 실패의 반환 타입은 Never 만 보냈지만, 실제 실패할 경우를 대비해서 에러를 처리해야한다. Combine 에서는 잠재적 실패에 대응하는 것이 매우 중요하다.

```c
let trickNamePublisher = NotificationCenter.default.publisher(for: .newTrickDownloaded)
  .map { notification in
   return notification.userInfo?["data"] as! Data
  }
  .decode(MagicTrick.self, JSONDecoder())
  .assertNoFailure()
  // MagicTrick 
  // Never
```

.assertNoFailure() 연산자를 사용해 기존 실패 타입이 Never 로 바뀌었다.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*84BtR3tdZnyZ4hA_eXIKKw.png)

오류가 있는 경우에 다음과 같이 FatalError 가 발생하며 앱이 종료된다. 따라서 assertNoFailure() 는 디버깅, 절대 에러가 날 수 없는 환경에서만 사용해야 한다. 그럼 에러를 처리 하는 방법이 assertNoFailure() 밖에 없는걸까??

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YEFmKPNPebH4lnOtjuJlyg.png)

다행히도 에러를 처리하는 다양한 연산자가 있다. 이때 가장 유용한 연산자는 catch 이다.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7BnaOLdXZwcb4TyyA5uvaA.png)

에러를 받았다.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*m7UjQYqm-L01Uo90mcxndQ.png)

catch 는 오류를 받아오면 기존에 받아온 Publisher 를 지우고 Recovery 클로저를 호출하여 에러를 대체할 수 있게 된다.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*i12Pk1NpuvNFWjCxi4gxgg.png)

새로운 Recovery Publisher 를 구독하면서 에러에 대체할 수 있다. 이를 코드로 표현하면

```c
let trickNamePublisher = NotificationCenter.default.publisher(for: .newTrickDownloaded)
  .map { notification in
   return notification.userInfo?["data"] as! Data
  }
  .decode(MagicTrick.self, JSONDecoder())
  .catch { Just(MagicTrick.placeholder) 
  }
 // MagicTrick
 // Never
```

Just 는 그냥 단일 값을 배출하는 Publisher 이다. 오류가 나면 MagicTrick.placeholder 를 단순배출 한다는 뜻!

### 정리

1. Publisher 로 시작 (알림)  
	\- NotificationCenter 를 통해 알림 이벤트를 수신하는 Publisher를 생성한다.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*7SkOPgy6pcMXnzjM6I0XYQ.png)

2\. 데이터 매핑

- Notification 을 원하는 데이터 형식으로 변환하기 위해 map 을 사용한다.
![](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*hMFiEdlkjo05_HOTeWL5zA.png)

3\. 디코딩

- 매핑된 데이터를 JSON과 같은 사용자 정의 타입으로 변환하기 위해 decode 연산자를 사용한다.
![](https://miro.medium.com/v2/resize:fit:1124/format:webp/1*HigUHqkICIDrDkIRTeHWxQ.png)

4\. 디코딩 Error Handling

- 디코딩 과정에서 에러가 발생할 가능성이 있으므로, 실패 상황을 대비해 placeholder 데이터를 준비한다.
- 에러 발생 시, 단순히 실패한 Publisher를 placeholder 로 대체하면 원래 데이터 스트림과의 연결이 끊어진다.
- 결과- 기존 Publisher 의 Notification 을 더 이상 받을 수 없다. -> 이를 보완하기 위해 flatMap 사용

## flatMap

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Fm2by04LCba7YdkAH8MLSQ.png)

- flatMap은 디코딩에 실패하더라도 원래의 upstream 과 연결을 유지하면서 placeholder 데이터를 사용할 수 있도록 처리한다.
- 디코딩을 시도한다.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0dgYiQsVImKIa0JqAizcIA.png)

- 실패 시, 준비된 placeholder데이터를 반환한다.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*r7JfAatmAKsm36iWPNSJAQ.png)

- 동시에 원래 Publisher 와의 연결을 계속 유지한다.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Hg1t-DQN5QhjVGBt2taOxQ.png)

1. map과 decode로 데이터를 변환한다.
2. 디코딩 실패 시, flatMap을 사용해 실패를 처리하면서도 원래 데이터 스트림(업스트림)과의 연결을 유지한다.
3. flatMap은 Combine에서 에러 처리와 데이터 스트림 유지에 적합한 연산자다.

따라서 해당 작업은 절대로 실패하지 않음을 보장할 수 있다.

```c
let trickNamePublisher = NotificationCenter.default.publisher(for: .newTrickDownloaded)
  .map { notification in
   return notification.userInfo?["data"] as! Data
  }
  .flatMap { data in
   return Just(data)
    .decode(MagicTrick.self, JSONDecoder())
    .catch {
     return Just(MagicTrick.placeholder)
    }
  }
  .publisher(for: \.name)
```
- catch는 Recover Publisher를 통해 실패를 복구하지만, **기존 스트림과의 연결은 끊어진다.**
- 원래 Publisher의 업데이트를 계속 수신하려면, 다시 연결을 명시적으로 설정해야 한다.
- 이 과정에서 publisher(for:)를 사용해 기존의 Publisher와 재연결한다.

## Scheduled Operators

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zaXWqrlUrrpWX53QnBVKNg.png)

- 특정 이벤트가 언제, 어디에서 전달 되는지 설명하는데 도움이 된다.
- RunLoop 나 DispatchQueue 에서 네이티브로 지원
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7dM5wm93ryCeJVaOdQRAOQ.png)

```c
let trickNamePublisher = NotificationCenter.default.publisher(for: .newTrickDownloaded)
  .map { notification in
   return notification.userInfo?["data"] as! Data
  }
  .flatMap { data in
   return Just(data)
  .decode(MagicTrick.self, JSONDecoder())
  .catch {
   return Just(MagicTrick.placeholder)
   }
  }
  .publisher(for: \.name)
  .receive(on: RunLoop.main)
```
- receive: 특정 스레드 또는 큐에 전달 되도록 보장
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SJFzeAnPEDVLNuY43Waoig.png)

flatMap 을 통해 새로운 Publisher 와 연결 → pulisher(for: ) 연산자를 통해 MagicTrick 내부로 들어가 MagicTrick name 을 추출 → recevie(on: ) 연산자를 통해 작업을 메인 스레드로 이동

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HNddrFMbqM2WTnUvDf_TSw.png)

Publisher 와 Operator 를 통하여 많은 작업을 수행했다.

Publisher 가 Just 처럼 동기적으로 값을 생성할 수 있고 NoticifationCenter 와 같이 비동기적으로도 값을 생성할 수 있는것을 확인했다. 이제 Subscriber 에 대해서 알아보자

## Subscriber

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*mPBPw4LySuHOhpCTfFgJvg.png)

Combine에서 Subscriber는 Input과 Failure 라는 두 가지 관련 타입을 가진다. 또한, subscription, value, completion 를 수신하기 위한 세 가지 주요 이벤트 함수가 있다. 이 함수들이 호출되는 순서는 다음 세 가지 규칙에 의해 정의된다.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*swCQvR2uthRnb9s6A4WD6A.png)

- receive(subscription: )
- Publisher는 구독 요청에 응답하여 정확히 한번 receive(subscription: )을 호출한다.
- 이 단계에서 Subscriber 는 데이터를 얼마나 받을 지 요청할 수 있다.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*VC1YuZzo_SJ9PR8uQ3zA0w.png)

- Publisher는 Subscriber가 요청한 데이터의 양만큼 **0개 이상의 값** 을 receive(\_:)를 통해 전달한다.
- 이 값들은 다운스트림으로 전달되며, 요청한 데이터 양보다 적게 전달될 수도 있다.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*BPIRLjQZaTGkhyME4t5Qdg.png)

- Publisher는 데이터 전송을 종료하기 위해 최대 **한 번의 완료(completion)** 이벤트를 보낸다.
- 완료 이벤트는 두 가지 중 하나로 표시된다:  
	.finished: 정상적으로 데이터 전송 완료.  
	.failure(Error): 오류로 인해 데이터 스트림 종료.
- 완료 이벤트가 발생한 이후에는 더 이상 데이터를 방출할 수 없다.

### 요약

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bkr52iRn-YGerm6elEbLcQ.png)

1. Subscriber는 하나의 구독(subscription)을 받는다.
2. 이후, 0개 이상의 값(value)을 받을 수 있다.
3. 마지막으로, **최대 하나의 완료(completion)** 이벤트로 종료된다.

### Kinds of Subscribers

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*h-5ylKhzxFPRKFiErWD79Q.png)

```c
let trickNamePublisher = NotificationCenter.default.publisher(for: .newTrickDownloaded)
  .map { notification in
   return notification.userInfo?["data"] as! Data
  }
  .flatMap { data in
     return Just(data)
    .decode(MagicTrick.self, JSONDecoder())
    .catch   {
       return Just(MagicTrick.placeholder)
     }
  }
  .publisher(for: \.name)
  .receive(on: RunLoop.main)
  
let canceller = trickNamePublisher.assign(to: \.someProperty, on: someObject)

canceller.cancel()
```
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*pKuFnZH5NRB02modulsy3Q.png)

## Cancellation

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*WsqQnWd9N47XzlIC-mV8KQ.png)

Combine에서는 구독을 관리하고 취소할 수 있는 AnyCancellable 이라는 편리한 도구를 제공한다.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*q7xBpIDzcXATjHZR88QPHg.png)

AnyCancellable의 장점

1. 자동 구독 취소  
	\- AnyCancellable 객체가 deinit 될 시 자동으로.cancel() 를 호출한다.  
	\- 별도로 구독을 명시적으로 취소하지 않아도, scope 를 벗어나거나 메모리에서 해제되면 구독이 종료된다.
2. Swift 메모리 관리 활용  
	\- deinit 에서 자동 취소를 통해 ARC 기반 메모리 관리를 최대한 활용할 수 있다.  
	\- 명시적으로.cancel() 를 호출해야하는 부담이 줄어든다.

Sink

```c
let trickNamePublisher = ... // Publisher of <String, Never>
let canceller = trickNamePublisher.sink { trickName in 
  // Do Something with trickName
}
```
- sink 연산자는 클로저를 제공하면 모든 값에 대해 클로저가 호출되고 side effect 를 처리할 수 있다.
- sink 구독을 종료할 수 있는 취소 가능 항목을 반환한다.

Subjects

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sQU1wlOrfbx7r0_IvNEjbA.png)

- Publisher, Subscriber 의 특징을 모두 가지고 있는 연산자이다.
- 수신된 값을 Subscriber 에게 보낼 수 있고 명령형으로 보낼 수 있다.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*esgO8TVeczL9Ld_pfyY8oA.png)

위와 같이 하나의 subject 를 broadcast 형식으로 다중의 Subscriber 에게 보낼 수 있는 것

## Passthrough & CurrentValue

Subject 는 두가지 형식이 있다.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4-BGx0jzk5EYsk2SPYAJzA.png)

1. Passthrough: 값을 저장하지 않기 때문에 구독을 한 후에만 값을 볼 수 있다.
2. CurrentValue: 수신된 마지막 값을 기록하여 신규 Subscriber 도 값을 확인할 수 있다.
```c
let trickNamePublisher = ... // Publisher of <String, Never> 생략 

// Subject는 Publisher와 Subscriber의 역할을 모두 할 수 있다.
let magicWordsSubject = PassthroughSubject<String, Never>()

// Subject가 Subscriber처럼 작동하여 upstream Publisher를 구독한다.
trickNamePublisher.subscribe(magicWordsSubject)

// Subject는 Publisher처럼 작동하여 downstream Subscriber에게 값을 전달한다.
let canceller = magicWordsSubject.sink { value in
    // do something with the value  
} 
 
// Subject는 send를 사용해 명령형으로 값을 발행할 수 있다.
magicWordsSubject.send("Please")

// share 연산자를 사용하여 PassthroughSubject를 Stream에 주입.
let sharedTrickNamePublisher = trickNamePublisher.share()
```
- **Subject** 는 Publisher와 Subscriber의 역할을 모두 수행할 수 있다.
- subscribe를 통해 upstream Publisher를 구독하고, 값을 downstream Subscriber로 전달한다.
- send를 사용해 명령형으로 값을 발행할 수도 있다.
- share를 활용해 스트림을 공유하거나 Subject를 주입하는 데 사용한다.

## Working with SwiftUI

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*hl61vlgEZq44kxdAoLrg1Q.png)

- SwiftUI 의 놀라운 점 중 하나는 종속성만 설명하면 프레임워크가 나머지를 처리한다는 것이다.
- Combine 관점에서 데이터가 언제 어떻게 변경되었는지 설명하는 Publisher 를 제공해야 한다.
- 사용자 정의 유형을 ObservableObject Protocol 에 맞추기만 하면 된다.
```c
protocol ObservableObject  {
  associatedtype PublisherType : Publisher where PublisherType.Failure == Never
  
  var didChange: PublisherType { get }
}
```
- Publisher 에 도달하기 전에 업스트림 오류를 처리한다.(Failure == Never)
- didChange 라는 속성을 통해 유형이 변경 되었을 때 알리는 Publisher 를 생성한다.

**1\. 초기 상태: Combine 적용 전**

```c
// Combine 적용 전: 단순한 모델 클래스
class WizardModel {
    var trick: WizardTrick
    var wand: Wand?
}
```
- WizardModel은 단순히 trick과 wand라는 두 프로퍼티를 가지는 일반 클래스.
- Combine이나 SwiftUI와의 데이터 바인딩 기능은 없음.

**2\. Combine 시작: PassthroughSubject 추가**

```c
// Combine 적용: 데이터 변경 알림을 위한 PassthroughSubject 추가
class WizardModel: ObservableObject {
    var trick: WizardTrick
    var wand: Wand?
    let didChange = PassthroughSubject<Void, Never>() // 데이터 변경 시 알림을 보내는 Subject
}
```
- ObservableObject를 채택해 SwiftUI와 통합.
- PassthroughSubject를 추가해 상태 변경을 외부에 알릴 수 있도록 설정.

**3\. 상태 변경 알림 구현**

```c
// Combine 적용: 상태 변경 시 PassthroughSubject로 알림 전송
class WizardModel: BindableObject {
    var trick: WizardTrick { didSet { didChange.send() } } // 변경 시 알림
    var wand: Wand? { didSet { didChange.send() } }        // 변경 시 알림
    let didChange = PassthroughSubject<Void, Never>()
}
```
- didSet을 사용해 trick과 wand가 변경될 때마다 didChange.send() 호출.
- Combine을 통해 SwiftUI와 데이터 바인딩 가능.

**4\. SwiftUI와 통합: @ObservedObject 추가**

```c
// Combine + SwiftUI: 데이터 바인딩을 위해 @ObjectBinding 추가
struct TrickView: View {
    @ObservedObject var model: WizardModel // WizardModel을 관찰
    var body: some View {
        Text(model.trick.name) // 모델의 trick.name을 UI에 표시
    }
}
```

**5\. 최종**

```c
import SwiftUI
import Combine

// ObservableObject를 사용하여 데이터 변경 알림
class WizardModel: ObservableObject {
    @Published var trick: WizardTrick // 변경 시 자동으로 알림
    @Published var wand: Wand?       // 변경 시 자동으로 알림
    
    init(trick: WizardTrick, wand: Wand? = nil) {
        self.trick = trick
        self.wand = wand
    }
}

// SwiftUI와 통합
struct TrickView: View {
    @ObservedObject var model: WizardModel 
    var body: some View {
        Text(model.trick.name) // 모델의 trick.name을 UI에 표시
    }
}
```