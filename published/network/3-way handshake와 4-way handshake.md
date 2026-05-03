---
slug: net-tcp-handshake
order: 1001
related: [TCP와 UDP, HTTP와 HTTPS]
---

> 3-way handshake는 TCP 연결을 성립하고, 4-way handshake는 양방향 연결을 독립적으로 종료한다.

## 정의
- 3-way handshake: TCP/IP 통신에서 데이터 전송 전 신뢰성 있는 세션을 수립하는 과정. SYN → SYN-ACK → ACK 3단계로 이루어진다.
- 4-way handshake: TCP 세션을 종료하는 과정. FIN → ACK → FIN → ACK 4단계로 양방향 연결을 각각 독립적으로 닫는다.
- SYN(Synchronize Sequence Numbers): 연결 요청 플래그. 초기 순서 번호를 동기화한다.
- ACK(Acknowledgment): 수신 확인 플래그. 상대방의 요청을 수락했음을 알린다.
- FIN(Finish): 연결 종료 요청 플래그. 더 이상 보낼 데이터가 없음을 의미한다.
- TIME_WAIT: 클라이언트가 FIN을 수신한 후 일정 시간(기본 240초) 대기하는 상태. 지연 도착 패킷 유실을 방지한다.

## 핵심 포인트
- 3-way handshake 흐름: 클라이언트가 SYN 전송(SYN_SENT) → 서버가 SYN-ACK 응답(SYN_RECEIVED) → 클라이언트가 ACK 전송 → 연결 성립(ESTABLISHED).
- 연결 성립은 3번으로 충분하다. 서버의 SYN과 ACK를 하나의 패킷으로 합칠 수 있기 때문이다.
- 4-way handshake 흐름: 클라이언트 FIN → 서버 ACK(TIME_WAIT 진입) → 서버 FIN → 클라이언트 ACK.
- 연결 종료가 4단계인 이유는 서버가 ACK를 보낸 후 아직 전송 중인 데이터가 남아 있을 수 있기 때문이다. FIN과 ACK를 분리해야 안전하다.
- TIME_WAIT는 클라이언트 측에서 발생하며, 서버의 FIN보다 늦게 도착하는 패킷을 처리하기 위한 안전장치다.
- 양쪽 모두 초기 순차 일련번호(Sequence Number)를 교환하여 데이터 순서를 보장한다.

## 면접 질문
- 3-way handshake 과정을 단계별로 설명해보세요.
- 왜 연결 수립은 3번이고 종료는 4번인가요?
- TIME_WAIT 상태가 왜 필요한가요?
- SYN_SENT, SYN_RECEIVED, ESTABLISHED는 각각 어느 시점의 상태인가요?

## 확인 문제
- 클라이언트가 SYN을 보낸 뒤 SYN-ACK를 기다리는 상태 이름은?
- 서버가 FIN을 보내기 전 ACK만 보내고 기다리는 이유는?
- 클라이언트가 서버의 FIN을 받고도 바로 세션을 닫지 않는 이유는?

## 키워드
3-way handshake, 4-way handshake, SYN, ACK, FIN, TIME_WAIT, SYN_SENT, SYN_RECEIVED, ESTABLISHED, TCP 연결, TCP 종료

## 연관 콘텐츠
- [[TCP와 UDP]]
- [[HTTP와 HTTPS]]
