---
category: ios
title: iOS 단어장
---

# iOS 단어장

## App Lifecycle
- answer: 앱이 실행, 활성화, 백그라운드, 종료 상태로 이동하는 흐름
- detail: 앱 생명주기는 사용자의 실행, 홈 이동, 시스템 자원 상황에 따라 변한다. 각 상태에 맞춰 저장, 복원, 네트워크 작업을 관리한다.

## Foreground
- answer: 앱이 화면에 보이고 사용자와 상호작용할 수 있는 상태
- detail: 포그라운드에서는 UI 업데이트와 사용자 입력 처리가 가능하다. 활성 상태인지 비활성 상태인지에 따라 세부 동작이 달라질 수 있다.

## Background
- answer: 앱이 화면에는 보이지 않지만 제한적으로 작업할 수 있는 상태
- detail: 백그라운드에서는 실행 시간이 제한된다. 위치, 오디오, 백그라운드 작업처럼 허용된 작업만 계속될 수 있다.

## Suspended
- answer: 앱이 메모리에 남아 있지만 코드는 실행되지 않는 상태
- detail: Suspended 상태의 앱은 빠르게 복귀할 수 있다. 시스템 메모리가 부족하면 예고 없이 종료될 수 있다.

## Combine
- answer: 시간에 따라 발생하는 값의 흐름을 선언적으로 처리하는 프레임워크
- detail: Combine은 Publisher와 Subscriber를 연결해 비동기 이벤트를 처리한다. 네트워크 응답, 사용자 입력, 상태 변화 등을 스트림처럼 다룰 수 있다.

## Publisher
- answer: 값이나 완료 이벤트를 내보내는 Combine 구성 요소
- detail: Publisher는 Subscriber에게 값을 전달한다. 비동기 작업의 결과나 연속적인 이벤트를 표현하는 데 사용된다.

## Subscriber
- answer: Publisher가 내보낸 값을 받아 처리하는 Combine 구성 요소
- detail: Subscriber는 값을 얼마나 받을지 요청하고, 전달된 값과 완료 이벤트를 처리한다.

## Subscription
- answer: Publisher와 Subscriber 사이의 연결과 수요를 관리하는 객체
- detail: Subscription은 데이터 흐름을 시작하거나 취소하는 역할을 한다. Combine의 backpressure 처리와도 관련된다.

## Operator
- answer: Publisher의 값을 변환하거나 조합하는 Combine 연산
- detail: map, filter, debounce, merge 같은 연산자가 있다. 여러 비동기 흐름을 읽기 쉬운 파이프라인으로 만들 수 있다.

## AnyCancellable
- answer: Combine 구독을 취소할 수 있게 보관하는 타입
- detail: AnyCancellable이 해제되면 연결된 구독도 취소된다. 보통 프로퍼티에 저장해 구독 생명주기를 관리한다.

## Main Thread
- answer: iOS에서 UI 작업을 처리해야 하는 주 실행 흐름
- detail: UIKit과 SwiftUI의 UI 변경은 메인 스레드에서 수행해야 한다. 비동기 작업 결과를 화면에 반영할 때 메인 스레드 전환이 필요하다.

## RunLoop
- answer: 입력 이벤트와 타이머 같은 작업을 반복적으로 처리하는 이벤트 루프
- detail: RunLoop는 스레드가 이벤트를 기다리고 처리하도록 돕는다. 타이머나 특정 스케줄링 동작과 관련해 자주 등장한다.
