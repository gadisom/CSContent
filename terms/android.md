---
category: android
title: Android 단어장
---

# Android 단어장

## Compose
- answer: 선언형 방식으로 Android UI를 만드는 Jetpack UI 도구
- detail: Jetpack Compose는 상태가 바뀌면 UI를 다시 그리는 방식으로 동작한다. XML 레이아웃보다 코드 중심으로 화면을 구성한다.

## Composable
- answer: Compose에서 UI 조각을 선언하는 함수
- detail: Composable 함수는 화면의 일부를 표현한다. 상태 변화에 따라 필요한 부분이 다시 호출될 수 있다.

## State
- answer: UI가 어떤 모습으로 보여야 하는지 결정하는 데이터
- detail: Compose에서는 상태가 바뀌면 관련 UI가 다시 구성된다. 상태를 어디에 두고 어떻게 전달할지가 화면 구조의 핵심이다.

## Recomposition
- answer: 상태 변화에 맞춰 Composable을 다시 실행해 UI를 갱신하는 과정
- detail: Compose는 전체 화면을 항상 새로 만드는 것이 아니라 필요한 부분을 중심으로 재구성한다. 불필요한 재구성을 줄이는 설계가 중요하다.

## Modifier
- answer: Compose UI 요소의 크기, 배치, 클릭, 배경 등을 조정하는 체인형 객체
- detail: Modifier는 Composable에 기능과 스타일을 덧붙인다. 순서에 따라 적용 결과가 달라질 수 있다.

## remember
- answer: Recomposition 사이에서 값을 유지하기 위한 Compose 함수
- detail: remember는 Composable이 다시 실행되어도 특정 값을 보존한다. 화면 회전 같은 구성 변경까지 보존하려면 rememberSaveable을 사용할 수 있다.

## Map
- answer: 키와 값을 한 쌍으로 저장하는 자료구조 인터페이스
- detail: Map은 특정 키로 값을 빠르게 찾기 위해 사용한다. Kotlin과 Java에서 여러 구현체를 통해 제공된다.

## HashMap
- answer: 해시를 이용해 키-값 데이터를 저장하는 Map 구현체
- detail: HashMap은 평균적으로 빠른 검색과 삽입을 제공한다. 키의 hashCode와 equals 구현이 올바르게 동작해야 한다.

## Key-Value
- answer: 하나의 키로 하나의 값을 찾아가는 데이터 저장 방식
- detail: 키는 값을 식별하는 이름이나 식별자 역할을 한다. Map, 캐시, 설정 저장소 등에서 널리 사용된다.

## Hash Collision
- answer: 서로 다른 키가 같은 해시 위치로 계산되는 상황
- detail: 해시 충돌은 HashMap 내부에서 연결 리스트나 트리 같은 방식으로 처리될 수 있다. 충돌이 많으면 조회 성능이 떨어질 수 있다.
