# CSContent Wiki — 활동 로그

> append-only. 가장 최근 항목이 위에 온다.
> 파싱: `grep "^## \[" wiki/log.md | head -10`

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
