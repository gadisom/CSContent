---
category: server
tag: Spring MVC
---

#### OX | [625]
Filter는 Spring MVC 레벨에서 동작하므로 핸들러(Controller) 정보를 알 수 있다.
> X
> Filter는 서블릿 컨테이너 레벨에서 동작해 핸들러 정보를 알 수 없다. 핸들러 정보를 알 수 있는 것은 Spring MVC 레벨에서 동작하는 Interceptor다.

#### OX | [626]
afterCompletion은 컨트롤러에서 예외가 발생해도 반드시 호출된다.
> O
> afterCompletion은 예외 발생 여부와 무관하게 항상 호출된다. postHandle은 컨트롤러가 정상 리턴한 경우에만 호출된다.

#### 빈칸 | [627]
Spring MVC에서 @RequestBody를 자바 객체로 변환하는 컴포넌트는 ___ 이다.
> HttpMessageConverter
> ArgumentResolver가 어노테이션을 분석하고 내부적으로 HttpMessageConverter를 호출해 HTTP 요청 본문을 자바 객체로 변환한다.

#### 빈칸 | [628]
Dispatcher Servlet에서 다양한 핸들러 타입을 동일한 방식으로 호출하기 위한 컴포넌트는 ___ 이다.
> HandlerAdapter
> @RequestMapping, Controller 인터페이스, HttpRequestHandler 등 타입마다 호출 방식이 다르므로 HandlerAdapter가 이를 추상화해 유연성을 확보한다.

#### 객관식 | [629]
Interceptor의 postHandle이 호출되지 않는 경우는?
1. View 렌더링 이후
2. afterCompletion 이후
3. ✅ 컨트롤러에서 예외가 발생한 경우
4. preHandle이 true를 반환한 경우
> postHandle은 컨트롤러 메서드가 정상적으로 리턴한 경우에만 호출된다. 예외가 발생하면 호출되지 않는다.

#### 객관식 | [630]
Filter와 Interceptor를 각각 어떤 용도에 사용하는 것이 적합한가?
1. Filter: 인가, Interceptor: 인증
2. ✅ Filter: 인증·보안, Interceptor: 인가·로그인 체크·공통 로깅
3. 둘 다 동일한 용도로 사용 가능하다
4. Filter: 로깅, Interceptor: 트랜잭션 관리
> Filter는 핸들러 정보가 없어 URL 기반 처리에 적합하고, Interceptor는 Controller 정보를 알 수 있어 Controller별 접근 권한 확인에 유리하다.
