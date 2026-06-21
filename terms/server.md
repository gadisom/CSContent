---
category: server
title: Server 단어장
---

# Server 단어장

## MVC
- answer: Model, View, Controller로 역할을 나누는 애플리케이션 구조
- detail: MVC는 데이터, 화면, 요청 처리 책임을 분리한다. 서버에서는 Controller가 요청을 받고 Model을 통해 데이터를 처리한 뒤 응답을 만든다.

## DispatcherServlet
- answer: Spring MVC에서 들어온 HTTP 요청을 가장 먼저 받아 적절한 컨트롤러로 보내는 핵심 객체
- detail: Front Controller 패턴을 구현한 구성 요소다. 요청 매핑, 핸들러 어댑터, 뷰 처리 흐름의 중심에 있다.

## Filter
- answer: 서블릿에 요청이 도달하기 전후에 공통 처리를 수행하는 구성 요소
- detail: 필터는 인증, 로깅, 인코딩 처리처럼 웹 컨테이너 레벨의 공통 작업에 자주 쓰인다.

## Interceptor
- answer: Spring MVC 요청 처리 전후에 컨트롤러 흐름을 가로채는 구성 요소
- detail: 인터셉터는 Spring 컨텍스트 안에서 동작한다. 인증 확인, 로깅, 권한 검사 같은 컨트롤러 주변 로직에 사용된다.

## AOP
- answer: 여러 곳에 흩어진 공통 관심사를 분리해 적용하는 프로그래밍 방식
- detail: Aspect-Oriented Programming의 줄임말이다. 로깅, 트랜잭션, 권한 검사처럼 반복되는 부가 기능을 핵심 로직과 분리한다.

## Proxy
- answer: 실제 대상 객체 앞에서 대신 요청을 받아 부가 동작을 수행하는 객체
- detail: 프록시는 접근 제어, 지연 로딩, 트랜잭션, AOP 같은 기능을 구현할 때 자주 사용된다.

## Message Queue
- answer: 생산자와 소비자 사이에서 메시지를 임시로 보관하고 전달하는 구조
- detail: 메시지 큐는 작업을 비동기로 처리하고 시스템 사이의 결합도를 낮춘다. 트래픽이 몰릴 때 완충 역할도 할 수 있다.

## Docker Image
- answer: 컨테이너 실행에 필요한 파일과 설정을 담은 읽기 전용 템플릿
- detail: 이미지는 애플리케이션, 런타임, 라이브러리, 환경 설정을 함께 묶는다. 같은 이미지로 여러 컨테이너를 만들 수 있다.

## Docker Container
- answer: Docker Image를 실행한 격리된 프로세스 환경
- detail: 컨테이너는 호스트 커널을 공유하면서 애플리케이션 실행 환경을 분리한다. 배포 환경 차이를 줄이는 데 도움을 준다.

## CI/CD
- answer: 코드 변경을 자동으로 빌드, 테스트, 배포하는 개발 흐름
- detail: Continuous Integration과 Continuous Delivery 또는 Deployment의 줄임말이다. 반복 배포의 실수를 줄이고 피드백을 빠르게 만든다.

## Blue-Green Deployment
- answer: 두 환경 중 하나를 운영하고 다른 하나에 새 버전을 배포한 뒤 트래픽을 전환하는 방식
- detail: 문제가 생기면 이전 환경으로 빠르게 되돌릴 수 있다. 대신 두 환경을 유지할 자원이 필요하다.

## Canary Deployment
- answer: 일부 사용자나 서버에만 새 버전을 먼저 배포해 검증하는 방식
- detail: 카나리 배포는 위험을 작게 나누어 확인한다. 지표가 안정적이면 점진적으로 배포 범위를 넓힌다.

## JDBC
- answer: Java 애플리케이션이 데이터베이스와 통신하기 위한 표준 API
- detail: Java Database Connectivity의 줄임말이다. SQL 실행, 연결 관리, 결과 조회 같은 작업의 기본 인터페이스를 제공한다.

## ORM
- answer: 객체와 관계형 데이터베이스 테이블을 매핑해주는 기술
- detail: Object-Relational Mapping의 줄임말이다. SQL을 직접 다루는 양을 줄일 수 있지만, 생성되는 쿼리와 영속성 컨텍스트를 이해해야 한다.

## WebSocket
- answer: 클라이언트와 서버가 하나의 연결로 양방향 통신하는 프로토콜
- detail: WebSocket은 실시간 채팅, 알림, 협업 기능처럼 서버가 즉시 데이터를 보내야 하는 경우에 적합하다.

## SSE
- answer: 서버가 클라이언트로 단방향 이벤트를 지속적으로 보내는 방식
- detail: Server-Sent Events의 줄임말이다. 브라우저가 HTTP 연결을 유지하고 서버 이벤트를 순서대로 받는다.

## Polling
- answer: 클라이언트가 일정 주기로 서버에 새 데이터가 있는지 물어보는 방식
- detail: 구현은 단순하지만 요청이 반복되어 불필요한 트래픽이 생길 수 있다. 실시간성이 강할수록 주기 선택이 중요하다.

## JWT
- answer: JSON 형태의 클레임을 서명해 전달하는 토큰 형식
- detail: JSON Web Token의 줄임말이다. 서버가 토큰의 서명을 검증해 위변조 여부를 확인할 수 있다.

## Session
- answer: 서버가 사용자 상태를 저장하고 식별자만 클라이언트에 전달하는 방식
- detail: 세션은 로그인 상태 같은 정보를 서버에 보관한다. 클라이언트는 보통 세션 ID를 쿠키로 전달한다.

## Cookie
- answer: 브라우저가 저장하고 요청마다 서버에 보낼 수 있는 작은 데이터
- detail: 쿠키는 세션 ID, 사용자 설정, 추적 정보 등에 쓰인다. 보안 속성인 HttpOnly, Secure, SameSite 설정이 중요하다.
