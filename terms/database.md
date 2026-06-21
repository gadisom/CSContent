---
category: database
title: 데이터베이스 단어장
---

# 데이터베이스 단어장

## RDBMS
- answer: 데이터를 테이블과 관계 중심으로 관리하는 데이터베이스 시스템
- detail: Relational Database Management System의 줄임말이다. 스키마, SQL, 트랜잭션, 관계 제약을 기반으로 데이터를 다룬다.

## NoSQL
- answer: 관계형 모델에 고정되지 않은 다양한 형태의 데이터베이스
- detail: 문서형, 키-값, 컬럼형, 그래프형 등이 있다. 유연한 스키마나 수평 확장이 필요한 상황에서 선택될 수 있다.

## Transaction
- answer: 데이터베이스에서 하나의 논리적 작업 단위
- detail: 트랜잭션은 여러 쿼리를 하나의 작업처럼 묶는다. 중간에 실패하면 전체를 되돌려 데이터 일관성을 지킨다.

## ACID
- answer: 트랜잭션이 신뢰성을 갖기 위해 만족해야 하는 네 가지 성질
- detail: Atomicity, Consistency, Isolation, Durability의 줄임말이다. 원자성, 일관성, 격리성, 지속성을 의미한다.

## Isolation Level
- answer: 동시에 실행되는 트랜잭션들이 서로 얼마나 분리되어 보이는지 정하는 수준
- detail: 격리 수준이 높을수록 이상 현상은 줄지만 동시성이 낮아질 수 있다. Read Committed, Repeatable Read, Serializable 등이 있다.

## Index
- answer: 테이블의 특정 컬럼을 빠르게 찾기 위한 보조 자료구조
- detail: 인덱스는 조회 성능을 높일 수 있지만, 삽입과 수정 시 인덱스도 함께 갱신해야 하므로 쓰기 비용이 늘 수 있다.

## Primary Key
- answer: 테이블에서 각 행을 고유하게 식별하는 키
- detail: 기본키는 중복될 수 없고 보통 NULL을 허용하지 않는다. 다른 테이블이 이 값을 참조할 수 있다.

## Foreign Key
- answer: 다른 테이블의 기본키를 참조해 관계를 표현하는 키
- detail: 외래키는 테이블 사이의 연결과 참조 무결성을 유지하는 데 사용된다.

## Join
- answer: 두 개 이상의 테이블을 관계 조건에 따라 합쳐 조회하는 연산
- detail: 조인은 정규화된 데이터를 함께 읽기 위해 사용한다. Inner Join, Left Join, Right Join 등이 있다.

## Normalization
- answer: 중복을 줄이고 데이터 일관성을 높이기 위해 테이블을 나누는 설계 과정
- detail: 정규화는 이상 현상을 줄이는 데 도움을 준다. 다만 지나친 분리는 조회 시 조인을 많이 만들 수 있다.

## Prepared Statement
- answer: SQL 구조와 값을 분리해 미리 준비한 쿼리 실행 방식
- detail: Prepared Statement는 파라미터 바인딩을 통해 SQL Injection 위험을 줄이고, 반복 실행 시 효율을 높일 수 있다.

## SQL Injection
- answer: 입력값에 악의적인 SQL을 섞어 의도하지 않은 쿼리를 실행시키는 공격
- detail: 사용자 입력을 문자열로 직접 이어 붙일 때 발생하기 쉽다. 파라미터 바인딩과 입력 검증으로 방어한다.

## Lock
- answer: 동시에 같은 데이터에 접근할 때 충돌을 막기 위한 잠금 장치
- detail: 락은 데이터 일관성을 지키지만 범위가 넓거나 오래 유지되면 대기와 데드락을 만들 수 있다.

## Deadlock
- answer: 트랜잭션들이 서로 가진 락을 기다리며 진행하지 못하는 상태
- detail: 데이터베이스는 데드락을 감지하면 보통 한 트랜잭션을 롤백해 상황을 해소한다.

## MVCC
- answer: 데이터의 여러 버전을 관리해 읽기와 쓰기의 충돌을 줄이는 방식
- detail: Multi-Version Concurrency Control의 줄임말이다. 읽는 트랜잭션이 쓰기 작업을 무조건 막지 않도록 도와 동시성을 높인다.
