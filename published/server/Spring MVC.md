> 요청은 Dispatcher Servlet → HandlerMapping → HandlerAdapter → Controller 순으로 처리된다. ArgumentResolver가 파라미터를 변환하고, Filter는 서블릿 레벨, Interceptor는 Spring MVC 레벨에서 동작한다.

## 정의
- Dispatcher Servlet: Spring MVC의 Front Controller. 모든 요청을 받아 핸들러를 찾고 응답을 조율한다.
- HandlerAdapter: 다양한 핸들러 타입(@RequestMapping, HttpRequestHandler 등)을 동일한 방식으로 호출하기 위한 어댑터. 유연성과 확장성 확보가 목적.
- ArgumentResolver: 컨트롤러 메서드 파라미터를 HTTP 요청으로부터 변환하는 컴포넌트. 내부적으로 HttpMessageConverter를 사용한다.
- Filter: 서블릿 컨테이너 레벨에서 동작. 핸들러 정보를 알 수 없어 인증·보안 처리에 주로 사용.
- Interceptor: Spring MVC 레벨에서 동작. 핸들러를 알 수 있어 인가 로직에 적합. preHandle / postHandle / afterCompletion 세 시점 제공.

## 핵심 포인트
- HandlerAdapter를 두는 이유: 핸들러 타입마다 호출 방식이 달라 어댑터가 이를 추상화해 유연성을 확보한다.
- ArgumentResolver가 @RequestBody, @PathVariable 등 어노테이션을 리플렉션으로 분석해 HttpMessageConverter로 변환한다.
- postHandle은 컨트롤러가 정상 리턴한 경우에만 호출되고, afterCompletion은 예외 여부와 무관하게 항상 호출된다.
- Filter는 Spring Context 밖에서 동작하므로 Spring 빈 주입이 기본적으로 어렵다.
- @ControllerAdvice는 AOP 프록시가 아닌 ExceptionHandlerExceptionResolver가 리플렉션으로 처리한다.

## 면접 질문
- Dispatcher Servlet이 요청을 처리하는 흐름을 설명해보세요.
- Filter와 Interceptor의 차이는 무엇인가요?
- HandlerAdapter를 별도로 두는 이유는 무엇인가요?

## 확인 문제
- ArgumentResolver 내부에서 어떤 컴포넌트가 실제 변환을 담당하나요?
- postHandle이 호출되지 않는 경우는 언제인가요?
- afterCompletion에서 응답을 조작할 수 있나요?

## 키워드
Dispatcher Servlet, HandlerAdapter, ArgumentResolver, Filter, Interceptor, HttpMessageConverter, Spring MVC, ControllerAdvice
