---
slug: net-tcp-handshake
order: 1001
related: [TCP와 UDP, HTTP와 HTTPS]
---

> 3-way handshake는 TCP 연결을 시작하기 위해 양쪽의 통신 가능성과 초기 순서 번호를 맞추는 과정이고, 4-way handshake는 양방향 TCP 연결을 각 방향별로 안전하게 닫는 과정이다.

## 정의
![[tcp-handshake-flow.png]]
- 3-way handshake: TCP에서 데이터를 주고받기 전에 연결을 수립하는 3단계 절차다. 클라이언트 SYN, 서버 SYN+ACK, 클라이언트 ACK 순서로 진행된다.
- 4-way handshake: TCP 연결을 종료하는 4단계 절차다. 한쪽이 FIN을 보내면 상대가 ACK로 확인하고, 남은 데이터를 정리한 뒤 다시 FIN을 보내며, 마지막 ACK로 종료가 마무리된다.
- SYN(Synchronize Sequence Numbers): 연결을 시작하고 초기 순서 번호를 동기화하기 위한 TCP 플래그다. 첫 SYN에는 클라이언트의 초기 시퀀스 번호가 담긴다.
- ACK(Acknowledgment): 상대가 보낸 데이터를 어디까지 받았는지 확인하는 TCP 플래그다. ACK 번호는 다음에 기대하는 시퀀스 번호를 의미한다.
- FIN(Finish): 더 이상 보낼 데이터가 없다는 뜻의 TCP 플래그다. FIN은 한 방향의 전송 종료를 의미하므로, 반대 방향 전송은 별도로 닫힐 수 있다.
- Sequence Number: TCP가 바이트 스트림의 순서를 추적하기 위해 사용하는 번호다. 패킷이 나뉘거나 순서가 바뀌어 도착해도 올바른 순서로 재조립할 수 있게 한다.
- TIME_WAIT: 능동적으로 연결 종료를 마무리한 쪽이 마지막 ACK를 보낸 뒤 일정 시간 대기하는 상태다. 지연 패킷 처리와 마지막 ACK 유실에 대비하는 안전장치다.
- Half-close: TCP 연결에서 한쪽 방향 전송만 먼저 닫힌 상태다. 한쪽은 FIN을 보냈지만 반대쪽은 아직 남은 데이터를 보낼 수 있다.

## 핵심 포인트
- 3-way handshake의 첫 단계에서 클라이언트는 SYN을 보내고 SYN_SENT 상태가 된다. 이때 클라이언트는 자신의 초기 시퀀스 번호를 서버에 알린다.
- 서버는 SYN을 받으면 SYN_RECEIVED 상태가 되고, 클라이언트의 SYN에 대한 ACK와 서버 자신의 SYN을 함께 보낸다. 이 패킷이 흔히 SYN-ACK라고 불린다.
- 클라이언트는 서버의 SYN-ACK를 받으면 ACK를 보내고 ESTABLISHED 상태가 된다. 서버도 이 ACK를 받으면 ESTABLISHED 상태가 되어 양쪽 모두 데이터 전송 준비가 끝난다.
- 연결 수립이 2단계가 아니라 3단계인 이유는 양쪽 모두 송신과 수신이 가능한지 확인해야 하기 때문이다. 클라이언트의 마지막 ACK는 서버가 보낸 SYN을 클라이언트가 정상적으로 받았음을 증명한다.
- 연결 수립 단계에서 양쪽은 초기 시퀀스 번호를 교환한다. 이후 TCP는 시퀀스 번호와 ACK 번호를 이용해 데이터 순서 보장, 손실 감지, 재전송을 수행한다.
- 4-way handshake는 보통 능동 종료자가 FIN을 보내면서 시작된다. FIN을 보낸 쪽은 FIN_WAIT_1로 이동하고, 상대의 ACK를 받으면 FIN_WAIT_2에서 상대의 FIN을 기다린다.
- 수동 종료자는 FIN을 받으면 먼저 ACK를 보내고 CLOSE_WAIT 상태가 된다. 이 상태는 “상대는 더 이상 보내지 않지만, 나는 아직 보낼 데이터가 남아 있을 수 있음”을 뜻한다.
- 수동 종료자가 남은 데이터를 모두 보낸 뒤 FIN을 보내면 LAST_ACK 상태가 된다. 능동 종료자는 이 FIN에 ACK를 보내고 TIME_WAIT 상태로 들어간다.
- 연결 종료가 4단계인 이유는 TCP 연결이 양방향 독립 스트림이기 때문이다. 한쪽이 더 이상 보낼 데이터가 없다고 해서 상대도 즉시 보낼 데이터가 없는 것은 아니다.
- TIME_WAIT는 마지막 ACK가 유실되었을 때 상대가 FIN을 재전송할 수 있는 시간을 남긴다. 또한 이전 연결의 지연 패킷이 같은 4-tuple 연결에 섞이는 위험을 줄인다.
- TIME_WAIT는 주로 먼저 종료를 시작한 쪽에 생긴다. 클라이언트가 먼저 닫으면 클라이언트에, 서버가 먼저 닫으면 서버에 생길 수 있다.
- 서버에서 CLOSE_WAIT가 오래 남아 있으면 애플리케이션이 소켓을 제대로 닫지 않았다는 신호일 수 있다. 반대로 TIME_WAIT가 많은 것은 TCP 종료 절차의 정상적인 결과일 수 있다.
- TCP 연결은 IP와 포트 번호를 포함한 4-tuple로 식별된다. 같은 클라이언트 IP, 클라이언트 포트, 서버 IP, 서버 포트 조합의 지연 패킷을 구분하는 데 TIME_WAIT가 도움이 된다.

## 면접 질문
- 3-way handshake 과정을 단계별로 설명해보세요.
- 왜 연결 수립은 3번이고 종료는 4번인가요?
- TIME_WAIT 상태가 왜 필요한가요?
- SYN_SENT, SYN_RECEIVED, ESTABLISHED는 각각 어느 시점의 상태인가요?
- 4-way handshake에서 CLOSE_WAIT와 LAST_ACK는 각각 어떤 상태인가요?
- 2-way handshake만으로 TCP 연결을 수립하면 어떤 문제가 생길 수 있나요?
- TIME_WAIT가 클라이언트가 아니라 서버에 생길 수도 있나요?
- FIN과 ACK가 항상 분리되어야 하나요, 아니면 함께 전송될 수도 있나요?

## 확인 문제
- 클라이언트가 SYN을 보낸 뒤 SYN-ACK를 기다리는 상태 이름은?
- 서버가 FIN을 보내기 전 ACK만 보내고 기다리는 이유는?
- 클라이언트가 서버의 FIN을 받고도 바로 세션을 닫지 않는 이유는?
- TCP 연결 수립에서 양쪽 모두 초기 시퀀스 번호를 교환할까?
- TIME_WAIT는 마지막 ACK 유실에 대비하는 역할을 할까?
- CLOSE_WAIT가 오래 유지되면 애플리케이션이 소켓 종료를 제대로 처리하지 못했을 가능성이 있을까?

## 키워드
3-way handshake, 4-way handshake, SYN, ACK, FIN, Sequence Number, Acknowledgment Number, SYN_SENT, SYN_RECEIVED, ESTABLISHED, FIN_WAIT_1, FIN_WAIT_2, CLOSE_WAIT, LAST_ACK, TIME_WAIT, Half-close, TCP 연결, TCP 종료

## 연관 콘텐츠
- [[TCP와 UDP]]
- [[TCPIP 모델]]
- [[HTTP와 HTTPS]]
