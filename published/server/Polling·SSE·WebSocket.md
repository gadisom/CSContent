> 실시간 통신은 폴링→롱폴링→SSE→WebSocket 순으로 연결 유지 방향으로 발전했다. SSE는 서버→클라이언트 단방향, WebSocket은 양방향 통신이다.

## 정의
- 폴링: 클라이언트가 주기적으로 서버에 요청을 반복 전송. 매번 TCP 연결이 필요해 오버헤드가 크고 실시간성 확보가 어렵다.
- 롱 폴링: 서버가 응답할 때까지 연결을 유지. 응답 수신 후 연결을 끊고 재연결이 필요하며 커넥션을 점유한다.
- SSE(Server-Sent Events): HTTP 연결 1번으로 유지한 채 서버→클라이언트로 단방향 이벤트를 스트리밍. 연결 끊김 감지를 위해 heartbeat가 필요하다.
- WebSocket: HTTP Upgrade 헤더로 핸드셰이크 후 독립 TCP 기반 양방향 실시간 통신으로 전환한다.

## 핵심 포인트
- 폴링은 불필요한 요청으로 서버 부하가 크고 실시간성이 낮다.
- SSE는 서버가 연결 끊김을 즉시 파악할 수 없어 heartbeat로 끊긴 연결을 회수한다.
- WebSocket은 초기 HTTP 핸드셰이크(Upgrade: websocket) 이후 별도 프로토콜로 동작한다.
- 단방향 서버 push(알림, 주가 피드)는 SSE, 채팅처럼 양방향이 필요한 경우는 WebSocket이 적합하다.

## 면접 질문
- 폴링과 롱 폴링의 차이는?
- SSE와 WebSocket을 각각 어떤 상황에 사용하나요?
- WebSocket 연결 수립 과정을 설명해보세요.

## 확인 문제
- SSE에서 heartbeat가 필요한 이유는?
- 롱 폴링의 단점 두 가지는?
- WebSocket이 HTTP와 다른 별도 프로토콜인 이유는?

## 키워드
폴링, 롱폴링, SSE, WebSocket, heartbeat, HTTP Upgrade, 실시간 통신, 단방향, 양방향
