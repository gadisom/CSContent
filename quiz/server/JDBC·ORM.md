---
category: server
tag: 데이터 접근
---

#### OX | [649]
JPA는 JDBC를 대체하는 기술로, JPA를 사용하면 JDBC가 필요 없다.
> X
> JPA는 내부적으로 JDBC를 사용한다. JPA는 JDBC 위에서 객체-테이블 매핑을 추상화한 상위 기술이다.

#### OX | [650]
DataSource는 커넥션 획득 방법을 추상화해 DriverManager와 HikariCP를 동일한 인터페이스로 사용할 수 있게 한다.
> O
> DataSource 인터페이스를 통해 커넥션을 획득하면, 구현체(DriverManager/HikariCP)를 교체해도 코드 변경이 최소화된다.

#### 빈칸 | [651]
Spring Boot에서 기본으로 사용하는 커넥션 풀 구현체는 ___ 이다.
> HikariCP
> HikariCP는 Spring Boot 2.x부터 기본 커넥션 풀로 채택됐다. 성능과 안정성이 뛰어나 업계 표준으로 사용된다.

#### 빈칸 | [652]
같은 트랜잭션 내에서 동일 커넥션을 유지하기 위해 ThreadLocal을 사용하는 컴포넌트는 ___ 이다.
> 트랜잭션 동기화 매니저
> 트랜잭션 동기화 매니저는 ThreadLocal에 커넥션을 저장해 같은 스레드에서 동일 커넥션이 재사용되도록 보장한다. 메서드 간 커넥션을 매개변수로 넘기지 않아도 된다.

#### 객관식 | [653]
SQL Mapper와 ORM의 차이로 올바른 것은?
1. SQL Mapper는 SQL이 불필요하고, ORM은 SQL을 직접 작성한다
2. ✅ SQL Mapper는 개발자가 SQL을 직접 작성하고, ORM은 객체-테이블 매핑으로 SQL을 자동 생성한다
3. 둘 다 SQL을 자동 생성한다
4. SQL Mapper가 ORM보다 생산성이 항상 높다
> MyBatis 같은 SQL Mapper는 SQL을 직접 제어할 수 있어 복잡한 쿼리에 유리하다. JPA 같은 ORM은 반복 CRUD를 자동화하지만 복잡한 쿼리는 JPQL이 필요하다.

#### 객관식 | [654]
REQUIRED 트랜잭션 전파에서 내부 논리 트랜잭션이 롤백되면?
1. 내부 트랜잭션만 롤백되고 외부는 영향이 없다
2. 외부 트랜잭션만 롤백된다
3. ✅ 물리 트랜잭션 전체가 롤백된다
4. 아무것도 롤백되지 않는다
> REQUIRED 전파에서 내부 트랜잭션이 rollbackOnly를 마킹하면 물리 트랜잭션 커밋 시 전체 롤백이 발생한다. 논리 트랜잭션 하나라도 실패하면 물리 트랜잭션 전체가 롤백된다.
