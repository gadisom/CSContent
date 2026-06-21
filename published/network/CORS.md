> [CORS는 브라우저가 다른 출처의 자원 요청을 제한하는 Same-Origin Policy를 서버의 허용 정책으로 안전하게 완화하는 메커니즘이다.]{.lead}

## 정의
- [Origin]{.term}은 프로토콜, 호스트, 포트의 조합이다. `https://example.com:443`처럼 세 요소가 같아야 같은 출처로 본다.
- [Same-Origin Policy]{.term}는 브라우저가 기본적으로 다른 출처의 리소스 접근을 제한하는 보안 정책이다. 악성 스크립트가 사용자의 인증 정보를 이용해 임의 요청을 남용하지 못하게 돕는다.
- [CORS]{.term}는 서버가 특정 출처의 접근을 허용한다는 HTTP 헤더를 보내면 브라우저가 교차 출처 제한을 완화하도록 만든 규칙이다.
- [Access-Control-Allow-Origin]{.term}은 어떤 출처의 요청을 허용할지 알려주는 대표적인 CORS 응답 헤더다.
- [Preflight]{.term}는 실제 요청 전에 브라우저가 OPTIONS 요청으로 서버의 허용 여부를 먼저 확인하는 절차다.
- [Credentials]{.term}는 쿠키, 인증 헤더, TLS 클라이언트 인증서처럼 사용자 인증과 관련된 정보를 뜻한다. credentials 요청은 출처 허용과 인증 정보 허용을 더 엄격하게 다룬다.
- CORS 실패는 서버가 응답을 아예 만들지 못했다는 뜻이 아니라, [브라우저가 응답을 프론트엔드 코드에 넘기지 않고 차단했다는 의미]{.warning}에 가깝다.

## 핵심 포인트
- [CORS는 브라우저 보안 정책과 관련된 메커니즘]{.accent}이다. 서버 간 통신이나 curl 요청에서는 같은 방식의 브라우저 CORS 차단이 발생하지 않는다.
- 서버는 [Access-Control-Allow-Origin]{.term}, [Access-Control-Allow-Methods]{.term}, [Access-Control-Allow-Headers]{.term} 같은 헤더로 허용 범위를 명시한다.
- preflight는 모든 요청에서 발생하지 않는다. 단순 요청이 아니거나 커스텀 헤더, 일부 메서드, 특정 Content-Type이 포함되면 브라우저가 먼저 OPTIONS 요청을 보낼 수 있다.
- credentials를 포함한 요청에서는 `Access-Control-Allow-Credentials: true`가 필요하고, 이때 `Access-Control-Allow-Origin`에 와일드카드 `*`를 사용할 수 없다.
- [CORS를 프론트엔드에서 우회하는 것이 아니라, 서버가 허용할 출처와 메서드와 헤더를 명확히 정해야 한다.]{.danger}
- 개발 환경에서는 `localhost` 포트가 다르면 다른 출처가 된다. 예를 들어 `localhost:3000`과 `localhost:8080`은 서로 다른 origin이다.
- CORS 허용은 브라우저 접근 제어를 완화하는 설정이지, 인증과 권한 검사를 대체하지 않는다.

## 면접 질문
- CORS가 무엇인지 설명해보세요.
- 왜 브라우저에서만 CORS 문제가 두드러지나요?
- Same-Origin Policy와 CORS는 어떤 관계인가요?
- preflight 요청은 언제 발생하고 어떤 역할을 하나요?
- credentials 요청에서 와일드카드 origin을 사용할 수 없는 이유는 무엇인가요?

## 확인 문제
- CORS는 브라우저 정책과 관련이 있을까?
- 서버 간 통신에서도 동일하게 CORS 에러가 핵심 이슈일까?
- 프로토콜, 호스트, 포트 중 하나라도 다르면 다른 origin으로 볼 수 있을까?
- preflight는 실제 요청 전에 OPTIONS로 허용 여부를 확인할 수 있을까?
- credentials 요청에서 `Access-Control-Allow-Origin: *`를 그대로 쓰는 것은 적절할까?
- CORS 설정이 인증과 권한 검사를 완전히 대체할 수 있을까?

## 키워드
CORS, Same-Origin Policy, Origin, Access-Control-Allow-Origin, Access-Control-Allow-Methods, Access-Control-Allow-Headers, Access-Control-Allow-Credentials, preflight, OPTIONS, credentials, 브라우저 보안

## 연관 콘텐츠
- [[HTTP와 HTTPS]]
- [[HTTP 메서드]]
- [[REST와 RESTful]]
