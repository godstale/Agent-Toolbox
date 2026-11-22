# 🛡️ 보안 · 역공학 & OSINT (Security, Reverse Engineering & OSINT)

> 보안 감사 스킬·CLI, 스킬 악성코드 스캐너, 리버스 엔지니어링·클린룸 분석, OSINT 점검 및 통합 인증

[🏠 메인으로 돌아가기](../README.md) · [🔍 웹에서 실시간 검색하기](https://godstale.github.io/Agent-Toolbox/?cat=07-security-and-osint) · [📂 GitHub 내 검색](https://github.com/godstale/Agent-Toolbox/search?q=path%3A07-security-and-osint)

총 **12개** 항목 수록 · 최종 업데이트: `2026-11-22`

## 세부 분류 목차

- [보안 감사 · 취약점 점검 & 스킬 스캐너](#보안-감사-취약점-점검-스킬-스캐너) (4)
- [리버스 엔지니어링 & 클린룸 분석](#리버스-엔지니어링-클린룸-분석) (4)
- [OSINT · 계정 보안 & 통합 인증](#osint-계정-보안-통합-인증) (4)

## 보안 감사 · 취약점 점검 & 스킬 스캐너

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **openai/codex-security** | 저장소의 위협 모델을 세우고 취약점 후보를 샌드박스에서 검증한 뒤 패치까지 제안하는 OpenAI 공식 보안 CLI·SDK. ([심층 가이드](https://godstale.mycafe24.com/?p=1168)) | `Tool/CLI` | [github.com/openai/codex-security](https://github.com/openai/codex-security) |
| **Cloudflare security-audit-skill** | 코딩 에이전트를 독립적이고 일관된 보안 감사관으로 동작하게 만드는 Cloudflare 오픈소스 다단계 감사 스킬. ([심층 가이드](https://godstale.mycafe24.com/?p=1155)) | `Skill` | [github.com/cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) |
| **NVIDIA SkillSpector** | 외부에서 받은 AI 에이전트 스킬 내부의 악성 명령이나 프롬프트 인젝션을 탐지하는 NVIDIA 보안 스캐너. | `Tool/CLI` | [github.com/NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) |
| **Claude-BugHunter** | 버그 바운티와 모의 해킹 점검 절차를 정리한 스킬 묶음 (반드시 본인 소유 또는 서면 허가를 받은 자산에만 사용). ([심층 가이드](https://godstale.mycafe24.com/?p=1168)) | `Skill` | [github.com/elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) |

## 리버스 엔지니어링 & 클린룸 분석

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **Craft Anything** | 외부 동작과 화면을 관찰해 클린룸(Study→Build→Check) 방식으로 분석·재구현하는 Rust 기반 MCP·CLI 엔진 (저작권·약관 준수 필수). ([심층 가이드](https://godstale.mycafe24.com/?p=1168)) | `MCP` | [github.com/storytold/craft-anything](https://github.com/storytold/craft-anything) |
| **REA (Reverse Engineer Anything)** | 실행 파일·앱·웹사이트의 구조와 동작 원리를 로컬에서 분석하는 역공학 MCP 도구 겸 스킬 (법·라이선스 확인 필수). ([심층 가이드](https://godstale.mycafe24.com/?p=1113)) | `MCP` | [github.com/morluto/rea](https://github.com/morluto/rea) |
| **reverse-skill** | IDA, Ghidra 같은 역공학·모의침투 워크플로우 스킬 20여 개를 단일 라우터로 연결한 스킬 모음. | `Skill` | [github.com/zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) |
| **Ghidra** | 미국 국가안보국(NSA)이 오픈소스로 공개한 대표 소프트웨어 리버스 엔지니어링 분석 프레임워크. | `App` | [github.com/NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) |

## OSINT · 계정 보안 & 통합 인증

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **Sherlock** | 400개 이상의 웹사이트에서 특정 아이디(Username) 사용 여부를 조회하는 오픈소스 OSINT 도구. | `Tool/CLI` | [github.com/sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) |
| **Holehe** | 이메일 주소 하나로 어떤 온라인 서비스에 가입되어 있는지 확인하는 개인 보안 점검용 OSINT 도구. | `Tool/CLI` | [github.com/megadose/holehe](https://github.com/megadose/holehe) |
| **authentik** | SSO, OAuth2, SAML, LDAP를 지원하는 셀프호스팅 오픈소스 통합 인증(IdP) 서버. | `App` | [github.com/goauthentik/authentik](https://github.com/goauthentik/authentik) |
| **Heretic** | 재학습 없이 오픈 웨이트 모델의 과도한 거절 성향이나 상투적 말투를 조정하는 연구용 도구 (윤리·안전 범위 내 사용). ([심층 가이드](https://godstale.mycafe24.com/?p=1155)) | `Tool/CLI` | [github.com/p-e-w/heretic](https://github.com/p-e-w/heretic) |

---

### 다른 카테고리 둘러보기

[💻 IT · 코딩 & 개발 워크플로우](../01-coding-and-dev/README.md) · [⚡ 생산성 · 협업 & 비즈니스](../02-productivity-and-business/README.md) · [🎨 미디어 · 디자인 & 크리에이티브](../03-media-and-creative/README.md) · [🎮 게임 개발 & 에셋 제작](../04-game-dev/README.md) · [📚 교육 · 학습 & 연구](../05-education-and-research/README.md) · [🖥️ 로컬 AI · 모델 서빙 & 인프라](../06-local-ai-and-infra/README.md) · **🛡️ 보안 · 역공학 & OSINT**
