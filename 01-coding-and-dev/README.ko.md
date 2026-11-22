🌐 [English](README.md) | **한국어 (Korean)**

# 💻 IT · 코딩 & 개발 워크플로우 (Coding & Dev Workflows)

> 코딩 에이전트 스킬, 멀티 에이전트 오케스트레이션·하네스, 코드 리뷰·지식 그래프, 테스트·CLI 및 백엔드 개발 도구

[🏠 메인으로 돌아가기](../README.ko.md) · [🔍 웹에서 실시간 검색하기](https://godstale.github.io/Agent-Toolbox/?lang=ko&cat=01-coding-and-dev) · [📂 GitHub 내 검색](https://github.com/godstale/Agent-Toolbox/search?q=path%3A01-coding-and-dev)

총 **65개** 항목 수록 · 최종 업데이트: `2026-11-22`

## 세부 분류 목차

- [코딩 에이전트 스킬](#코딩-에이전트-스킬) (7)
- [플랫폼·프레임워크 공식 스킬](#플랫폼프레임워크-공식-스킬) (6)
- [멀티 에이전트 오케스트레이션 & 하네스](#멀티-에이전트-오케스트레이션-하네스) (14)
- [코드 리뷰 · 분석 · 지식 그래프](#코드-리뷰-분석-지식-그래프) (9)
- [브라우저 · 데스크톱 제어 & 테스트](#브라우저-데스크톱-제어-테스트) (7)
- [터미널 · IDE · 개발 유틸리티](#터미널-ide-개발-유틸리티) (4)
- [백엔드 · DB · 인프라 개발 도구](#백엔드-db-인프라-개발-도구) (9)
- [MCP · API · 레퍼런스 모음](#mcp-api-레퍼런스-모음) (5)
- [시스템 · 컴파일러 · 핵심 라이브러리](#시스템-컴파일러-핵심-라이브러리) (4)

## 코딩 에이전트 스킬

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **Superpowers** | 기획 확인, 구현 계획, TDD 작성, 2단계 코드 리뷰로 이어지는 개발 워크플로우 스킬 모음 (필요한 하위 스킬만 선택 사용 권장). ([심층 가이드](https://godstale.mycafe24.com/?p=801)) | `Skill` | [github.com/obra/superpowers](https://github.com/obra/superpowers) |
| **Matt Pocock Skills (Grill-me 포함)** | 현업 엔지니어 맷 포콕의 AI 코딩 스킬 모음. 인터뷰 방식으로 기획을 검증하는 Grill-me와 세션 회고(/retro) 등을 제공. ([심층 가이드](https://godstale.mycafe24.com/?p=1136)) | `Skill` | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) |
| **addyosmani/agent-skills** | 애디 오스마니가 정리한 프로덕트 수준 에이전트 스킬 모음 (spec, plan, build, test, review, simplify, ship 단계 지원). ([심층 가이드](https://godstale.mycafe24.com/?p=1136)) | `Skill` | [github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| **pstack (Lauren Tan)** | 로렌 탄이 공개한 실전 코딩 에이전트 플러그인·스킬 묶음. 단계별 구현과 검증 루프를 구조화. ([심층 가이드](https://godstale.mycafe24.com/?p=1136)) | `Skill` | [github.com/cursor/plugins/tree/main/pstack](https://github.com/cursor/plugins/tree/main/pstack) |
| **Andrej Karpathy Skills** | 안드레이 카파시의 조언을 바탕으로 AI가 과도하게 코드를 부풀리거나 주변 코드를 건드리지 않게 제어하는 코딩 효율화 스킬. ([심층 가이드](https://godstale.mycafe24.com/?p=801)) | `Skill` | [github.com/forrestchang/andrej-karpathy...](https://github.com/forrestchang/andrej-karpathy-skills) |
| **Ponytail** | 토큰 절약과 불필요한 코드 작성을 줄이기 위한 간결한 시니어 개발자 스타일 코딩 스킬. | `Skill` | [github.com/alexphelps/ponytail](https://github.com/alexphelps/ponytail) |
| **unclebob/ub-mode** | '클린 코드' 저자 로버트 C. 마틴(엉클 밥)의 개발 규율과 TDD 원칙을 에이전트에 적용하는 스킬. | `Skill` | [github.com/unclebob/ub-mode](https://github.com/unclebob/ub-mode) |

## 플랫폼·프레임워크 공식 스킬

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **GoogleChrome/modern-web-guidance-src** | 코딩 에이전트가 오래된 폴리필 대신 최신 HTML·CSS·네이티브 브라우저 API와 Baseline 기준을 쓰도록 돕는 구글 크롬 공식 스킬·CLI. ([심층 가이드](https://godstale.mycafe24.com/?p=1168)) | `Skill` | [github.com/GoogleChrome/modern-web-guid...](https://github.com/GoogleChrome/modern-web-guidance-src) |
| **anthropics/skills (Skill Creator 포함)** | 앤트로픽 공식 에이전트 스킬 모음. 문서(pptx·xlsx 등) 작업 스킬과 스킬 제작·평가용 Skill Creator를 포함. ([심층 가이드](https://godstale.mycafe24.com/?p=1168)) | `Skill` | [github.com/anthropics/skills](https://github.com/anthropics/skills) |
| **Supabase Agent Skills** | Supabase 데이터베이스, 인증, 마이그레이션 등 데이터 저장·관리 작업을 에이전트에 가르치는 공식 스킬 모음. | `Skill` | [github.com/supabase/agent-skills](https://github.com/supabase/agent-skills) |
| **Vercel Agent Skills** | Next.js, React 서버 컴포넌트 및 배포 최적화를 위한 Vercel Labs 공식 에이전트 스킬 모음. | `Skill` | [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| **Google Cloud Skills (google/skills)** | 구글 클라우드(GCP) 서비스 활용법을 100개 이상의 에이전트 스킬로 정리한 공식 저장소. | `Skill` | [github.com/google/skills](https://github.com/google/skills) |
| **android/skills** | CameraX, Jetpack Compose 등 안드로이드 앱 개발용 구글 공식 에이전트 스킬 모음. | `Skill` | [github.com/android/skills](https://github.com/android/skills) |

## 멀티 에이전트 오케스트레이션 & 하네스

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **affaan-m/ECC (Everything Claude Code)** | 계획·리뷰·보안 역할의 서브에이전트와 수백 개의 스킬·훅을 통합한 대규모 에이전트 하네스. | `Framework/Harness` | [github.com/affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **Paseo** | Claude Code, Codex 등 여러 코딩 에이전트를 격리된 Git Worktree에서 동시에 돌리고 웹·모바일에서 제어·병합하는 워크스페이스. ([심층 가이드](https://godstale.mycafe24.com/?p=1163)) | `App` | [github.com/getpaseo/paseo](https://github.com/getpaseo/paseo) |
| **Worktrunk** | Git Worktree를 활용해 여러 코딩 AI에 각자 독립된 작업 폴더를 배정하고 완료 후 병합하는 CLI 도구. ([심층 가이드](https://godstale.mycafe24.com/?p=1155)) | `Tool/CLI` | [github.com/max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) |
| **OpenRig** | 리드 에이전트와 워커 에이전트로 역할을 분담해 작업을 지휘하는 에이전트 오케스트레이션 도구. | `Framework/Harness` | [github.com/mvschwarz/openrig](https://github.com/mvschwarz/openrig) |
| **ruflo** | Claude Code와 Codex 위에 올려 다중 에이전트 흐름을 조율하는 오케스트레이션 도구. | `Framework/Harness` | [github.com/ruvnet/ruflo](https://github.com/ruvnet/ruflo) |
| **DeepSeek Harness / DSH Desktop** | 모델·도구·스킬·작업 기록을 하나로 묶어 AI 에이전트를 실행하는 플러그인형 하네스 환경. | `Framework/Harness` | [github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) |
| **Google Research Harness²** | 에이전트 실행 환경을 스스로 실험하고 개선하는 자가 개선 하네스 연구 저장소. ([심층 가이드](https://godstale.mycafe24.com/?p=1170)) | `Framework/Harness` | [github.com/google-research/harness2](https://github.com/google-research/harness2) |
| **GSD (Get Sh*t Done)** | 스펙 기반 개발과 컨텍스트 윈도우 관리에 초점을 맞춘 AI 코딩 워크플로우 프레임워크. | `Framework/Harness` | [github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) |
| **Agency Agents** | 개발·기획·아키텍처 등 분야별 전문 에이전트 페르소나를 명령어나 데스크톱 앱으로 손쉽게 설치·관리하는 도구. | `App` | [github.com/msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) |
| **codex-plugin-cc** | Claude Code 세션 안에서 OpenAI Codex를 직접 호출해 코드 리뷰나 하위 작업을 위임하는 플러그인. | `Tool/CLI` | [github.com/openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) |
| **t3code** | 내 PC에 설치된 Claude Code, Codex, Cursor 등을 웹·데스크톱·휴대폰에서 원격 제어하는 UI. | `App` | [github.com/pingdotgg/t3code](https://github.com/pingdotgg/t3code) |
| **OpenMausBot** | 메신저 스타일 화면에서 Claude, Codex 등 로컬 코딩 에이전트를 권한 제어와 함께 운영하는 오픈소스 데스크톱 앱. | `App` | [github.com/milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) |
| **Nodeterm** | 여러 AI 에이전트 터미널을 무한 캔버스 위에 노드 형태로 띄워두고 상태를 한눈에 모니터링하는 앱. ([심층 가이드](https://godstale.mycafe24.com/?p=848)) | `App` | [github.com/eneskirca/nodeterm](https://github.com/eneskirca/nodeterm) |
| **Hermes Agent** | Nous Research의 오픈소스 로컬 AI 에이전트 및 봇 모드 실행 프레임워크. ([심층 가이드](https://godstale.mycafe24.com/?p=804)) | `Framework/Harness` | [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) |

## 코드 리뷰 · 분석 · 지식 그래프

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **codebase-memory-mcp** | Tree-sitter로 코드베이스 전체를 오프라인 지식 그래프로 인덱싱해 탐색 토큰을 크게 줄여주는 로컬 MCP 서버. | `MCP` | [github.com/DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) |
| **Trail-code (구 Graft)** | 로컬에서 함수 호출 지도를 만들어 프롬프트마다 관련 파일 위치를 붙이고 수정 영향 범위(blast radius)를 알려주는 컨텍스트 레이어. | `Tool/CLI` | [github.com/trailhq/trail-code](https://github.com/trailhq/trail-code) |
| **code-review-graph** | 저장소를 의존성 그래프로 구성해 AI가 리뷰에 꼭 필요한 파일만 읽도록 돕는 도구. | `Tool/CLI` | [github.com/tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) |
| **open-code-review** | 알리바바 사내 코드 리뷰 경험을 바탕으로 규칙 매칭은 결정적으로, 맥락 판단은 LLM으로 분리한 코드 리뷰 도구. | `Tool/CLI` | [github.com/alibaba/open-code-review](https://github.com/alibaba/open-code-review) |
| **plannotator** | 에이전트가 세운 작업 계획과 코드 변경 사항을 브라우저에서 댓글로 검토해 한 번에 피드백을 돌려보내는 도구. ([심층 가이드](https://godstale.mycafe24.com/?p=1168)) | `Tool/CLI` | [github.com/backnotprop/plannotator](https://github.com/backnotprop/plannotator) |
| **Understand-Anything** | 대규모 코드베이스를 멀티 에이전트와 Tree-sitter로 탐색해 지식 그래프와 웹 대시보드로 시각화하는 플러그인. ([심층 가이드](https://godstale.mycafe24.com/?p=801)) | `Skill` | [github.com/Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) |
| **Graphify** | 코드·문서·PDF를 로컬 Tree-sitter 기반 지식 그래프로 매핑해 에이전트 탐색 비용을 줄여주는 CLI 및 스킬. ([심층 가이드](https://godstale.mycafe24.com/?p=801)) | `Tool/CLI` | [github.com/Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) |
| **Archify** | 코드베이스나 시스템 설명을 분석해 아키텍처 다이어그램으로 자동 변환하는 도구. | `Tool/CLI` | [github.com/archify-ai/archify](https://github.com/archify-ai/archify) |
| **NVIDIA SkillEvaluator** | AI 에이전트 스킬(SKILL.md)의 스키마·보안·실제 성능 향상 효과를 다단계로 검증하는 NVIDIA 오픈소스 평가 프레임워크. ([심층 가이드](https://godstale.mycafe24.com/?p=1168)) | `Framework/Harness` | [github.com/NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) |

## 브라우저 · 데스크톱 제어 & 테스트

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **chrome-devtools-mcp** | 에이전트가 실제 Chrome 브라우저를 열어 네트워크, 콘솔, 성능 프로파일까지 직접 점검하는 구글 공식 MCP 서버. | `MCP` | [github.com/ChromeDevTools/chrome-devtoo...](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| **vercel-labs/agent-desktop** | OS 접근성 트리를 읽어 AI 에이전트가 Mac·Windows·Linux 데스크톱 앱을 직접 조작하도록 돕는 오픈소스 CLI·스킬. ([심층 가이드](https://godstale.mycafe24.com/?p=1155)) | `Tool/CLI` | [github.com/vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) |
| **vercel-labs/agent-browser** | 에이전트가 셸 명령으로 웹 브라우저를 간결하게 탐색·조작할 수 있도록 만든 CLI 도구. | `Tool/CLI` | [github.com/vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **browser-use** | LLM 에이전트가 웹 브라우저의 클릭·입력·스크롤 작업을 자율적으로 수행하도록 연결하는 오픈소스 프레임워크. | `Framework/Harness` | [github.com/browser-use/browser-use](https://github.com/browser-use/browser-use) |
| **Playwright** | 마이크로소프트의 크로스 브라우저 자동화 및 E2E UI 테스트 오픈소스 프레임워크. | `Tool/CLI` | [github.com/microsoft/playwright](https://github.com/microsoft/playwright) |
| **tester-army/e2e** | 기존 코드 테스트에 자연어 단계를 섞어 작성할 수 있는 E2E 테스트 프레임워크. | `Framework/Harness` | [github.com/tester-army/e2e](https://github.com/tester-army/e2e) |
| **Google ARTEMIS** | 자연어 지시로 안드로이드 앱 UI를 자동 조작하고 테스트하는 구글의 UI 테스트 에이전트. | `Tool/CLI` | [github.com/google/artemis](https://github.com/google/artemis) |

## 터미널 · IDE · 개발 유틸리티

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **CLI-Anything** | GUI 프로그램이나 일반 소프트웨어를 CLI 명령으로 감싸 에이전트가 실행할 수 있게 해주는 스킬·도구. | `Skill` | [github.com/HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) |
| **JetBrains Thinkrail** | JetBrains 인큐베이터에서 공개한 가벼운 데스크톱 AI 코딩 도구 (오픈소스 코딩 에이전트 pi 내장). | `App` | [github.com/JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) |
| **Open Interpreter** | 로컬 및 오픈 모델이 터미널에서 직접 코드를 실행해 작업을 처리하도록 돕는 오픈소스 코딩 에이전트. | `Tool/CLI` | [github.com/OpenInterpreter/open-interpr...](https://github.com/OpenInterpreter/open-interpreter) |
| **Ghostty** | GPU 가속과 네이티브 UI를 지원하는 빠르고 가벼운 macOS·Linux용 터미널 에뮬레이터. | `App` | [github.com/ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) |

## 백엔드 · DB · 인프라 개발 도구

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **Expo Exact** | React 없이 선언형 뷰 언어로 웹·macOS·iOS·Linux 네이티브 앱을 만드는 AI 친화적 Rust 기반 크로스플랫폼 런타임. | `Framework/Harness` | [github.com/expo/exact](https://github.com/expo/exact) |
| **drawDB** | 설치 없이 브라우저에서 바로 데이터베이스 ERD를 설계하고 SQL을 생성하는 오픈소스 편집기. | `App` | [github.com/drawdb-io/drawdb](https://github.com/drawdb-io/drawdb) |
| **Appwrite** | 인증, 데이터베이스, 파일 저장소, 서버 함수, 호스팅을 한 번에 제공하는 오픈소스 백엔드(BaaS) 플랫폼. | `Framework/Harness` | [github.com/appwrite/appwrite](https://github.com/appwrite/appwrite) |
| **Floci** | 외부 클라우드 계정 없이 내 PC에서 AWS·클라우드 환경을 빠르게 에뮬레이션하는 경량 오픈소스 도구. ([심층 가이드](https://godstale.mycafe24.com/?p=1155)) | `Tool/CLI` | [github.com/floci-io/floci](https://github.com/floci-io/floci) |
| **Arcane** | 터미널 명령 대신 깔끔한 웹 대시보드에서 Docker 컨테이너·볼륨·Compose 스택을 관리하는 오픈소스 UI. | `App` | [github.com/getarcaneapp/arcane](https://github.com/getarcaneapp/arcane) |
| **Coder** | 개발자와 AI 에이전트가 Docker·Terraform 기반으로 격리된 원격 개발 환경을 셀프 호스팅하는 플랫폼. ([심층 가이드](https://godstale.mycafe24.com/?p=1072)) | `Framework/Harness` | [github.com/coder/coder](https://github.com/coder/coder) |
| **Supabase CLI** | 데이터베이스 스키마 마이그레이션, Edge Functions, 인증을 터미널에서 직접 제어하는 공식 CLI. | `Tool/CLI` | [github.com/supabase/cli](https://github.com/supabase/cli) |
| **Vercel CLI** | 프론트엔드·서버리스 배포와 환경 변수를 터미널과 에이전트 루프에서 직접 관리하는 공식 CLI. | `Tool/CLI` | [github.com/vercel/vercel](https://github.com/vercel/vercel) |
| **GitHub CLI (gh)** | 이슈, PR, Actions 워크플로우, 릴리스를 터미널에서 에이전트와 함께 제어하는 GitHub 공식 CLI. | `Tool/CLI` | [cli.github.com](https://cli.github.com/) |

## MCP · API · 레퍼런스 모음

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **Google MCP Toolbox (genai-toolbox)** | 구글이 제공하는 데이터베이스·클라우드 연동용 오픈소스 MCP 서버 툴박스. | `MCP` | [github.com/googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) |
| **awesome-mcp-servers** | 전 세계 개발자들이 만든 Model Context Protocol(MCP) 서버를 분야별로 정리한 대표 큐레이션 목록. | `Resource/Guide` | [github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) |
| **public-apis** | 개발자와 에이전트 프로젝트에 활용할 수 있는 무료 공개 API를 카테고리별로 모아둔 대표 북마크 저장소. | `Resource/Guide` | [github.com/public-apis/public-apis](https://github.com/public-apis/public-apis) |
| **claude-quickstarts** | Claude API와 에이전트 기반 프로젝트를 빠르게 시작할 수 있도록 Anthropic이 제공하는 공식 템플릿 모음. | `Resource/Guide` | [github.com/anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts) |
| **claude-code-tips** | 깃허브에서 화제가 된 Claude Code 실전 활용 팁과 워크플로우 노하우를 정리한 가이드. | `Resource/Guide` | [github.com/ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) |

## 시스템 · 컴파일러 · 핵심 라이브러리

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **RAD Debugger** | Epic Games가 공개한 다중 프로세스 지원 네이티브 디버거 (Windows 및 Linux 예비 지원). | `Tool/CLI` | [github.com/EpicGames/raddebugger](https://github.com/EpicGames/raddebugger) |
| **LLVM Project** | Rust, Swift, Clang 등 현대 언어의 최적화와 기계어 생성을 담당하는 공용 컴파일러 인프라. | `Library` | [github.com/llvm/llvm-project](https://github.com/llvm/llvm-project) |
| **{fmt}** | 파이썬과 비슷한 직관적인 문법으로 안전하고 빠른 문자열 포매팅을 제공하는 C++ 오픈소스 라이브러리. | `Library` | [github.com/fmtlib/fmt](https://github.com/fmtlib/fmt) |
| **Modular Mojo** | 파이썬 문법 친화성과 시스템 언어급 성능을 결합한 AI 개발용 프로그래밍 언어 및 컴파일러. | `Library` | [github.com/modular/modular](https://github.com/modular/modular) |

---

### 다른 카테고리 둘러보기

**💻 IT · 코딩 & 개발 워크플로우** · [⚡ 생산성 · 협업 & 비즈니스](../02-productivity-and-business/README.ko.md) · [🎨 미디어 · 디자인 & 크리에이티브](../03-media-and-creative/README.ko.md) · [🎮 게임 개발 & 에셋 제작](../04-game-dev/README.ko.md) · [📚 교육 · 학습 & 연구](../05-education-and-research/README.ko.md) · [🖥️ 로컬 AI · 모델 서빙 & 인프라](../06-local-ai-and-infra/README.ko.md) · [🛡️ 보안 · 역공학 & OSINT](../07-security-and-osint/README.ko.md)
