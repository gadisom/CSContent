---
category: network
tag: TCP
---

#### 객관식 | [691]
TCP 3-way handshake의 올바른 순서는?
1. ✅ SYN → SYN-ACK → ACK
2. ACK → SYN → SYN-ACK
3. SYN → ACK → SYN-ACK
4. SYN-ACK → SYN → ACK
> 클라이언트가 SYN 전송, 서버가 SYN-ACK 응답, 클라이언트가 ACK를 보내 연결이 성립됩니다.

#### OX | [692]
연결 종료는 3-way handshake로 처리된다.
> X
> 연결 종료는 FIN-ACK-FIN-ACK의 4-way handshake로 처리됩니다. 서버가 아직 보낼 데이터가 남아 있을 수 있어 ACK와 FIN을 분리합니다.

#### 빈칸 | [693]
클라이언트가 SYN을 보낸 뒤 SYN-ACK를 기다리는 상태를 ___이라고 한다.
> SYN_SENT
> SYN을 전송한 후 아직 응답을 받지 못한 클라이언트의 상태입니다.

#### 빈칸 | [694]
서버가 SYN-ACK를 보내고 클라이언트의 ACK를 기다리는 상태를 ___이라고 한다.
> SYN_RECEIVED
> SYN-ACK를 전송한 후 최종 확인 ACK를 기다리는 서버의 상태입니다.

#### OX | [695]
TIME_WAIT 상태는 서버 측에서 발생한다.
> X
> TIME_WAIT는 클라이언트(연결 종료를 먼저 요청한 쪽)에서 발생합니다. 늦게 도착하는 패킷을 처리하기 위한 대기 상태입니다.

#### 객관식 | [696]
4-way handshake에서 연결 종료가 4단계인 이유는?
1. ✅ 서버가 ACK를 보낸 후 아직 전송 중인 데이터가 남아 있을 수 있기 때문이다
2. 클라이언트가 두 번 FIN을 보내야 하기 때문이다
3. 보안을 위해 한 번 더 확인하기 때문이다
4. UDP와의 호환성을 맞추기 위해서다
> 서버는 FIN을 받으면 즉시 ACK를 보내지만, 전송 중인 데이터를 모두 보낸 뒤에야 FIN을 보냅니다. 그래서 ACK와 FIN이 분리됩니다.

#### 객관식 | [697]
3-way handshake 과정에서 사용되는 플래그를 모두 고르시오. (2개)
1. ✅ SYN
2. FIN
3. ✅ ACK
4. RST
> SYN(연결 요청)과 ACK(수신 확인)가 3-way handshake에 사용됩니다. FIN은 연결 종료, RST는 강제 초기화에 쓰입니다.
