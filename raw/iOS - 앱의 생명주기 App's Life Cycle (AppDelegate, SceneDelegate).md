---
title: "[iOS] - 앱의 생명주기 App's Life Cycle (AppDelegate, SceneDelegate)"
source: "https://clamp-coding.tistory.com/407"
author:
  - "[[clamp]]"
published: 2023-03-27
created: 2026-04-24
description: "앱의 생명주기란 App의 생명주기는 App의 실행/종료 및 App이 Foreground/Background 상태에 있을 때, 시스템이 발생시키는 event에 의해 App의 상태가 전환되는 일련의 과정을 뜻한다. App은 여러가지App이 한 번에 실행될 수 있고, 어떤App을 사용하다가 어떤 App을 사용할 수 있다. 그럼 App이 다른App으로 전환될 수 있고 백그라운드로 전환될 수 있다. 또는 App이 완전히 종료될 수 있다. 이런 시점에 운영체제가 자동으로 호출하는 메서드가 존재하며, 이러한 메서드 실행의 과정을 앱 라이프 사이클(App Life Cycle)이라고 부른다. 앱 라이프 사이클은 AppDelegate와 SceneDelegate에 의해 관리된다. Foreground/Background Fo.."
tags:
  - "clippings"
---
## 앱의 생명주기란

App의 생명주기는 App의 실행/종료 및 App이 Foreground/Background 상태에 있을 때,

시스템이 발생시키는 event에 의해 App의 상태가 전환되는 일련의 과정을 뜻한다.

App은 여러가지App이 한 번에 실행될 수 있고, 어떤App을 사용하다가 어떤 App을 사용할 수 있다.

그럼 App이 다른App으로 전환될 수 있고 백그라운드로 전환될 수 있다. 또는 App이 완전히 종료될 수 있다.

이런 시점에 운영체제가 자동으로 호출하는 메서드가 존재하며, 이러한 메서드 실행의 과정을 앱 라이프 사이클(App Life Cycle)이라고 부른다.

앱 라이프 사이클은 **AppDelegate** 와 **SceneDelegate** 에 의해 관리된다.

![](https://blog.kakaocdn.net/dna/cn6Grk/btr6oJLfgYK/AAAAAAAAAAAAAAAAAAAAAP5WAVk_SJK28pZQjX42vYimmN7PK3sLyaNE9V_PKRZu/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1777561199&allow_ip=&allow_referer=&signature=57huVqkSiLBDjWAUr5GYkhaBNGY%3D)

---

#### Foreground/Background

Foreground

내가 지금 카카오톡을 사용하고 있다면 카카오톡은 Foreground상태이다.

![](https://blog.kakaocdn.net/dna/bam9Oj/btr5Tp9hds4/AAAAAAAAAAAAAAAAAAAAAANXEuPagYs3Lzlpz0HYbB0JB2Ynyn7X6FWaQc4oonkk/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1777561199&allow_ip=&allow_referer=&signature=NBped3wi%2BUJyGfkVf4LgQy%2Beqa4%3D)

Foreground인 상태

Background

카카오톡으로 카톡을 하고있는 도중에 전화를 받거나 다른 앱으로 넘어가게 된다면 이 때 카카오톡은 backgound상태가 된다. Background 상태는 잠시 비활성화가 되는 상태이다.

![](https://blog.kakaocdn.net/dna/ujXe3/btr6eVzaV5T/AAAAAAAAAAAAAAAAAAAAAP6QjxRE5fxpGvz0dvo26ZEFquFofdMfDe-8GVKuIXnE/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1777561199&allow_ip=&allow_referer=&signature=iH3K90jACTBV548%2Bhnd6ZsiUt%2Bw%3D)

Background인 상태

---

#### 앱의 생명주기를 왜 알아야 할까❓

Fourground 상태인 앱은 화면을 점유하고 있기 때문에 시스템 리소스 보다 높은 우선순위를 가지고 있다.

Background 상태인 앱은 최소한의 작업을 수행해야 한다.

앱의 상태에 따라 그에 맞는 동작을 수행시켜야 하기 때문에 앱의 생명 주기를 파악하고 있어야 한다.

앱의 생명 주기를 알아야 구현할 수 있는 기능도 존재한다.

예를 들어 은행 앱들은 앱에서 벗어나면 보안 화면을 보여주는 경우가 많다.

Background 상태에서 언제든 종료될 수 있다는 것을 모르면 Background 기능 개발이 당황스러울 것이다.

앱이 화면에 보일 때만 타이머를 동작시키고 싶을 때도 앱의 생명주기에 대해 알아야 한다.

---

앱 라이프 사이클의 실행시점 및 메서드

![](https://blog.kakaocdn.net/dna/uNN4r/btr5YVNA9zL/AAAAAAAAAAAAAAAAAAAAADVpLr3h8w7UAgM96NFP2UNdeByGIDFqTv6Cen7cHzPw/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1777561199&allow_ip=&allow_referer=&signature=HqcE8wdZS0TUv97Guvn%2FY%2FywmC4%3D)

- Not Running: App이 실행중이지 않은 상태
- Foregound: App의 실행화면(Scene)을 사용자에게 보여주는 상태(영역)
	- Active: 사용자가 App을 100% 컨트롤 할 수 있는 상태
		- inActive: App사용중 전화 또는 문자와 같은 이벤트가 접근한 상태(App이 잠시 멈추는 상태이며 100%컨트롤할 순 없다)
- Background: App의 실행화면(Scene)이 내려간 상태(영역)
	- Background Running: App의 화면은 내려갔지만 계속 작동하는 상태를 의미. 애플은 보안등의 이유로 Background영역에서 App의 작동을 허용하지 않는다. 하지만 일부 App은 작동이 가능하다. (음악App같은 경우 작동을 허용)
- Suspended: 실행 대기 상태(영역)을 의미. App의 실행 화면(Scene)이 내려가면 대부분의 App은 대기상태로 전환

### ✅ AppDelegate

#### 1\. didFinishLaunchingWithOptions(앱이 처음 실행될 때)

파란색 1번을 의미한다.

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        return true
    }
```

Not Running 상태의 초기 App을 실행할 때 사용자에게 화면(Scene)이 보일 수 있도록 Foreground 영역에 접근하는 메서드이며, App화면이 보이기 직전에 호출된다.

#### 2\. configurationForConnecting(새로운 Scene을 생성할 때 호출)

파란색 2번을 의미한다

```swift
func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        // Called when a new scene session is being created.
        // Use this method to select a configuration to create the new scene with.
        return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
    }
```

새로운 화면(Scene)을 생성할 때 호출된다.

iOS12 이전에는 하나의 디바이스에서 단일 화면(Scene)만이 존재할 수 있었지만 iOS13부터 하나의 디바이스(iPad)에 여러 화면을 가질 수 있게 되었다.(iPad의 멀티태스킹)

#### 3\. didDiscardSceneSessions

파란색 3번을 의미한다

화면의 세션이 제거되기 직전에 호출되는 메서드.

```swift
func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
        // Called when the user discards a scene session.
        // If any sessions were discarded while the application was not running, this will be called shortly after application:didFinishLaunchingWithOptions.
        // Use this method to release any resources that were specific to the discarded scenes, as they will not return.
    }
```

화면을 영구적으로 메모리에서 해제될 때만 해당 메서드가 호출된다.(Background에 있는 App이 종료되려고 할 때 (Background에 있는 App이 종료되려고 할 때 호출되는 메서드는 applicationWillTerminate: 메서드이다.)

---

### ✅SceneDelegate

#### 0\. scene() (Scene이 해당 App에 추가될 때)

그림에는 나와있지 않은 단계

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        // Use this method to optionally configure and attach the UIWindow \`window\` to the provided UIWindowScene \`scene\`.
        // If using a storyboard, the \`window\` property will automatically be initialized and attached to the scene.
        // This delegate does not imply the connecting scene or session are new (see \`application:configurationForConnectingSceneSession\` instead).
        guard let _ = (scene as? UIWindowScene) else { return }
    }
```

화면(Scene)이 해당 App에 추가(연결)될 때 호출되는 메서드이다.

초기 화면을 지정하거나 Window를 설정한다.

#### 1\. sceneDidBecomeActive()

빨간색 1번을 의미한다.

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
        // Called when the scene has moved from an inactive state to an active state.
        // Use this method to restart any tasks that were paused (or not yet started) when the scene was inactive.
    }
