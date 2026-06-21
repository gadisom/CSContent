---
category: network
title: 네트워크 단어장
---

# 네트워크 단어장

## TTL
- answer: DNS 응답이나 네트워크 정보가 유효한 시간
- detail: Time To Live의 줄임말이다. DNS에서는 캐시된 응답을 얼마나 오래 재사용할 수 있는지 나타낸다. TTL이 길면 조회는 줄지만 변경 반영이 늦고, 짧으면 반영은 빠르지만 조회가 늘어난다.

## DNS
- answer: 도메인 이름을 IP 주소 같은 네트워크 주소로 바꾸는 시스템
- detail: Domain Name System의 줄임말이다. 브라우저가 서버에 연결하기 전에 사람이 읽기 쉬운 도메인을 실제 서버 주소로 해석한다.

## Resolver
- answer: 클라이언트 대신 DNS 응답을 찾아주는 재귀 해석기
- detail: Recursive Resolver를 뜻한다. 브라우저나 운영체제의 요청을 받아 루트, TLD, 권한 있는 네임서버 등을 조회하고 최종 응답을 돌려준다.

## Authoritative Name Server
- answer: 특정 도메인의 실제 DNS 레코드를 관리하는 권한 있는 네임서버
- detail: 재귀 해석기가 최종적으로 확인하는 서버이며, A, AAAA, CNAME 같은 레코드 정보를 제공한다.

## A Record
- answer: 도메인을 IPv4 주소에 연결하는 DNS 레코드
- detail: Address Record를 뜻한다. 예를 들어 `example.com`이 어떤 IPv4 주소로 가야 하는지 알려준다.

## AAAA Record
- answer: 도메인을 IPv6 주소에 연결하는 DNS 레코드
- detail: A 레코드가 IPv4 주소를 다룬다면, AAAA 레코드는 IPv6 주소를 다룬다.

## CNAME
- answer: 하나의 도메인 이름을 다른 도메인 이름의 별칭으로 연결하는 레코드
- detail: Canonical Name의 줄임말이다. 실제 주소를 직접 가리키기보다 다른 정식 이름을 참조하게 만든다.

## HTTP
- answer: 웹에서 클라이언트와 서버가 요청과 응답을 주고받는 프로토콜
- detail: HyperText Transfer Protocol의 줄임말이다. 기본 HTTP는 평문 기반이며, 보안이 필요한 통신은 TLS가 적용된 HTTPS로 보호한다.

## HTTPS
- answer: HTTP 통신을 TLS로 보호하는 방식
- detail: HyperText Transfer Protocol Secure의 줄임말이다. 서버 인증, 암호화, 무결성 검사를 통해 웹 요청과 응답을 안전하게 주고받도록 한다.

## URI
- answer: 웹에서 리소스를 식별하기 위한 문자열
- detail: Uniform Resource Identifier의 줄임말이다. REST API에서는 URI가 사용자, 게시글 같은 리소스를 가리키고, HTTP 메서드가 그 리소스에 대한 행위를 표현한다.

## URL
- answer: 리소스의 위치와 접근 방법을 함께 나타내는 주소
- detail: Uniform Resource Locator의 줄임말이다. URL은 URI의 한 종류이며, 프로토콜, 도메인, 경로처럼 리소스에 도달하는 위치 정보를 포함한다.

## TLS
- answer: 통신 구간에 암호화, 무결성, 인증을 제공하는 보안 프로토콜
- detail: Transport Layer Security의 줄임말이다. HTTPS에서는 TLS 핸드셰이크로 세션 키를 만들고 이후 데이터를 대칭키로 암호화한다.

## Session Key
- answer: 한 연결에서 실제 데이터 암호화에 사용하는 임시 대칭키
- detail: TLS는 비대칭키 기반 절차로 세션 키를 만들고, 이후 HTTP 데이터는 이 키로 빠르게 암호화한다.

## Public Key
- answer: 외부에 공개할 수 있는 비대칭키 쌍의 한쪽 키
- detail: 공개키는 개인키와 짝을 이루며, 인증서 검증이나 키 교환 과정에서 사용된다.

## Private Key
- answer: 소유자만 안전하게 보관해야 하는 비대칭키 쌍의 한쪽 키
- detail: 개인키가 노출되면 해당 키 기반의 인증과 복호화 신뢰가 깨질 수 있다.

