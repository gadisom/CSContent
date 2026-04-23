# CSContent Wiki — 인덱스

> Claude가 자동으로 유지한다. 새 콘텐츠 생성 전 반드시 이 파일을 읽어 slug 중복을 확인한다.

마지막 업데이트: 2026-04-24

---

## display_order 현황 (1000 단위 증분)

| category | 현재 마지막 | 다음 신규 |
|----------|-----------|---------|
| data-structure | 6001 (ds-graph-basics) | 7001 |
| algorithms | 8001 (algo-dp-basics) | 9001 |
| operating-system | 11001 (os-context-switching) | 12001 |
| database | 11001 (db-rdbms-vs-nosql) | 12001 |
| network | 10001 (net-rest-restful) | 11001 |

---

## 기존 콘텐츠 (DB 동기화 기준: 2026-04-24) — 총 46개

### data-structure (6개)
| slug | title | display_order |
|------|-------|--------------|
| ds-array-vs-linked-list | 배열과 연결리스트의 차이 | 1001 |
| ds-stack-vs-queue | 스택과 큐의 차이 | 2001 |
| ds-hash-table-and-collision | 해시테이블과 충돌 해결 | 3001 |
| ds-tree-vs-bst | 트리와 이진 탐색 트리(BST) | 4001 |
| ds-heap-and-priority-queue | 힙과 우선순위큐 | 5001 |
| ds-graph-basics | 그래프의 기본 개념과 표현 방식 | 6001 |

### algorithms (8개)
| slug | title | display_order |
|------|-------|--------------|
| alg-time-complexity | 시간복잡도와 공간복잡도 | 1001 |
| algo-sorting-overview | 정렬 알고리즘 비교 | 2001 |
| algo-search-strategy | 탐색 문제를 푸는 관점 | 3001 |
| algo-graph-bfs-dfs | BFS와 DFS의 차이 | 4001 |
| algo-binary-search | 이진 탐색의 전제와 활용 | 5001 |
| algo-recursion-backtracking | 재귀와 백트래킹 | 6001 |
| algo-greedy-basics | 그리디 알고리즘의 조건 | 7001 |
| algo-dp-basics | 동적 계획법의 핵심 아이디어 | 8001 |

### operating-system (11개)
| slug | title | display_order |
|------|-------|--------------|
| os-process-vs-thread | 프로세스와 스레드의 차이 | 1001 |
| os-multi-process-vs-multi-thread | 멀티프로세스와 멀티스레드 비교 | 2001 |
| os-ipc-overview | IPC와 동기화가 필요한 이유 | 3001 |
| os-mutex-semaphore-monitor | 뮤텍스, 세마포어, 모니터 비교 | 4001 |
| os-deadlock-os | 운영체제에서의 데드락 | 5001 |
| os-cpu-scheduling | CPU 스케줄링의 기본 개념 | 6001 |
| os-memory-management | 운영체제의 메모리 관리 | 7001 |
| os-paging-vs-segmentation | 페이징과 세그멘테이션 비교 | 8001 |
| os-virtual-memory | 가상 메모리와 페이지 교체 | 9001 |
| os-cache-locality | 캐시 메모리와 지역성 | 10001 |
| os-context-switching | 컨텍스트 스위칭과 오버헤드 | 11001 |

### database (12개)
| slug | title | display_order |
|------|-------|--------------|
| db-database-basics | 데이터베이스를 사용하는 이유 | 1001 |
| db-key-and-relationship | 기본키, 외래키와 관계 설계 | 2001 |
| db-normalization | 정규화의 목적과 단계 | 3001 |
| db-index-basics | 인덱스의 역할과 설계 기준 | 4001 |
| db-index-btree-vs-hash | DB 인덱스가 해시보다 B+트리를 많이 쓰는 이유 | 4002 |
| db-join-basics | 조인의 개념과 종류 | 5001 |
| db-transaction-basics | 트랜잭션과 ACID | 6001 |
| db-isolation-and-lock | 격리 수준과 락 | 7001 |
| db-transaction-deadlock | 트랜잭션과 데드락 | 8001 |
| db-statement-vs-prepared | Statement와 Prepared Statement의 차이 | 9001 |
| db-sql-injection | SQL Injection의 원리와 대응 | 10001 |
| db-rdbms-vs-nosql | RDBMS와 NoSQL 비교 | 11001 |

### network (10개)
| slug | title | display_order |
|------|-------|--------------|
| net-osi-vs-tcpip | OSI 7계층과 TCP/IP 모델 | 1001 |
| net-tcp-vs-udp | TCP와 UDP 비교 | 2001 |
| net-three-way-four-way | 3-way handshake와 4-way handshake | 3001 |
| net-http-vs-https | HTTP와 HTTPS의 차이 | 4001 |
| net-get-vs-post | GET과 POST의 차이 | 5001 |
| net-cookie-vs-session | 쿠키와 세션의 차이 | 6001 |
| net-dns-resolution | DNS 조회 과정 | 7001 |
| net-cors-basics | CORS의 목적과 동작 | 8001 |
| net-web-request-flow | 브라우저에 URL을 입력했을 때의 흐름 | 9001 |
| net-rest-restful | REST와 RESTful API의 개념 | 10001 |

---

## Wiki 문서 현황

### Concepts (개념 문서)
| 파일 | 상태 |
|------|------|
| [[concepts/ds-array-vs-linked-list]] | 작성됨 |

### Content (앱 전달용 JSON)
| 파일 | slug | status |
|------|------|--------|
| [[content/ds-array-vs-linked-list]] | ds-array-vs-linked-list | published |

---

## Meta
| 파일 | 요약 |
|------|------|
| [[meta/app-features]] | 앱 데이터 모델 및 기능 현황 |
| [[meta/content-guidelines]] | 콘텐츠 제작 가이드라인 |
