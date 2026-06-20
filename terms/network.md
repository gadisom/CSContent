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