## SYN
- answer: TCP 연결을 시작하자고 보내는 제어 플래그
- detail: 3-way handshake의 첫 단계에서 클라이언트가 서버에게 연결 시작 의사를 알릴 때 사용한다.

## ACK
- answer: 상대가 보낸 데이터를 확인했다는 의미의 제어 플래그
- detail: TCP에서는 데이터 수신 확인과 연결 수립/종료 단계에서 사용된다.

## FIN
- answer: TCP 연결에서 더 이상 보낼 데이터가 없음을 알리는 제어 플래그
- detail: 4-way handshake에서 연결 종료 의사를 전달하는 데 사용된다.

## TIME_WAIT
- answer: TCP 연결 종료 후 마지막 패킷 지연이나 재전송에 대비해 잠시 기다리는 상태
- detail: 마지막 ACK가 유실되었을 때를 대비하고, 이전 연결의 지연 패킷이 새 연결에 섞이지 않도록 돕는다.

## Port
- answer: 같은 호스트 안에서 어떤 애플리케이션으로 전달할지 구분하는 번호
- detail: IP가 호스트를 찾는 단서라면, 포트는 그 호스트 안의 서비스나 프로세스를 구분한다.

## CORS
- answer: 브라우저가 다른 출처의 자원 요청을 제한하고 서버 허용 헤더로 완화하는 메커니즘
- detail: Cross-Origin Resource Sharing의 줄임말이다. 서버 간 통신 자체의 문제가 아니라 브라우저 보안 정책과 관련된 동작이다.

## Preflight
- answer: 실제 CORS 요청 전에 브라우저가 허용 여부를 확인하는 사전 요청
- detail: 브라우저는 특정 조건의 교차 출처 요청에서 OPTIONS 요청으로 서버의 허용 정책을 먼저 확인한다.

## Root Name Server
- answer: DNS 조회에서 최상위 출발점 역할을 하는 네임서버
- detail: 루트 네임서버는 특정 도메인의 최종 IP를 직접 알려주기보다, 다음에 물어볼 TLD 네임서버 정보를 알려준다.

## TLD Name Server
- answer: .com, .kr 같은 최상위 도메인 정보를 담당하는 네임서버
- detail: Top-Level Domain Name Server를 뜻한다. 재귀 해석기가 권한 있는 네임서버로 가기 전에 거치는 단계다.

## MX Record
- answer: 도메인의 메일 서버 정보를 나타내는 DNS 레코드
- detail: Mail Exchange Record의 줄임말이다. 해당 도메인으로 이메일을 보낼 때 어떤 메일 서버를 사용해야 하는지 알려준다.

## DNS Cache
- answer: DNS 조회 결과를 일정 시간 저장해 재사용하는 캐시
- detail: DNS 캐시는 반복 조회를 줄여 응답 시간을 줄인다. TTL이 지나면 캐시된 응답을 다시 확인해야 한다.

## IP Address
- answer: 네트워크에서 호스트를 찾기 위한 주소
- detail: IP 주소는 목적지 장비나 서버를 찾는 단서다. 포트 번호가 그 호스트 안의 애플리케이션을 구분한다면, IP 주소는 호스트 자체를 찾는 데 쓰인다.

## MAC Address
- answer: 같은 네트워크 안에서 장치를 식별하는 물리 주소
- detail: MAC 주소는 데이터 링크 계층에서 주로 사용된다. IP 주소가 네트워크 간 경로를 찾는 데 쓰인다면, MAC 주소는 같은 링크 안의 장치를 구분하는 데 쓰인다.

## OSI 7 Layer
- answer: 네트워크 통신을 일곱 역할 계층으로 나눈 참조 모델
- detail: 물리, 데이터 링크, 네트워크, 전송, 세션, 표현, 응용 계층으로 나뉜다. 실제 구현보다 통신 역할을 단계별로 이해하기 위한 모델에 가깝다.

## TCP/IP Model
- answer: 실제 인터넷 프로토콜 구조를 설명하는 계층 모델
- detail: 보통 네트워크 접근, 인터넷, 전송, 응용 계층으로 이해한다. 웹 요청 흐름을 설명할 때 OSI보다 실제 프로토콜과 직접 연결하기 쉽다.

