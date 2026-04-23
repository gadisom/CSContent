---
slug: <%*
const folder = tp.file.folder(true);
const category = folder.split("/").pop();
const prefixes = {
  "data-structure": "ds",
  "algorithms": "alg",
  "operating-system": "os",
  "database": "db",
  "network": "net"
};
const prefix = prefixes[category] ? prefixes[category] + "-" : "";
const slug = await tp.system.prompt("slug", prefix);
tR += slug;
%>
---

> <% tp.file.cursor(1) %>

## 정의
- <% tp.file.cursor(2) %>

## 핵심 포인트
- <% tp.file.cursor(3) %>

## 면접 질문
- <% tp.file.cursor(4) %>

## 확인 문제
- <% tp.file.cursor(5) %>

## 키워드
<% tp.file.cursor(6) %>

## 연관 콘텐츠
- <% tp.file.cursor(7) %>
