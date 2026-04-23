---
tags: [topic]
concept_count: 0
content_count: 0
coverage: 0%
---

# 시스템 설계 (System Design)

## 개요
대규모 소프트웨어 시스템을 설계하는 방법론. 확장성, 가용성, 일관성, 성능 간의 트레이드오프를 다룬다.
시니어 개발자 면접의 핵심 영역.

---

## 핵심 개념 목록

### 기초 개념
- [ ] 수평 확장 vs 수직 확장
- [ ] 로드 밸런싱
- [ ] CAP 정리
- [ ] 일관성 vs 가용성 트레이드오프

### 캐싱
- [ ] 캐시 전략 (Cache-aside, Write-through, Write-back)
- [ ] CDN
- [ ] Redis vs Memcached

### 데이터 처리
- [ ] 메시지 큐 (Kafka, RabbitMQ)
- [ ] 배치 처리 vs 스트림 처리
- [ ] 데이터 파이프라인

### 분산 시스템
- [ ] 일관성 해싱 (Consistent Hashing)
- [ ] 샤딩 (Sharding)
- [ ] 복제 (Replication)
- [ ] 분산 트랜잭션

### 설계 패턴
- [ ] 마이크로서비스 vs 모노리스
- [ ] API Gateway
- [ ] Circuit Breaker

---

## 제작된 콘텐츠

*아직 없음*

---

## 우선순위 아이디어

1. CAP 정리 설명 — 직관적 예시로
2. 캐싱 전략 비교 (언제 무엇을)
3. 로드 밸런서 동작 원리 설명
4. 시스템 설계 면접 템플릿 (요구사항 → 추정 → 설계)

---

## 관련 주제
- [[topics/databases]] — 시스템 설계에서 DB 선택이 중요
- [[topics/networks]] — 분산 시스템은 네트워크 위에서 동작
- [[topics/operating-systems]] — 서버 OS 이해가 기반