## Encapsulation
- answer: 상위 계층 데이터에 하위 계층 제어 정보를 붙여 내려보내는 과정
- detail: 캡슐화는 송신 측에서 일어나고, 수신 측은 반대로 각 계층의 정보를 해석하며 제거한다.

## Frame
- answer: 데이터 링크 계층에서 다루는 데이터 단위
- detail: 프레임은 같은 네트워크 안에서 장치 간 전달을 다룰 때 사용된다. MAC 주소와 관련된 흐름에서 자주 등장한다.

## Packet
- answer: 네트워크 계층에서 목적지까지 전달되는 데이터 단위
- detail: 패킷은 IP 주소와 라우팅을 통해 네트워크 사이를 이동한다. 목적지까지의 경로 선택과 관련이 깊다.

## Segment
- answer: TCP에서 애플리케이션 데이터를 나누어 보내는 단위
- detail: TCP 세그먼트는 순서 번호와 ACK를 이용해 손실 감지, 재전송, 순서 보장을 수행하는 데 사용된다.

## Datagram
- answer: UDP에서 독립적으로 전송되는 데이터 단위
- detail: UDP 데이터그램은 연결 수립 없이 전송된다. 순서 보장이나 재전송은 기본으로 제공하지 않는다.

## TCP
- answer: 신뢰성 있는 연결 기반 전송을 제공하는 프로토콜
- detail: Transmission Control Protocol의 줄임말이다. 연결 수립, 순서 보장, 재전송, 흐름 제어, 혼잡 제어를 제공한다.

## UDP
- answer: 연결 수립 없이 가볍게 데이터를 보내는 전송 프로토콜
- detail: User Datagram Protocol의 줄임말이다. 지연이 중요한 실시간 통신이나 DNS 질의처럼 빠른 요청에 자주 쓰인다.

## Flow Control
- answer: 수신자가 처리할 수 있는 양에 맞춰 송신 속도를 조절하는 기능
- detail: 흐름 제어는 수신 측 버퍼가 넘치지 않도록 돕는다. TCP 신뢰성 메커니즘의 한 부분으로 이해할 수 있다.

## Congestion Control
- answer: 네트워크 혼잡을 줄이기 위해 전송량을 조절하는 기능
- detail: 혼잡 제어는 수신자뿐 아니라 네트워크 전체 상태를 고려한다. 네트워크가 과부하되지 않도록 송신량을 조절한다.

## QUIC
- answer: UDP 위에서 연결 관리와 암호화 등을 제공하는 현대 전송 프로토콜
- detail: QUIC은 UDP를 기반으로 하면서도 재전송, 암호화, 연결 관리를 프로토콜 내부에서 제공한다. HTTP/3의 기반으로 쓰인다.

## Sequence Number
- answer: TCP 바이트 스트림의 순서를 추적하기 위한 번호
- detail: 시퀀스 번호를 통해 TCP는 데이터가 나뉘거나 순서가 바뀌어 도착해도 올바른 순서로 재조립할 수 있다.

## Acknowledgment Number
- answer: TCP에서 다음에 기대하는 데이터 위치를 알려주는 번호
- detail: ACK 번호는 어디까지 받았는지를 간접적으로 표현한다. 손실 감지와 재전송 판단에 사용된다.

## SYN_SENT
- answer: 클라이언트가 SYN을 보내고 SYN-ACK를 기다리는 TCP 상태
- detail: 3-way handshake의 첫 단계 이후 클라이언트 쪽에서 볼 수 있는 상태다.

## SYN_RECEIVED
- answer: 서버가 SYN을 받고 SYN-ACK를 보낸 뒤 ACK를 기다리는 TCP 상태
- detail: 서버가 클라이언트의 연결 요청을 받았지만 아직 연결 수립이 완전히 끝나지 않은 상태다.

## ESTABLISHED
- answer: TCP 연결이 수립되어 데이터를 주고받을 수 있는 상태
- detail: 3-way handshake가 완료되면 양쪽은 ESTABLISHED 상태가 되고 애플리케이션 데이터 전송을 시작할 수 있다.

## FIN_WAIT_1
- answer: 능동 종료자가 FIN을 보내고 ACK를 기다리는 상태
- detail: TCP 연결 종료를 먼저 시작한 쪽에서 나타난다. 상대가 FIN을 확인하면 다음 종료 단계로 이동한다.

