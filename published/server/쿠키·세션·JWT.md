> 쿠키는 클라이언트, 세션은 서버에 상태를 저장한다. JWT는 무상태로 서버 부담이 없지만 탈취 대응을 위해 Refresh Token을 함께 운용한다.

## 정의
- 쿠키: 클라이언트 로컬에 저장되는 키-값 데이터 파일. HttpOnly(JS 접근 차단), Secure(HTTPS만 전송)로 보안 강화. 세션 쿠키(브라우저 종료 시 삭제)와 지속 쿠키(만료일까지 유지)로 나뉜다.
- 세션: 서버 측에서 세션 ID로 사용자 상태를 관리. 서버가 임의로 세션을 폐기할 수 있어 보안이 우수하지만, Scale-out 시 외부 저장소가 필요하다.
- JWT: Header(서명 알고리즘).Payload(클레임).Signature(비밀키 서명) 구조. 무상태로 서버가 상태를 저장하지 않는다. Payload는 Base64 인코딩이라 민감 정보를 담으면 안 된다.
- Refresh Token: ATK 유효시간을 짧게 설정하고 RTK로 재발급해 탈취 피해를 최소화하는 전략. RTK는 서버에 저장해 부분적으로 상태를 가진다.

## 핵심 포인트
- 분산 환경에서 세션은 Redis 같은 인메모리 캐시를 외부 저장소로 사용하는 것이 적합하다. RDB는 I/O 비용이 크다.
- JWT Signature는 서버만 아는 비밀키로 서명하므로 위변조 여부를 서버가 확인할 수 있다.
- RTK 탈취 가능성이 있어 JWT 방식도 완벽한 보안은 아니다.
- 쿠키는 조작·탈취가 가능하므로 HttpOnly + Secure 설정이 권장된다.

## 면접 질문
- 쿠키와 세션의 차이는 무엇인가요?
- 분산 환경에서 세션을 어떻게 관리하나요?
- Access Token과 Refresh Token을 분리하는 이유는?

## 확인 문제
- HttpOnly 쿠키 설정의 효과는?
- JWT Payload가 암호화되지 않는다는 점에서 주의해야 할 것은?
- Scale-out 환경에서 세션 저장에 RDB 대신 Redis를 쓰는 이유는?

## 키워드
쿠키, 세션, JWT, Refresh Token, HttpOnly, Secure, Redis, Scale-out, Base64, 무상태
