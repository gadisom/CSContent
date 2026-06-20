# CSContent Wiki — 활동 로그

> append-only. 가장 최근 항목이 위에 온다.
> 파싱: `grep "^## \[" wiki/log.md | head -10`

---

## [2026-06-20] meta | terms 운영 가이드 반영
앞으로 terms 단어장은 category별 MD 파일에 answer/detail만 작성하고, sync_terms_to_supabase.py로 word_terms에 동기화하도록 AGENTS/CLAUDE/terms README 운영 가이드에 명시.
생성/변경된 파일: AGENTS.md, CLAUDE.md, terms/README.md, wiki/log.md

---

## [2026-06-20] meta | terms Supabase 동기화 자동화 추가
terms/*.md를 word_terms 테이블에 업서트하고 로컬에 없는 단어를 삭제하는 sync_terms_to_supabase.py를 추가. GitHub Actions 동기화 대상에 terms/와 terms sync 단계를 포함.
생성/변경된 파일: scripts/sync_terms_to_supabase.py, .github/workflows/sync-content.yml, wiki/log.md

---

## [2026-06-20] meta | terms 단어장 포맷 단순화
단어장 항목에서 full, related, tags 필드를 제거하고 answer/detail 중심으로 단순화. 풀네임은 필요한 경우 detail에 포함하도록 정리.
생성/변경된 파일: terms/README.md, terms/network.md, wiki/log.md

---

## [2026-06-20] meta | terms 단어장 초안 생성
앱 단어장 기능을 위한 terms/ 폴더와 네트워크 단어장 초안을 생성. 프론트 준비 전 단계이므로 Supabase 동기화 대상에는 포함하지 않음.
생성/변경된 파일: terms/README.md, terms/network.md, wiki/log.md

---

## [2026-06-20] ingest | network — DNS 보강
DNS 문서를 재귀 해석기, 루트/TLD/권한 있는 네임서버, 주요 레코드, TTL 캐시 중심으로 보강하고 조회 흐름 도식과 퀴즈 6문항을 추가.
생성/변경된 파일: published/network/DNS.md, quiz/network/DNS.md, raw/assets/dns-resolution-flow.png, wiki/log.md

---

## [2026-06-20] ingest | network — 대칭키와 비대칭키 역할 설명 보강
대칭키는 실제 데이터를 암호화하는 공통 비밀키이고, 비대칭키는 그 비밀키를 안전하게 만들기 위한 공개키·개인키 구조라는 설명을 보강.
생성/변경된 파일: published/network/대칭키와 비대칭키.md, wiki/log.md

---

## [2026-06-20] ingest | network — 대칭키와 비대칭키 이미지 추가
대칭키와 비대칭키 문서에 같은 키, 공개키·개인키 쌍, TLS 세션 키 흐름을 보여주는 단순 도식을 추가.
생성/변경된 파일: published/network/대칭키와 비대칭키.md, raw/assets/symmetric-asymmetric-key-map.png, wiki/log.md

---

## [2026-06-20] ingest | network — 대칭키와 비대칭키 신규 생성
HTTPS/TLS 이해에 필요한 대칭키·비대칭키, 공개키·개인키, 세션 키, 전자서명 개념을 독립 콘텐츠로 생성하고 퀴즈 6문항을 추가. 파일명 정렬 기준에 맞춰 display_order를 10001로 반영.
생성/변경된 파일: published/network/대칭키와 비대칭키.md, quiz/network/대칭키와 비대칭키.md, wiki/index.md, wiki/log.md

---

## [2026-06-20] ingest | network — HTTP와 HTTPS 보강
HTTP와 HTTPS 문서를 TLS의 역할, 대칭키·비대칭키, 기밀성·무결성·인증, 포트 차이 중심으로 보강하고 단순 비교 도식을 추가.
생성/변경된 파일: published/network/HTTP와 HTTPS.md, raw/assets/http-vs-https-flow.png, wiki/log.md

---

## [2026-06-20] ingest | network — HTTP 메서드 이미지 추가
HTTP 메서드 문서에 URI와 메서드의 관계를 보여주는 단순 도식을 추가.
생성/변경된 파일: published/network/HTTP 메서드.md, raw/assets/http-methods-map.png, wiki/log.md

---

## [2026-06-20] ingest | network — HTTP 메서드 보강
기존 HTTP 메서드 콘텐츠를 HTTP 메서드로 이름 정리하고, 주요 메서드와 안전성·멱등성 개념을 보강.
생성/변경된 파일: published/network/HTTP 메서드.md, published/network/HTTP와 HTTPS.md, published/network/REST와 RESTful.md, wiki/index.md, wiki/log.md

---

## [2026-06-20] ingest | network — 3-way handshake와 4-way handshake 보강
TCP 연결 수립/종료 흐름을 시퀀스 번호, ACK 번호, 상태 전이(SYN_SENT, SYN_RECEIVED, FIN_WAIT, CLOSE_WAIT, LAST_ACK, TIME_WAIT), half-close, TIME_WAIT 필요성 중심으로 보강하고 단계 흐름 이미지를 추가.
생성/변경된 파일: published/network/3-way handshake와 4-way handshake.md, raw/assets/tcp-handshake-flow.png, wiki/log.md

---

## [2026-06-18] meta | 콘텐츠 문체 규칙 추가
정의와 핵심 포인트 섹션에는 "면접에서는" 같은 면접 상황 전제 문장을 넣지 않고, 면접 관련 내용은 면접 질문 또는 면접 포인트 섹션으로 분리하도록 가이드에 명시. TCP와 UDP, TCPIP 모델 문서의 해당 표현도 정리.
생성/변경된 파일: published/network/TCP와 UDP.md, published/network/TCPIP 모델.md, wiki/meta/content-guidelines.md, AGENTS.md, CLAUDE.md, wiki/log.md

---

## [2026-06-18] ingest | network — TCP와 UDP 개념 보강
기존 TCP와 UDP 문서를 전송 계층, 포트 번호, TCP 신뢰성 메커니즘, UDP 선택 기준, 흐름 제어와 혼잡 제어 중심으로 보강하고 이미지 자료를 추가.
생성/변경된 파일: published/network/TCP와 UDP.md, raw/assets/Pasted image 20260618195504.png, wiki/log.md

---

## [2026-06-18] meta | TCPIP 모델 이미지 동기화 수정
TCPIP 모델 문서의 이미지가 앱 image block으로 변환되도록 이미지 wikilink를 정의 섹션 안으로 이동하고, 참조되는 raw/assets 이미지를 업로드 대상에 포함.
생성/변경된 파일: published/network/TCPIP 모델.md, raw/assets/Pasted image 20260617203311.png, wiki/log.md

---

## [2026-06-17] ingest | network — TCPIP 모델 신규 생성
TCPIP 모델을 OSI 7계층과 분리된 실제 인터넷 프로토콜 스택 개념으로 신규 작성. 네트워크 접근/인터넷/전송/응용 계층, IP와 포트, TCP·UDP와의 관계를 중심으로 정리하고 퀴즈 6문항(id 706-711)을 추가.
생성/변경된 파일: published/network/TCPIP 모델.md, quiz/network/TCPIP 모델.md, published/network/TCP와 UDP.md, published/network/OSI 7계층.md, wiki/index.md, wiki/log.md

---

## [2026-06-17] meta | 퀴즈 앱 디코딩 형식 복구
DB 변경 사항에 맞춰 객관식 type은 mcq, correct_index는 배열로 동기화하도록 sync_quiz_to_supabase.py를 수정하고, import_quiz_from_db.py도 배열형 정답 인덱스를 처리하도록 보강.
생성/변경된 파일: scripts/sync_quiz_to_supabase.py, scripts/import_quiz_from_db.py, wiki/log.md

---

## [2026-06-17] meta | published stale 콘텐츠 삭제 동기화 로직 추가
published/를 content_items의 SSOT로 보고, 로컬 published/에 없는 기존 콘텐츠 row를 Supabase에서도 삭제하도록 sync_to_supabase.py를 보강.
생성/변경된 파일: scripts/sync_to_supabase.py, wiki/log.md

---

## [2026-06-15] meta | network — OSI 7계층 콘텐츠명 정리
TCP/IP는 OSI 7계층에 종속된 가벼운 개념이 아니므로 기존 콘텐츠명을 OSI 7계층으로 변경하고, TCP/IP는 비교 대상으로만 짧게 언급하도록 조정. 관련 wikilink와 퀴즈 파일명도 함께 정리.
생성/변경된 파일: published/network/OSI 7계층.md, quiz/network/OSI 7계층.md, published/network/TCP와 UDP.md, published/network/DNS.md, published/network/웹 요청 흐름.md, wiki/index.md, wiki/log.md

---

## [2026-06-15] ingest | network — OSI 7계층과 TCP/IP 보강
raw/OSI 7계층.md 자료를 기반으로 기존 OSI 7계층과 TCPIP 콘텐츠를 7계층별 역할, 데이터 단위, 장비·프로토콜 중심의 개념 설명서 형태로 보강. 퀴즈 6문항(id 700-705) 추가.
생성/변경된 파일: published/network/OSI 7계층과 TCPIP.md, quiz/network/OSI 모델.md, wiki/log.md

---

## [2026-05-04] ingest | database — 데이터베이스 기본 개념 보강
데이터베이스를 단순 저장소가 아니라 애플리케이션의 신뢰 가능한 데이터 관리 계층으로 설명하도록 기존 콘텐츠를 보강. 트랜잭션, 인덱스, 격리 수준 등 세부 문서와 겹치지 않도록 기본 개념 지도 중심으로 정리.
생성/변경된 파일: published/database/데이터베이스 기본.md, wiki/log.md

---

## [2026-05-01] ingest | network — 3-way handshake와 4-way handshake 보강
raw 자료(TCP 3-way/4-way handshake 블로그 클리핑)를 기반으로 기존 빈약한 파일을 전면 보강. frontmatter 추가, 단계별 상태(SYN_SENT, SYN_RECEIVED, ESTABLISHED), TIME_WAIT 상세 설명 추가. 퀴즈 6문항(id 691-696) 신규 생성.
생성/변경된 파일: published/network/3-way handshake와 4-way handshake.md, quiz/network/3-way handshake와 4-way handshake.md, wiki/log.md

---

## [2026-04-29] meta | 퀴즈 삭제 동기화 로직 추가
quiz/를 SSOT로 보고 로컬 파일에 없는 quiz_questions id를 Supabase에서도 삭제하도록 sync_quiz_to_supabase.py를 보강.
생성/변경된 파일: scripts/sync_quiz_to_supabase.py, README.md, wiki/log.md

---

## [2026-04-29] lint | 퀴즈 빈칸 한국어 단답 기준 정리
quiz/ 전체 216문항 구조 점검. 빈칸 64문항의 정답을 모두 한국어 단답으로 정리하고, 정답 노출·영어 API명·숫자·약어 맞히기 문항을 개념어 중심으로 수정.
생성/변경된 파일: quiz/algorithms/*, quiz/android/*, quiz/data-structure/*, quiz/database/*, quiz/ios/*, quiz/network/*, quiz/oop/추상화.md, quiz/operating-system/*, quiz/server/*, wiki/meta/content-guidelines.md, wiki/log.md

---

## [2026-04-25] ingest | Android — Map과 HashMap (Kotlin)
HashMap 내부 원리(배열+연결리스트→트리, 해시 충돌, 버킷, 리사이징) 신규 생성. 퀴즈 6문항(id 685-690).
생성된 파일: published/android/Map과 HashMap.md, quiz/android/Map과 HashMap.md, wiki/index.md

---

## [2026-04-25] meta | oop 신규 대분류 생성 — ios에서 이동
OOP는 Swift 전용 개념이 아니라 별도 카테고리가 적합하다는 판단으로 ios → oop 이동.
변경된 파일: published/oop/*, quiz/oop/*, scripts/sync_to_supabase.py, CLAUDE.md, wiki/index.md

## [2026-04-25] ingest | OOP — 객체지향 프로그래밍(OOP)·추상화·다형성 (Swift 중심)
Swift로 보는 OOP 3개 콘텐츠 신규 생성. 퀴즈 18문항(id 667-684).
생성된 파일: published/oop/객체지향 프로그래밍(OOP).md, published/oop/추상화.md, published/oop/다형성.md, quiz/oop/객체지향 프로그래밍(OOP).md, quiz/oop/추상화.md, quiz/oop/다형성.md, wiki/index.md

---

## [2026-04-24] ingest | Server — 서버 개념.md 8개 파일로 분리
폴더명 Server→server 소문자 통일. 심종한.md 삭제. 메시지큐/Spring MVC/Spring AOP/쿠키·세션·JWT/Polling·SSE·WebSocket/JDBC·ORM/CICD 배포 전략/Docker 생성. quiz 48문항(id 619-666).
생성/변경된 파일: published/server/* (8개), quiz/server/* (8개), categories/server.md, CLAUDE.md, wiki/index.md

---

## [2026-04-24] ingest | Android - Compose UI (신규, android 대분류 생성)
raw/Android Compose UI.md 처리. android 대분류 신규 생성.
생성/변경된 파일: published/android/Compose UI.md, quiz/android/Compose UI.md, categories/android.md, CLAUDE.md, wiki/index.md

---

## [2026-04-24] ingest | iOS - Combine (신규)
raw/Combine 연습해보기-(WWDC).md 처리. DFS/BFS·앱 생명주기는 기존 파일 존재로 스킵.
생성/변경된 파일: published/ios/Combine.md, quiz/ios/Combine.md, wiki/index.md

---

## [2026-04-24] ingest | 앱 생명주기 — 신규 (ios 대분류 생성)

raw/iOS - 앱의 생명주기 클리핑 처리. ios 대분류 신규 생성.

생성/변경된 파일:
- published/ios/앱 생명주기.md (신규)
- scripts/sync_to_supabase.py (ios 카테고리 추가)
- wiki/index.md (ios 카테고리 추가)

## [2026-04-24] ingest | 그래프 탐색(BFSDFS) — 업데이트

raw/알고리즘 깊이 우선 탐색(DFS) 과 너비 우선 탐색(BFS).md 클리핑 처리.
기존 파일에 시간복잡도(O(N+E) vs O(N²)), 문제 유형별 선택 기준 보강.

변경된 파일:
- published/algorithms/그래프 탐색(BFSDFS).md (업데이트)

## [2026-04-24] meta | 앱 데이터 모델 반영 — JSON 파이프라인 스키마 확정

실제 앱 JSON 구조 확인 후 CLAUDE.md, meta/app-features.md 업데이트.
Raw → concepts/ + content/(JSON 포함) 파이프라인 확정.

생성/변경된 파일:
- CLAUDE.md (업데이트) — JSON 스키마, block 타입, slug 규칙, display_order 규칙 추가
- wiki/index.md (업데이트) — display_order 현황 테이블 추가
- wiki/meta/app-features.md (업데이트) — 데이터 모델 상세 추가

## [2026-04-24] ingest | 배열과 연결리스트의 차이 (예시)

파이프라인 동작 확인용 예시 콘텐츠 생성.

생성된 파일:
- wiki/concepts/ds-array-vs-linked-list.md
- wiki/content/ds-array-vs-linked-list.md (JSON 포함, status: draft)

## [2026-04-24] meta | 위키 시스템 초기화

CSContent 앱을 위한 LLM Wiki 시스템을 구축했다.
앱은 퀴즈 + 개념 설명 기능이 이미 구현된 상태이며, 이 위키는 콘텐츠 제작을 기록·연결하는 두뇌 역할을 한다.

변경된 파일:
- CLAUDE.md (신규) — 스키마 & 운영 가이드
- wiki/index.md (신규) — 전체 카탈로그
- wiki/log.md (신규) — 이 파일
- wiki/overview.md (신규) — CS 커버리지 현황 & 로드맵
- wiki/topics/data-structures.md (신규)
- wiki/topics/algorithms.md (신규)
- wiki/topics/operating-systems.md (신규)
- wiki/topics/networks.md (신규)
- wiki/topics/databases.md (신규)
- wiki/topics/system-design.md (신규)
- wiki/meta/app-features.md (신규)
- wiki/meta/content-guidelines.md (신규)