## FIN_WAIT_2
- answer: 능동 종료자가 자신의 FIN에 대한 ACK를 받고 상대의 FIN을 기다리는 상태
- detail: 한쪽 방향 전송은 닫혔지만, 반대쪽이 아직 남은 데이터를 보낼 수 있는 구간이다.

## CLOSE_WAIT
- answer: 상대의 FIN을 받고 애플리케이션 종료 처리를 기다리는 상태
- detail: CLOSE_WAIT가 오래 남아 있으면 애플리케이션이 소켓을 제대로 닫지 않았을 가능성이 있다.

## LAST_ACK
- answer: 수동 종료자가 FIN을 보낸 뒤 마지막 ACK를 기다리는 상태
- detail: 상대가 마지막 ACK를 보내면 수동 종료자도 연결을 완전히 닫을 수 있다.

## Half-close
- answer: TCP 연결에서 한쪽 방향 전송만 먼저 닫힌 상태
- detail: 한쪽은 더 이상 보낼 데이터가 없지만, 반대쪽은 아직 데이터를 보낼 수 있다. TCP 연결 종료가 4단계인 이유와 관련된다.

## 4-tuple
- answer: TCP 연결을 식별하는 네 가지 값의 조합
- detail: 클라이언트 IP, 클라이언트 포트, 서버 IP, 서버 포트로 구성된다. 같은 연결의 지연 패킷을 구분할 때 중요하다.

## HTTP Method
- answer: HTTP 요청이 리소스에 어떤 행위를 원하는지 나타내는 값
- detail: GET, POST, PUT, PATCH, DELETE 등이 대표적이다. REST API에서는 URI가 리소스를, 메서드가 행위를 표현한다.

## GET
- answer: 리소스 조회를 요청하는 HTTP 메서드
- detail: GET은 안전한 메서드로 분류되며, 같은 요청이 서버 상태를 바꾸지 않는 것이 원칙이다.

## POST
- answer: 서버에 생성이나 처리를 요청하는 HTTP 메서드
- detail: POST는 제출, 생성, 실행처럼 결과가 매번 달라질 수 있는 처리에 자주 사용된다.

## PUT
- answer: 리소스 전체 교체나 지정 위치 저장에 주로 쓰이는 HTTP 메서드
- detail: PUT은 보통 같은 요청을 여러 번 보내도 최종 상태가 같도록 멱등하게 설계한다.

## PATCH
- answer: 리소스의 일부 수정을 표현하는 HTTP 메서드
- detail: PATCH는 전체 교체보다 부분 변경에 가깝다. 변경할 필드만 전달하는 API에서 자주 사용된다.

## DELETE
- answer: 리소스 삭제를 요청하는 HTTP 메서드
- detail: DELETE는 보통 멱등하게 설계한다. 같은 삭제 요청을 반복해도 최종적으로 리소스가 없는 상태는 같다.

## OPTIONS
- answer: 서버가 지원하는 메서드나 요청 가능 조건을 확인하는 HTTP 메서드
- detail: CORS preflight에서 브라우저가 실제 요청 전에 허용 여부를 확인할 때 OPTIONS 요청을 보낼 수 있다.

## Safe Method
- answer: 서버 상태를 바꾸지 않아야 하는 HTTP 메서드 성질
- detail: GET, HEAD 같은 조회 계열 메서드가 대표적이다. 안전하다는 말은 읽기 동작이어야 한다는 뜻이지 보안상 안전하다는 뜻은 아니다.

## Idempotent
- answer: 같은 요청을 여러 번 보내도 최종 상태가 같은 성질
- detail: 멱등성이라고도 부른다. PUT과 DELETE는 보통 멱등하게 설계하고, POST는 멱등하지 않을 수 있다.

## HTTP Request
- answer: 클라이언트가 서버에 보내는 HTTP 메시지
- detail: 메서드, 경로, 헤더, 본문 등을 포함할 수 있다. 쿠키나 인증 헤더 같은 메타데이터도 함께 전달될 수 있다.

## HTTP Response
- answer: 서버가 클라이언트 요청에 대해 돌려주는 HTTP 메시지
- detail: 상태 코드, 헤더, 본문으로 구성된다. 브라우저는 응답을 바탕으로 렌더링, 캐시, 쿠키 저장 등을 처리한다.