```

화면(Scene)을 InActive에서 Active로 이동시킬 때 호출되는 메서드.

App을 처음 실행할 때 사용자가 해당 App을 100% 조작할 수 있도록 시켜주는 메서드

해당 메서드는 Foreground영역에서만 동작한다.

#### 2\. sceneWillResignActive()

빨간색 2번을 의미한다.

```swift
func sceneWillResignActive(_ scene: UIScene) {
        // Called when the scene will move from an active state to an inactive state.
        // This may occur due to temporary interruptions (ex. an incoming phone call).
    }
```

화면(Scene)을 Active에서 InActive로 이동시킬 때 호출되는 메서드.

App사용중 전화 또는 문자등의 특정 이벤트가 발생하면 해당 App의 화면은 이 메서드를 통해 Active에서 InActive로 이동한다.

해당 메서드는 Foreground 영역에서만 동작한다.

#### 3\. sceneDidEnterBackground()

빨간색 3번을 의미한다.

```swift
func sceneDidEnterBackground(_ scene: UIScene) {
        // Called as the scene transitions from the foreground to the background.
        // Use this method to save data, release shared resources, and store enough scene-specific state information
        // to restore the scene back to its current state.
    }
```

화면(Scene)을 InActive에서 Background영역으로 이동시킬 때 호출되는 메서드.

#### 4\. sceneWillEnterForeground()

빨간색 4번을 의미한다.

```swift
func sceneWillEnterForeground(_ scene: UIScene) {
        // Called as the scene transitions from the background to the foreground.
        // Use this method to undo the changes made on entering the background.
    }
```

화면(Scene)을 Background에서 Frreground(InActive)영역으로 이동시킬 때 호출되는 메서드

#### 5\. sceneDidDisconnect()

빨간색 5번을 의미한다.

```swift
func sceneDidDisconnect(_ scene: UIScene) {
        // Called as the scene is being released by the system.
        // This occurs shortly after the scene enters the background, or when its session is discarded.
        // Release any resources associated with this scene that can be re-created the next time the scene connects.
        // The scene may re-connect later, as its session was not necessarily discarded (see \`application:didDiscardSceneSessions\` instead).
    }
```

화면(Scene)이 해제될 때 호출되는 메서드.

해당 메서드는 App의 화면이 Background영역에 들어간 직후 또는 화면의 세션이 버려질 때 호출되는 메서드이다.

(메모리로부터 영구적으로 버려지는건 아니다. 사용자가 해당 화면에 다시 접근할 여지가 있기 때문이다. 완젼한 App종료는 아님.)

- Foreground mode는 시스템 리소스에 높은 우선순위를 가지며 foreground상태의 앱이 리소스를 할당받고 사용할 수 있도록 운영체제는 background앱을 종료하기도 한다.
- Background mode는 가능한 적은 메모리 공간을 사용해야하며 일부 앱(음악앱 등..)을 제외하면 background mode가 아닌 suspend 상태가 된다. 이런 앱들은 운영체제에 의해 종료될 수 있다.

[저작자표시 비영리 동일조건 (새창열림)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ko)