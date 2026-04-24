> JDBC는 DB 접근 표준 인터페이스이고, DataSource와 커넥션 풀로 성능을 개선하며, ORM(JPA)과 SQL Mapper(MyBatis)로 반복 SQL 문제를 해결한다.

## 정의
- JDBC: 자바에서 DB에 접속하기 위한 표준 인터페이스. DB별 드라이버가 실제 통신을 담당한다.
- SQL Mapper(JdbcTemplate, MyBatis): 개발자가 SQL을 직접 작성. 결과를 자바 객체로 매핑한다.
- ORM(JPA/Hibernate): 객체와 테이블을 자동 매핑해 반복적인 SQL 작성을 줄인다. Hibernate는 JPA의 구현체.
- DataSource: 커넥션 획득 방법을 추상화한 인터페이스. DriverManager → HikariCP 전환 시 코드 변경을 최소화한다.
- 트랜잭션 동기화 매니저: ThreadLocal로 커넥션을 동기화해 같은 트랜잭션 내에서 동일 커넥션을 유지한다.

## 핵심 포인트
- 커넥션 풀은 매번 TCP 연결 수립 비용을 줄이기 위해 등장. HikariCP가 Spring Boot 기본.
- JDBC/JPA/Hibernate마다 트랜잭션 처리 방식이 달라 Spring이 트랜잭션을 추상화했다.
- REQUIRED 전파 옵션: 논리 트랜잭션 중 하나라도 롤백하면 물리 트랜잭션도 롤백. rollbackOnly로 마킹해 처리한다.
- 트랜잭션 동기화 매니저 덕분에 메서드 간 커넥션을 매개변수로 넘기지 않아도 된다.

## 면접 질문
- JDBC와 JPA의 차이는 무엇인가요?
- DataSource 추상화가 필요한 이유는?
- 트랜잭션 동기화 매니저가 ThreadLocal을 사용하는 이유는?

## 확인 문제
- SQL Mapper와 ORM의 차이를 설명해보세요.
- HikariCP 전환 시 DataSource가 없었다면 어떤 문제가 생기나요?
- REQUIRED 전파에서 내부 트랜잭션이 롤백되면 어떻게 되나요?

## 키워드
JDBC, JPA, Hibernate, ORM, SQL Mapper, DataSource, HikariCP, 커넥션 풀, 트랜잭션 동기화, REQUIRED