## Status Code
- answer: HTTP 응답 결과의 의미를 숫자로 표현한 값
- detail: 2xx는 성공, 3xx는 리다이렉트, 4xx는 클라이언트 오류, 5xx는 서버 오류 계열로 이해할 수 있다.

## Header
- answer: HTTP 요청이나 응답에 붙는 부가 정보
- detail: 헤더에는 콘텐츠 타입, 캐시 정책, 쿠키, 인증 정보 등 본문 해석과 처리에 필요한 메타데이터가 들어갈 수 있다.

## Cache-Control
- answer: HTTP 캐시 동작 방식을 지시하는 헤더
- detail: 응답을 얼마나 캐시할지, 재검증이 필요한지 등을 표현한다. 적절한 캐시는 성능과 트래픽 효율을 높인다.

## REST
- answer: 리소스 중심으로 API를 설계하는 아키텍처 스타일
- detail: Representational State Transfer의 줄임말이다. URI로 리소스를 식별하고 HTTP 메서드로 행위를 표현하는 방식이 대표적이다.

## RESTful
- answer: REST 원칙을 비교적 잘 따르는 API를 가리키는 표현
- detail: 절대적인 인증 마크라기보다 REST 제약과 설계 원칙을 얼마나 일관되게 지키는지에 가까운 말이다.

## Resource
- answer: API가 다루는 대상이나 개념
- detail: 사용자, 게시글, 댓글 같은 명사형 대상이 리소스가 될 수 있다. REST에서는 URI로 리소스를 식별한다.

## Representation
- answer: 리소스의 현재 상태를 JSON이나 HTML 같은 형태로 표현한 결과
- detail: 클라이언트와 서버는 리소스 자체를 직접 주고받는 것이 아니라, 리소스의 표현을 주고받는다.

## Statelessness
- answer: 각 요청이 필요한 정보를 스스로 포함해야 한다는 제약
- detail: 무상태성은 서버가 이전 요청 문맥에 의존하지 않도록 만든다. 서버 확장과 장애 대응을 단순하게 하는 데 도움이 된다.

## Origin
- answer: 프로토콜, 호스트, 포트의 조합
- detail: 세 요소 중 하나라도 다르면 브라우저는 다른 출처로 본다. CORS와 Same-Origin Policy를 이해할 때 핵심이 된다.

## Same-Origin Policy
- answer: 다른 출처의 리소스 접근을 기본적으로 제한하는 브라우저 보안 정책
- detail: 악성 스크립트가 사용자의 인증 정보를 이용해 임의 요청을 남용하지 못하게 돕는다.

## Access-Control-Allow-Origin
- answer: 어떤 출처의 브라우저 요청을 허용할지 알려주는 CORS 응답 헤더
- detail: 서버가 이 헤더를 통해 허용 출처를 명시하면 브라우저가 교차 출처 응답 노출 여부를 판단한다.

## Access-Control-Allow-Methods
- answer: CORS 요청에서 허용할 HTTP 메서드를 알려주는 응답 헤더
- detail: preflight 응답에서 브라우저가 실제 요청 메서드를 보내도 되는지 판단하는 데 사용된다.

## Access-Control-Allow-Headers
- answer: CORS 요청에서 허용할 요청 헤더를 알려주는 응답 헤더
- detail: 커스텀 헤더나 인증 헤더를 사용할 때 preflight 단계에서 확인될 수 있다.

## Access-Control-Allow-Credentials
- answer: CORS 요청에서 쿠키 같은 인증 정보를 포함해도 되는지 알려주는 응답 헤더
- detail: credentials 요청에서는 이 값이 true여야 하며, 보통 와일드카드 origin과 함께 사용할 수 없다.

## Credentials
- answer: 요청에 포함될 수 있는 사용자 인증 관련 정보
- detail: 쿠키, 인증 헤더, TLS 클라이언트 인증서 등이 포함된다. CORS에서는 credentials 요청을 더 엄격하게 다룬다.

## Cookie
- answer: 브라우저가 저장하고 요청에 함께 보낼 수 있는 작은 데이터
- detail: 쿠키는 세션 ID, 사용자 설정, 추적 정보 등에 쓰인다. 보안 속성 설정이 중요하다.

## Session
- answer: 서버가 사용자 상태를 저장하고 관리하는 방식
- detail: 보통 브라우저에는 세션 ID만 쿠키로 저장하고 실제 사용자 정보는 서버의 세션 저장소에 둔다.

## Session ID
- answer: 서버에 저장된 세션을 찾기 위한 식별자
- detail: 세션 기반 로그인에서는 브라우저가 세션 ID를 쿠키로 보내고, 서버는 이 값으로 사용자 상태를 조회한다.

## Set-Cookie
- answer: 서버가 브라우저에 쿠키 저장을 요청하는 응답 헤더
- detail: 서버는 Set-Cookie 헤더로 쿠키 값과 만료 시간, 보안 속성 등을 함께 전달할 수 있다.

## Cookie Header
- answer: 브라우저가 저장된 쿠키를 서버 요청에 담아 보낼 때 사용하는 헤더
- detail: 서버는 Cookie 헤더를 보고 세션 ID나 사용자 설정 같은 정보를 확인할 수 있다.

## HttpOnly
- answer: JavaScript에서 쿠키에 접근하지 못하게 제한하는 쿠키 속성
- detail: HttpOnly를 설정하면 XSS 상황에서 스크립트가 쿠키 값을 직접 읽는 위험을 줄이는 데 도움이 된다.

## Secure
- answer: HTTPS 요청에서만 쿠키를 전송하도록 제한하는 쿠키 속성
- detail: Secure 속성은 평문 HTTP 연결에서 쿠키가 전송되는 것을 막아 전송 중 노출 위험을 줄인다.

## SameSite
- answer: 교차 사이트 요청에서 쿠키 전송 여부를 제한하는 쿠키 속성
- detail: SameSite는 CSRF 위험을 줄이는 데 도움이 된다. Strict, Lax, None 같은 정책 값이 있다.

## CSRF
- answer: 사용자의 인증 상태를 악용해 원치 않는 요청을 보내게 하는 공격
- detail: Cross-Site Request Forgery의 줄임말이다. SameSite 쿠키, CSRF 토큰, 중요한 요청의 추가 검증으로 방어할 수 있다.

## Symmetric Key
- answer: 암호화와 복호화에 같은 키를 사용하는 방식의 키
- detail: 대칭키는 연산이 빠르기 때문에 실제 데이터 암호화에 적합하다. TLS에서는 세션 키가 실제 HTTP 데이터를 암호화한다.

## Asymmetric Key
- answer: 공개키와 개인키 한 쌍으로 이루어진 암호화 방식의 키
- detail: 비대칭키는 키를 직접 공유하지 않고도 안전한 통신을 시작하거나 상대를 인증하는 데 유용하다.

## Certificate
- answer: 서버의 신원을 확인하기 위한 공개키 기반 문서
- detail: 인증서는 도메인과 공개키 정보를 담고, 신뢰할 수 있는 인증기관의 서명으로 서버 신원을 검증할 수 있게 한다.

## Digital Signature
- answer: 데이터의 출처와 변조 여부를 확인하기 위한 서명
- detail: 전자서명은 개인키로 만들고 공개키로 검증할 수 있다. 인증서 검증과 무결성 확인에 사용된다.

## Key Exchange
- answer: 통신 양쪽이 안전하게 공통 비밀을 만드는 과정
- detail: TLS에서는 비대칭키 기반 절차를 이용해 이후 실제 데이터 암호화에 사용할 세션 키를 만든다.

## Encryption
- answer: 데이터를 알아보기 어렵게 바꾸어 보호하는 과정
- detail: 암호화된 데이터는 올바른 키가 있어야 원래 의미로 복호화할 수 있다. HTTPS에서는 통신 내용을 보호하는 핵심 기능이다.

## Integrity
- answer: 데이터가 전송 중 변조되지 않았음을 보장하는 성질
- detail: 무결성 검사는 중간에서 데이터가 바뀌었는지 감지하는 데 사용된다. HTTPS의 핵심 보안 가치 중 하나다.

## Authentication
- answer: 통신 상대가 누구인지 확인하는 과정
- detail: HTTPS에서는 인증서를 통해 서버 신원을 확인한다. 인증은 암호화와 함께 안전한 통신의 중요한 축이다.

## Rendering
- answer: 브라우저가 응답 리소스를 해석해 화면을 구성하는 과정
- detail: HTML, CSS, JavaScript, 이미지 같은 리소스를 처리하며 사용자에게 보이는 화면을 만든다.
