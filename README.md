# 🧰 Agent Toolbox

**AI 에이전트·스킬·오픈소스·앱 분야별 큐레이션 저장소**

AI 에이전트(Claude Code, Codex, Gemini 등)와 함께 활용할 수 있는 최신 GitHub 오픈소스, 스킬(Skills), MCP 서버, 앱, 라이브러리, 학습 자료를 **사용 분야별**로 정리한 저장소입니다.  
모든 항목은 **`[Name, Description, URL]`** 표준 구조로 관리되며, 누구나 한눈에 파악할 수 있도록 쉽고 담백한 설명을 제공합니다.

![Total Tools](https://img.shields.io/badge/Tools-201-blue?style=flat-square) ![Categories](https://img.shields.io/badge/Categories-7-green?style=flat-square) ![Updated](https://img.shields.io/badge/Updated-2026--11--22-orange?style=flat-square)

## 🔍 도구 검색하기 (Search)

> **⚡ 실시간 검색창 (웹 앱):** [**Agent Toolbox 검색 페이지 열기 (GitHub Pages)**](https://godstale.github.io/Agent-Toolbox/)  
> 키워드 입력창, 카테고리 필터, 유형별 필터로 원하는 도구를 즉시 찾을 수 있습니다.

GitHub 화면에서 바로 검색하려면 키보드에서 **`/`** 키를 누르거나 아래 인기 키워드 버튼을 클릭하세요:

[`🔎 Claude Code`](https://github.com/godstale/Agent-Toolbox/search?q=Claude+Code) [`🔎 MCP`](https://github.com/godstale/Agent-Toolbox/search?q=MCP) [`🔎 Skill`](https://github.com/godstale/Agent-Toolbox/search?q=Skill) [`🔎 Worktree`](https://github.com/godstale/Agent-Toolbox/search?q=Worktree) [`🔎 Sprite`](https://github.com/godstale/Agent-Toolbox/search?q=Sprite) [`🔎 Motion`](https://github.com/godstale/Agent-Toolbox/search?q=Motion) [`🔎 Local LLM`](https://github.com/godstale/Agent-Toolbox/search?q=Local+LLM) [`🔎 OCR`](https://github.com/godstale/Agent-Toolbox/search?q=OCR) [`🔎 Security`](https://github.com/godstale/Agent-Toolbox/search?q=Security) [`🔎 Design`](https://github.com/godstale/Agent-Toolbox/search?q=Design) [`🔎 Godot`](https://github.com/godstale/Agent-Toolbox/search?q=Godot) [`🔎 Memory`](https://github.com/godstale/Agent-Toolbox/search?q=Memory)

## 🔥 최신 AI 에이전트 트렌드 요약

- **빅테크의 에이전트 실무 도구 직접 공개**: 구글 크롬(modern-web-guidance-src), OpenAI(codex-security), 메타(astryx), NVIDIA(SkillEvaluator·Auto-Ontology) 등 빅테크가 코딩 에이전트 전용 스킬과 CLI를 오픈소스로 공개하는 흐름이 본격화되었습니다. — [관련 심층 포스트](https://godstale.mycafe24.com/?p=1168)
- **멀티 에이전트 병렬 실행과 워크트리 오케스트레이션**: 단일 세션 대신 Git Worktree로 작업 폴더를 분리해 Claude Code·Codex를 동시에 지휘하는 Paseo, Worktrunk, ECC, OpenRig, Harness² 같은 실행 환경이 주목받고 있습니다. — [관련 심층 포스트](https://godstale.mycafe24.com/?p=1163)
- **AI 티를 없애는 디자인 시스템 & 코드형 모션그래픽**: impeccable, taste-skill, ui-ux-pro-max, hallmark처럼 디자인 품질을 높이는 스킬과 HyperFrames, Remotion, 리틱체 등 코드로 영상을 렌더링하는 워크플로우가 확산 중입니다. — [관련 심층 포스트](https://godstale.mycafe24.com/?p=1167)
- **게임 개발·스프라이트 제작 오픈소스 파이프라인**: pixelfx, sprite-gen, PerfectPixel Studio, Agent Sprite Forge, Codixel, Pixelbolt 등 2D 게임 리소스와 애니메이션을 에이전트로 자동 생성·정렬하는 도구 생태계가 빠르게 성장하고 있습니다. — [관련 심층 포스트](https://godstale.mycafe24.com/?p=1172)

## 📂 분야별 카테고리 (Categories)

| 분야 (Category) | 수록 수 | 주요 다루는 내용 | 폴더 바로가기 |
|---|---:|---|---|
| 💻 **IT · 코딩 & 개발 워크플로우** | 65개 | 코딩 에이전트 스킬, 멀티 에이전트 오케스트레이션·하네스, 코드 리뷰·지식 그래프, 테스트·CLI 및 백엔드 개발 도구 | [`01-coding-and-dev/`](01-coding-and-dev/README.md) |
| ⚡ **생산성 · 협업 & 비즈니스** | 34개 | 업무·문서 자동화, 에이전트 메모리·위키, 회의 요약, 마케팅·SEO, 금융·가계부, 구직 및 스마트홈 연동 | [`02-productivity-and-business/`](02-productivity-and-business/README.md) |
| 🎨 **미디어 · 디자인 & 크리에이티브** | 44개 | AI 영상·모션그래픽, 음성(TTS/STT)·작곡, 이미지·3D·CAD 생성, UI/UX Anti-Slop 디자인 스킬 및 웹 그래픽스 | [`03-media-and-creative/`](03-media-and-creative/README.md) |
| 🎮 **게임 개발 & 에셋 제작** | 12개 | Godot·Bevy 등 게임 엔진 에이전트 스킬, 스프라이트 시트·도트 애니메이션 생성기, 픽셀 이펙트, 무료 에셋 | [`04-game-dev/`](04-game-dev/README.md) |
| 📚 **교육 · 학습 & 연구** | 12개 | 오픈 AI 커리큘럼, 개인 튜터·AI 교실, 학술 논문·과학 연구 스킬, 학습 보조 스킬 및 프롬프트 레퍼런스 | [`05-education-and-research/`](05-education-and-research/README.md) |
| 🖥️ **로컬 AI · 모델 서빙 & 인프라** | 22개 | 로컬 LLM 추론·파인튜닝 엔진, LLM 게이트웨이, 초경량 온디바이스 모델, 문서 파싱/OCR, 에이전트 샌드박스 | [`06-local-ai-and-infra/`](06-local-ai-and-infra/README.md) |
| 🛡️ **보안 · 역공학 & OSINT** | 12개 | 보안 감사 스킬·CLI, 스킬 악성코드 스캐너, 리버스 엔지니어링·클린룸 분석, OSINT 점검 및 통합 인증 | [`07-security-and-osint/`](07-security-and-osint/README.md) |

## 📋 전체 목록 한눈에 보기 (Quick Browse)

각 분야를 클릭해 펼쳐 보거나, 분야별 폴더의 `README.md`에서 세부 분류별로 열람할 수 있습니다.

<details>
<summary><strong>💻 IT · 코딩 & 개발 워크플로우 (65개)</strong> — 클릭해서 펼치기</summary>

👉 [전체 상세 페이지 보기 (`01-coding-and-dev/README.md`)](01-coding-and-dev/README.md)

| 이름 (Name) | 설명 (Description) | URL |
|---|---|---|
| **Superpowers** | 기획 확인, 구현 계획, TDD 작성, 2단계 코드 리뷰로 이어지는 개발 워크플로우 스킬 모음 (필요한 하위 스킬만 선택 사용 권장). | [링크](https://github.com/obra/superpowers) |
| **Matt Pocock Skills (Grill-me 포함)** | 현업 엔지니어 맷 포콕의 AI 코딩 스킬 모음. 인터뷰 방식으로 기획을 검증하는 Grill-me와 세션 회고(/retro) 등을 제공. | [링크](https://github.com/mattpocock/skills) |
| **addyosmani/agent-skills** | 애디 오스마니가 정리한 프로덕트 수준 에이전트 스킬 모음 (spec, plan, build, test, review, simplify, ship 단계 지원). | [링크](https://github.com/addyosmani/agent-skills) |
| **pstack (Lauren Tan)** | 로렌 탄이 공개한 실전 코딩 에이전트 플러그인·스킬 묶음. 단계별 구현과 검증 루프를 구조화. | [링크](https://github.com/cursor/plugins/tree/main/pstack) |
| **Andrej Karpathy Skills** | 안드레이 카파시의 조언을 바탕으로 AI가 과도하게 코드를 부풀리거나 주변 코드를 건드리지 않게 제어하는 코딩 효율화 스킬. | [링크](https://github.com/forrestchang/andrej-karpathy-skills) |
| **Ponytail** | 토큰 절약과 불필요한 코드 작성을 줄이기 위한 간결한 시니어 개발자 스타일 코딩 스킬. | [링크](https://github.com/alexphelps/ponytail) |
| **unclebob/ub-mode** | '클린 코드' 저자 로버트 C. 마틴(엉클 밥)의 개발 규율과 TDD 원칙을 에이전트에 적용하는 스킬. | [링크](https://github.com/unclebob/ub-mode) |
| **GoogleChrome/modern-web-guidance-src** | 코딩 에이전트가 오래된 폴리필 대신 최신 HTML·CSS·네이티브 브라우저 API와 Baseline 기준을 쓰도록 돕는 구글 크롬 공식 스킬·CLI. | [링크](https://github.com/GoogleChrome/modern-web-guidance-src) |
| **anthropics/skills (Skill Creator 포함)** | 앤트로픽 공식 에이전트 스킬 모음. 문서(pptx·xlsx 등) 작업 스킬과 스킬 제작·평가용 Skill Creator를 포함. | [링크](https://github.com/anthropics/skills) |
| **Supabase Agent Skills** | Supabase 데이터베이스, 인증, 마이그레이션 등 데이터 저장·관리 작업을 에이전트에 가르치는 공식 스킬 모음. | [링크](https://github.com/supabase/agent-skills) |
| **Vercel Agent Skills** | Next.js, React 서버 컴포넌트 및 배포 최적화를 위한 Vercel Labs 공식 에이전트 스킬 모음. | [링크](https://github.com/vercel-labs/agent-skills) |
| **Google Cloud Skills (google/skills)** | 구글 클라우드(GCP) 서비스 활용법을 100개 이상의 에이전트 스킬로 정리한 공식 저장소. | [링크](https://github.com/google/skills) |
| **android/skills** | CameraX, Jetpack Compose 등 안드로이드 앱 개발용 구글 공식 에이전트 스킬 모음. | [링크](https://github.com/android/skills) |
| **affaan-m/ECC (Everything Claude Code)** | 계획·리뷰·보안 역할의 서브에이전트와 수백 개의 스킬·훅을 통합한 대규모 에이전트 하네스. | [링크](https://github.com/affaan-m/ECC) |
| **Paseo** | Claude Code, Codex 등 여러 코딩 에이전트를 격리된 Git Worktree에서 동시에 돌리고 웹·모바일에서 제어·병합하는 워크스페이스. | [링크](https://github.com/getpaseo/paseo) |
| **Worktrunk** | Git Worktree를 활용해 여러 코딩 AI에 각자 독립된 작업 폴더를 배정하고 완료 후 병합하는 CLI 도구. | [링크](https://github.com/max-sixty/worktrunk) |
| **OpenRig** | 리드 에이전트와 워커 에이전트로 역할을 분담해 작업을 지휘하는 에이전트 오케스트레이션 도구. | [링크](https://github.com/mvschwarz/openrig) |
| **ruflo** | Claude Code와 Codex 위에 올려 다중 에이전트 흐름을 조율하는 오케스트레이션 도구. | [링크](https://github.com/ruvnet/ruflo) |
| **DeepSeek Harness / DSH Desktop** | 모델·도구·스킬·작업 기록을 하나로 묶어 AI 에이전트를 실행하는 플러그인형 하네스 환경. | [링크](https://github.com/deepseek-ai/deepseek-harness) |
| **Google Research Harness²** | 에이전트 실행 환경을 스스로 실험하고 개선하는 자가 개선 하네스 연구 저장소. | [링크](https://github.com/google-research/harness2) |
| **GSD (Get Sh*t Done)** | 스펙 기반 개발과 컨텍스트 윈도우 관리에 초점을 맞춘 AI 코딩 워크플로우 프레임워크. | [링크](https://github.com/gsd-build/get-shit-done) |
| **Agency Agents** | 개발·기획·아키텍처 등 분야별 전문 에이전트 페르소나를 명령어나 데스크톱 앱으로 손쉽게 설치·관리하는 도구. | [링크](https://github.com/msitarzewski/agency-agents) |
| **codex-plugin-cc** | Claude Code 세션 안에서 OpenAI Codex를 직접 호출해 코드 리뷰나 하위 작업을 위임하는 플러그인. | [링크](https://github.com/openai/codex-plugin-cc) |
| **t3code** | 내 PC에 설치된 Claude Code, Codex, Cursor 등을 웹·데스크톱·휴대폰에서 원격 제어하는 UI. | [링크](https://github.com/pingdotgg/t3code) |
| **OpenMausBot** | 메신저 스타일 화면에서 Claude, Codex 등 로컬 코딩 에이전트를 권한 제어와 함께 운영하는 오픈소스 데스크톱 앱. | [링크](https://github.com/milind-soni/OpenMausBot) |
| **Nodeterm** | 여러 AI 에이전트 터미널을 무한 캔버스 위에 노드 형태로 띄워두고 상태를 한눈에 모니터링하는 앱. | [링크](https://github.com/eneskirca/nodeterm) |
| **Hermes Agent** | Nous Research의 오픈소스 로컬 AI 에이전트 및 봇 모드 실행 프레임워크. | [링크](https://github.com/NousResearch/hermes-agent) |
| **codebase-memory-mcp** | Tree-sitter로 코드베이스 전체를 오프라인 지식 그래프로 인덱싱해 탐색 토큰을 크게 줄여주는 로컬 MCP 서버. | [링크](https://github.com/DeusData/codebase-memory-mcp) |
| **Trail-code (구 Graft)** | 로컬에서 함수 호출 지도를 만들어 프롬프트마다 관련 파일 위치를 붙이고 수정 영향 범위(blast radius)를 알려주는 컨텍스트 레이어. | [링크](https://github.com/trailhq/trail-code) |
| **code-review-graph** | 저장소를 의존성 그래프로 구성해 AI가 리뷰에 꼭 필요한 파일만 읽도록 돕는 도구. | [링크](https://github.com/tirth8205/code-review-graph) |
| **open-code-review** | 알리바바 사내 코드 리뷰 경험을 바탕으로 규칙 매칭은 결정적으로, 맥락 판단은 LLM으로 분리한 코드 리뷰 도구. | [링크](https://github.com/alibaba/open-code-review) |
| **plannotator** | 에이전트가 세운 작업 계획과 코드 변경 사항을 브라우저에서 댓글로 검토해 한 번에 피드백을 돌려보내는 도구. | [링크](https://github.com/backnotprop/plannotator) |
| **Understand-Anything** | 대규모 코드베이스를 멀티 에이전트와 Tree-sitter로 탐색해 지식 그래프와 웹 대시보드로 시각화하는 플러그인. | [링크](https://github.com/Egonex-AI/Understand-Anything) |
| **Graphify** | 코드·문서·PDF를 로컬 Tree-sitter 기반 지식 그래프로 매핑해 에이전트 탐색 비용을 줄여주는 CLI 및 스킬. | [링크](https://github.com/Graphify-Labs/graphify) |
| **Archify** | 코드베이스나 시스템 설명을 분석해 아키텍처 다이어그램으로 자동 변환하는 도구. | [링크](https://github.com/archify-ai/archify) |
| **NVIDIA SkillEvaluator** | AI 에이전트 스킬(SKILL.md)의 스키마·보안·실제 성능 향상 효과를 다단계로 검증하는 NVIDIA 오픈소스 평가 프레임워크. | [링크](https://github.com/NVIDIA/SkillEvaluator) |
| **chrome-devtools-mcp** | 에이전트가 실제 Chrome 브라우저를 열어 네트워크, 콘솔, 성능 프로파일까지 직접 점검하는 구글 공식 MCP 서버. | [링크](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| **vercel-labs/agent-desktop** | OS 접근성 트리를 읽어 AI 에이전트가 Mac·Windows·Linux 데스크톱 앱을 직접 조작하도록 돕는 오픈소스 CLI·스킬. | [링크](https://github.com/vercel-labs/agent-desktop) |
| **vercel-labs/agent-browser** | 에이전트가 셸 명령으로 웹 브라우저를 간결하게 탐색·조작할 수 있도록 만든 CLI 도구. | [링크](https://github.com/vercel-labs/agent-browser) |
| **browser-use** | LLM 에이전트가 웹 브라우저의 클릭·입력·스크롤 작업을 자율적으로 수행하도록 연결하는 오픈소스 프레임워크. | [링크](https://github.com/browser-use/browser-use) |
| **Playwright** | 마이크로소프트의 크로스 브라우저 자동화 및 E2E UI 테스트 오픈소스 프레임워크. | [링크](https://github.com/microsoft/playwright) |
| **tester-army/e2e** | 기존 코드 테스트에 자연어 단계를 섞어 작성할 수 있는 E2E 테스트 프레임워크. | [링크](https://github.com/tester-army/e2e) |
| **Google ARTEMIS** | 자연어 지시로 안드로이드 앱 UI를 자동 조작하고 테스트하는 구글의 UI 테스트 에이전트. | [링크](https://github.com/google/artemis) |
| **CLI-Anything** | GUI 프로그램이나 일반 소프트웨어를 CLI 명령으로 감싸 에이전트가 실행할 수 있게 해주는 스킬·도구. | [링크](https://github.com/HKUDS/CLI-Anything) |
| **JetBrains Thinkrail** | JetBrains 인큐베이터에서 공개한 가벼운 데스크톱 AI 코딩 도구 (오픈소스 코딩 에이전트 pi 내장). | [링크](https://github.com/JetBrains/thinkrail) |
| **Open Interpreter** | 로컬 및 오픈 모델이 터미널에서 직접 코드를 실행해 작업을 처리하도록 돕는 오픈소스 코딩 에이전트. | [링크](https://github.com/OpenInterpreter/open-interpreter) |
| **Ghostty** | GPU 가속과 네이티브 UI를 지원하는 빠르고 가벼운 macOS·Linux용 터미널 에뮬레이터. | [링크](https://github.com/ghostty-org/ghostty) |
| **Expo Exact** | React 없이 선언형 뷰 언어로 웹·macOS·iOS·Linux 네이티브 앱을 만드는 AI 친화적 Rust 기반 크로스플랫폼 런타임. | [링크](https://github.com/expo/exact) |
| **drawDB** | 설치 없이 브라우저에서 바로 데이터베이스 ERD를 설계하고 SQL을 생성하는 오픈소스 편집기. | [링크](https://github.com/drawdb-io/drawdb) |
| **Appwrite** | 인증, 데이터베이스, 파일 저장소, 서버 함수, 호스팅을 한 번에 제공하는 오픈소스 백엔드(BaaS) 플랫폼. | [링크](https://github.com/appwrite/appwrite) |
| **Floci** | 외부 클라우드 계정 없이 내 PC에서 AWS·클라우드 환경을 빠르게 에뮬레이션하는 경량 오픈소스 도구. | [링크](https://github.com/floci-io/floci) |
| **Arcane** | 터미널 명령 대신 깔끔한 웹 대시보드에서 Docker 컨테이너·볼륨·Compose 스택을 관리하는 오픈소스 UI. | [링크](https://github.com/getarcaneapp/arcane) |
| **Coder** | 개발자와 AI 에이전트가 Docker·Terraform 기반으로 격리된 원격 개발 환경을 셀프 호스팅하는 플랫폼. | [링크](https://github.com/coder/coder) |
| **Supabase CLI** | 데이터베이스 스키마 마이그레이션, Edge Functions, 인증을 터미널에서 직접 제어하는 공식 CLI. | [링크](https://github.com/supabase/cli) |
| **Vercel CLI** | 프론트엔드·서버리스 배포와 환경 변수를 터미널과 에이전트 루프에서 직접 관리하는 공식 CLI. | [링크](https://github.com/vercel/vercel) |
| **GitHub CLI (gh)** | 이슈, PR, Actions 워크플로우, 릴리스를 터미널에서 에이전트와 함께 제어하는 GitHub 공식 CLI. | [링크](https://cli.github.com/) |
| **Google MCP Toolbox (genai-toolbox)** | 구글이 제공하는 데이터베이스·클라우드 연동용 오픈소스 MCP 서버 툴박스. | [링크](https://github.com/googleapis/genai-toolbox) |
| **awesome-mcp-servers** | 전 세계 개발자들이 만든 Model Context Protocol(MCP) 서버를 분야별로 정리한 대표 큐레이션 목록. | [링크](https://github.com/punkpeye/awesome-mcp-servers) |
| **public-apis** | 개발자와 에이전트 프로젝트에 활용할 수 있는 무료 공개 API를 카테고리별로 모아둔 대표 북마크 저장소. | [링크](https://github.com/public-apis/public-apis) |
| **claude-quickstarts** | Claude API와 에이전트 기반 프로젝트를 빠르게 시작할 수 있도록 Anthropic이 제공하는 공식 템플릿 모음. | [링크](https://github.com/anthropics/claude-quickstarts) |
| **claude-code-tips** | 깃허브에서 화제가 된 Claude Code 실전 활용 팁과 워크플로우 노하우를 정리한 가이드. | [링크](https://github.com/ykdojo/claude-code-tips) |
| **RAD Debugger** | Epic Games가 공개한 다중 프로세스 지원 네이티브 디버거 (Windows 및 Linux 예비 지원). | [링크](https://github.com/EpicGames/raddebugger) |
| **LLVM Project** | Rust, Swift, Clang 등 현대 언어의 최적화와 기계어 생성을 담당하는 공용 컴파일러 인프라. | [링크](https://github.com/llvm/llvm-project) |
| **{fmt}** | 파이썬과 비슷한 직관적인 문법으로 안전하고 빠른 문자열 포매팅을 제공하는 C++ 오픈소스 라이브러리. | [링크](https://github.com/fmtlib/fmt) |
| **Modular Mojo** | 파이썬 문법 친화성과 시스템 언어급 성능을 결합한 AI 개발용 프로그래밍 언어 및 컴파일러. | [링크](https://github.com/modular/modular) |

</details>

<details>
<summary><strong>⚡ 생산성 · 협업 & 비즈니스 (34개)</strong> — 클릭해서 펼치기</summary>

👉 [전체 상세 페이지 보기 (`02-productivity-and-business/README.md`)](02-productivity-and-business/README.md)

| 이름 (Name) | 설명 (Description) | URL |
|---|---|---|
| **OfficeCLI** | 마이크로소프트 오피스 설치 없이 단일 바이너리로 워드·엑셀·파워포인트 문서를 자동 수정하는 CLI 도구. | [링크](https://github.com/iOfficeAI/OfficeCLI) |
| **Taskwarrior** | 터미널에서 가볍고 빠르게 할 일과 이슈를 관리하는 오픈소스 커맨드라인 태스크 트래커. | [링크](https://github.com/GothenburgBitFactory/taskwarrior) |
| **Obsidian** | 마크다운 파일 기반 개인 지식 관리 앱. Claude Code 등 로컬 에이전트와 결합해 개인 비서·위키로 활용. | [링크](https://obsidian.md/) |
| **Meetily** | 클라우드 전송 없이 로컬에서 회의를 실시간 받아쓰고 화자 구분과 요약까지 처리하는 오픈소스 AI 회의 비서. | [링크](https://github.com/meetily-ai/meetily) |
| **i-have-adhd** | AI 에이전트가 긴 서론에 핵심을 묻어버리지 않고 결론부터 명확하게 답하도록 유도하는 응답 스타일 스킬. | [링크](https://github.com/ayghri/i-have-adhd) |
| **claude-mem** | 세션이 종료되면 맥락이 사라지는 문제를 보완해 작업 내용을 요약 저장하고 다음 세션에 필요한 만큼 복원하는 도구. | [링크](https://github.com/thedotmack/claude-mem) |
| **OpenViking** | AI 에이전트가 장기 맥락과 지식을 체계적으로 저장·조회할 수 있도록 설계된 컨텍스트 데이터베이스. | [링크](https://github.com/volcengine/OpenViking) |
| **Hindsight** | 에이전트의 과거 작업 기록과 회고 내용을 축적해 이후 판단에 반영하는 기억 시스템. | [링크](https://github.com/vectorize-io/hindsight) |
| **context-mode** | 코딩 에이전트의 컨텍스트 창이 불필요한 출력으로 빠르게 차는 현상을 줄여주는 보조 도구. | [링크](https://github.com/mksglu/context-mode) |
| **WeKnora** | 사내 문서를 넣으면 AI 에이전트가 상호 연결된 구조화 위키로 자동 정리해 주는 텐센트 오픈소스 지식 플랫폼. | [링크](https://github.com/Tencent/WeKnora) |
| **Semantica** | AI가 대화와 문서의 맥락을 지식 그래프로 기억하고 답변의 출처 근거까지 추적하게 하는 메모리 인프라. | [링크](https://github.com/semantica-ai) |
| **NVIDIA Auto-Ontology** | 사내 DB 스키마와 비즈니스 용어를 온톨로지로 컴파일해 자연어 질문을 정확한 SQL로 변환하는 오픈소스 프레임워크. | [링크](https://github.com/NVIDIA/auto-ontology) |
| **Agent-Reach** | 유료 공식 API 없이도 트위터(X), 레딧, 유튜브 등 주요 플랫폼의 웹 정보를 에이전트가 직접 수집·열람하게 돕는 도구. | [링크](https://github.com/Panniantong/agent-reach) |
| **Firecrawl** | 웹페이지를 LLM이 읽기 좋은 마크다운과 구조화 데이터로 변환하는 에이전트 특화 크롤링·검색 도구. | [링크](https://github.com/firecrawl/firecrawl) |
| **Scrapling** | 웹페이지 구조가 바뀌어도 원하는 요소를 스스로 다시 찾아내는 적응형 파이썬 크롤러 (MCP 연동 지원, 사용 시 사이트 약관 준수 필요). | [링크](https://github.com/D4Vinci/Scrapling) |
| **last30days-skill** | 최근 30일간의 레딧·X·유튜브·해커뉴스 여론과 논의를 모아 한 장의 리포트로 요약해 주는 리서치 스킬. | [링크](https://github.com/mvanhorn/last30days-skill) |
| **NotebookLM Skill (NotebookLM-PI)** | Google NotebookLM 리서치 워크플로우를 Claude Code 터미널 환경에서 연동해 활용하는 스킬. | [링크](https://github.com/PleasePrompto/notebooklm-skill) |
| **marketingskills** | 전환율 최적화(CRO), 카피라이팅, SEO 등 마케터 실무용 에이전트 스킬 50여 종 모음. | [링크](https://github.com/coreyhaines31/marketingskills) |
| **claude-seo** | Claude Code용 SEO·GEO(생성형 검색 최적화) 점검 플러그인. 기술 감사, 스키마, 보안 노출 점검까지 지원. | [링크](https://github.com/AgriciDaniel/claude-seo) |
| **open-seo** | 웹사이트의 검색엔진 최적화 상태를 자동 점검하는 오픈소스 SEO 감사 도구. | [링크](https://github.com/open-seo) |
| **anthropics/knowledge-work-plugins** | 영업, 법무, 운영 등 비개발 직무별 업무 흐름을 지원하는 앤트로픽 공식 플러그인 모음. | [링크](https://github.com/anthropics/knowledge-work-plugins) |
| **anthropics/financial-services** | 투자 은행 및 자산관리 실무 분석을 위해 앤트로픽이 공개한 금융 특화 에이전트 모음. | [링크](https://github.com/anthropics/financial-services) |
| **Sure (we-promise/sure)** | 상업용 가계부 앱 Maybe Finance를 커뮤니티가 이어받아 발전시킨 자체 호스팅 오픈소스 개인 금융·가계부 웹앱. | [링크](https://github.com/we-promise/sure) |
| **daily_stock_analysis** | 관심 종목의 시세와 뉴스를 매일 수집해 LLM이 리포트를 작성하고 메신저·메일로 발송하는 자동화 도구 (학습·참고용). | [링크](https://github.com/ZhuLinsen/daily_stock_analysis) |
| **Vibe-Trading** | 자연어로 트레이딩 전략을 지시하고 백테스트·시뮬레이션을 수행하는 오픈소스 개인 트레이딩 에이전트 프레임워크. | [링크](https://github.com/HKUDS/Vibe-Trading) |
| **Kronos** | 금융 차트 데이터를 학습해 주가 흐름을 예측하는 연구용 모델 (실제 매매용 아님). | [링크](https://github.com/shiyu-coder/Kronos) |
| **Google TimesFM** | 구글 리서치가 공개한 시계열 데이터 예측 전용 파운데이션 모델. | [링크](https://github.com/google-research/timesfm) |
| **JobFinderOS (AI Job Search)** | Claude Code 위에서 채용 공고 평가, 이력서 맞춤 수정, 자소서·면접 준비를 자동화하는 AI 구직 비서. | [링크](https://github.com/matthewprice/JobFinderOS) |
| **Block Buzz** | Block(구 Square)이 공개한 사람과 AI 에이전트가 같은 채널에서 함께 일하는 협업 플랫폼. | [링크](https://github.com/block) |
| **Macro Workspace** | 메일, 채팅, 문서, 할 일, 에이전트를 한 작업공간에 모으고 공유 AI 메모리로 연결하는 협업 앱. | [링크](https://github.com/macro-org) |
| **ha-mcp (Home Assistant MCP)** | 스마트홈 플랫폼 Home Assistant를 Claude·ChatGPT에 연결해 자연어로 기기 제어와 자동화를 구성하는 MCP 서버. | [링크](https://github.com/homeassistant-ai/ha-mcp) |
| **AIRI** | 실시간 음성 대화와 Minecraft 플레이까지 지원하는 셀프호스팅 오픈소스 AI 컴패니언. | [링크](https://github.com/moeru-ai/airi) |
| **WorldMonitor** | 65개 이상의 실시간 글로벌 API 데이터를 3D 지구본 위에 시각화하는 오픈소스 대시보드 (AGPL). | [링크](https://github.com/koala73/worldmonitor) |
| **God's Eye View** | 실제 항공·선박·위성·교통 데이터를 3D 지구본에 올려 브라우저에서 관측하는 시각화 도구. | [링크](https://github.com/bilawalsidhu/gods-eye-view) |

</details>

<details>
<summary><strong>🎨 미디어 · 디자인 & 크리에이티브 (44개)</strong> — 클릭해서 펼치기</summary>

👉 [전체 상세 페이지 보기 (`03-media-and-creative/README.md`)](03-media-and-creative/README.md)

| 이름 (Name) | 설명 (Description) | URL |
|---|---|---|
| **HyperFrames** | 에이전트가 작성한 HTML/CSS/GSAP 코드를 헤드리스 크롬으로 결정론적 영상으로 렌더링하는 코드형 비디오 엔진. | [링크](https://github.com/heygen/hyperframes) |
| **Remotion** | React 코드로 모션그래픽과 영상을 프로그래밍 방식으로 제작·렌더링하는 대표 오픈소스 프레임워크. | [링크](https://www.remotion.dev/showcase) |
| **OpenMontage** | 참고 릴스 분석부터 기획·편집까지 다중 에이전트 파이프라인으로 영상을 자동 제작하는 오픈소스 도구. | [링크](https://github.com/calesthio/OpenMontage) |
| **MoneyPrinterTurbo** | 주제 한 줄만 입력하면 대본, 음성, 자막, 배경음악까지 결합된 숏폼 영상을 자동 생성하는 오픈소스 도구. | [링크](https://github.com/harry0703/MoneyPrinterTurbo) |
| **video-use** | 타임스탬프 자막을 분석해 코딩 에이전트가 영상 컷 편집 목록을 작성하고 편집하게 돕는 도구. | [링크](https://github.com/browser-use/video-use) |
| **claude-video** | 영상 파일에서 프레임 이미지와 자막을 추출해 Claude가 시각적으로 분석할 수 있게 돕는 도구. | [링크](https://github.com/bradautomates/claude-video) |
| **OpenCut** | 브라우저에서 가볍게 실행되는 오픈소스 웹 기반 영상 편집기. | [링크](https://github.com/opencut-app/opencut) |
| **ArtCraft** | 2D 합성 및 3D 무대·포즈·카메라 구도를 직접 잡은 뒤 60여 종 AI 모델로 영상을 생성하는 오픈소스 데스크톱 IDE. | [링크](https://github.com/storytold/artcraft) |
| **Lemo-Opuscar** | Claude Code에서 영화 스타일의 영상 연출과 구성을 보조하는 크리에이티브 도구함. | [링크](https://github.com/lemomo-ai/lemo-opuscar) |
| **Manim (Community)** | 수학·알고리즘·기술 설명용 2D/3D 애니메이션을 파이썬 코드로 렌더링하는 오픈소스 엔진 (Claude Code 연동 활용). | [링크](https://github.com/ManimCommunity/manim) |
| **Opus 5.5 Motion Graphic Collection (claudevideo.org)** | Claude Opus 5.5로 제작된 코드 기반 모션그래픽 영상과 프롬프트를 모아둔 레퍼런스 컬렉션. | [링크](https://claudevideo.org/) |
| **awesome-opus5-5-videos** | 커뮤니티가 Claude Opus 5.5로 제작한 화제의 모션그래픽 영상과 프롬프트 큐레이션 저장소. | [링크](https://github.com/yihui-dev/awesome-opus5-5-videos) |
| **Skillry Motion Graphics Reference** | Opus 5.5 코드 렌더링 영상 사례와 프롬프트 구성을 함께 열람할 수 있는 레퍼런스 사이트. | [링크](https://skillry.dev/ai-videos/opus-5-5) |
| **Prompt Motion** | 코드 기반 AI 모션그래픽 제작을 위한 프롬프트 패턴과 레퍼런스 모음. | [링크](https://prompt-motion.com/) |
| **리틱체 (REATIC Font)** | 타이틀 디자인과 모션그래픽 스트레치 효과에 특화된 상업적 무료 한글 폰트 패밀리 (9종). | [링크](https://noonnu.cc/) |
| **Voicebox** | 목소리 클로닝부터 음성 받아쓰기까지 지원하는 오픈소스 AI 보이스 스튜디오. | [링크](https://github.com/jamiepine/voicebox) |
| **VoiceStudio** | 외부 서버 없이 로컬에서 음성을 생성하고 녹음·잘라내기·편집까지 지원하는 오픈소스 보이스 도구. | [링크](https://github.com/debpalash/VoiceStudio) |
| **Chatterbox (Chatterbox-nano)** | 일반 노트북에서도 가볍게 구동할 수 있는 Resemble AI의 오픈소스 음성합성(TTS) 모델. | [링크](https://github.com/resemble-ai/chatterbox) |
| **ACE-Step** | 허깅페이스와 깃허브에 공개된 오픈소스 AI 음악·작곡 생성 모델. | [링크](https://github.com/ace-step/ACE-Step) |
| **Suno** | 가사와 스타일 프롬프트만으로 보컬 포함 완성곡을 생성하는 대표 AI 작곡 서비스. | [링크](https://suno.com/) |
| **Deepgram Nova-3 / ElevenLabs / Cartesia Sonic** | 초저지연 받아쓰기(Deepgram Nova-3), 한국어 자연어 합성(ElevenLabs v3), 실시간 음성(Cartesia Sonic) 등 상용 음성 API. | [링크](https://deepgram.com/) |
| **ComfyUI** | 생성형 AI 모델과 연산을 노드(Node) 그래프로 연결해 이미지·비디오·3D·오디오 워크플로를 구축하는 대표 오픈소스 GUI 엔진. | [링크](https://github.com/comfyanonymous/ComfyUI) |
| **Meta Segment Anything (SAM)** | 텍스트나 클릭만으로 이미지·영상 속 특정 물체를 분리하고 배경을 제거하는 메타의 세그멘테이션 모델. | [링크](https://github.com/facebookresearch/segment-anything) |
| **HiDream** | 로컬 GPU 환경에서 고품질 이미지를 직접 생성할 수 있는 오픈소스 이미지 생성 모델. | [링크](https://github.com/HiDream-ai/HiDream-I1) |
| **Compositor** | 약 8~10MB의 초경량 용량으로 동작하는 macOS용 오픈소스 포토샵 대안 이미지 편집기. | [링크](https://github.com/robbietilton/Compositor) |
| **WaterMarks-Remover** | 이미지 워터마크 제거와 메타데이터 정리를 지원하는 오픈소스 유틸리티. | [링크](https://github.com/guillaumemeyer/watermarks-remover) |
| **TRELLIS.2 (Microsoft)** | 사진이나 문장으로 고품질 3D 에셋을 생성하고 재질이나 일부 영역만 부분 수정할 수 있는 마이크로소프트 오픈소스 3D 모델. | [링크](https://github.com/microsoft/TRELLIS.2) |
| **Modly** | 로컬 그래픽카드를 활용해 이미지나 프롬프트에서 3D 모델을 생성하는 오픈소스 도구. | [링크](https://github.com/lightningpixel/modly) |
| **Rodin Gen-2.5 (Hyper3D)** | 단일 이미지나 텍스트에서 정교한 3D 메시와 텍스처를 생성하는 상용 3D 생성 플랫폼. | [링크](https://hyper3d.ai/) |
| **text-to-cad** | 자연어 설명으로 3D 부품을 설계하고 STEP·STL·3MF·GLB 파일로 출력하는 오픈소스 CAD 도구. | [링크](https://github.com/earthtojake/text-to-cad) |
| **Pascal Editor** | 브라우저에서 바로 실행되며 MCP와 에이전트 스킬을 기본 지원하는 오픈소스 3D 건축 설계 도구. | [링크](https://github.com/pascalorg/editor) |
| **Three.js** | 웹 브라우저에서 WebGL·WebGPU 기반 3D 씬과 인터랙티브 그래픽을 구현하는 표준 자바스크립트 라이브러리. | [링크](https://github.com/mrdoob/three.js) |
| **Anime.js** | 가볍고 직관적인 문법으로 웹 2D·SVG·CSS 애니메이션을 구현하는 MIT 라이선스 라이브러리. | [링크](https://github.com/juliangarnier/anime) |
| **react-force-graph** | 2D·3D·VR 환경에서 노드-엣지(Node-Edge) 지식 그래프를 인터랙티브하게 시각화하는 React 라이브러리. | [링크](https://github.com/vasturiano/react-force-graph) |
| **Meta Astryx** | 메타가 사내에서 8년간 사용해 온 React 19 + StyleX 기반 디자인 시스템. 에이전트가 CLI·MCP로 공식 부품을 조회해 환각을 방지. | [링크](https://github.com/meta/astryx) |
| **impeccable** | 코딩 에이전트가 뽑아내는 평범한 UI를 polish·bolder·critique·audit 명령으로 세련되게 다듬는 디자인 언어 스킬. | [링크](https://github.com/pbakaus/impeccable) |
| **taste-skill** | AI 코딩 에이전트에게 구체적인 시각적 취향과 Anti-Slop 프론트엔드 기준을 심어주는 디자인 스킬. | [링크](https://github.com/Leonxlnx/taste-skill) |
| **ui-ux-pro-max-skill** | 50여 종 UI 스타일, 색상 팔레트, 타이포그래피, UX 가이드라인을 에이전트에 제공하는 종합 디자인 스킬. | [링크](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| **Nutlope/hallmark** | 기존 글꼴·색을 읽고 50개 테마 후보와 8개 브라우저 폭 검사를 거쳐 AI 티 나는 디자인을 개선하는 스킬. | [링크](https://github.com/Nutlope/hallmark) |
| **jakubkrehel/skills** | 디자인 엔지니어 Jakub Krehel의 여백·글꼴·색·접근성·문구 점검 UI 스킬 14종 모음. | [링크](https://github.com/jakubkrehel/skills) |
| **google-labs-code/stitch-skills** | 구글 Stitch 디자인 시스템과 MCP를 연동해 일관된 멀티페이지 UI를 생성하는 공식 스킬 모음. | [링크](https://github.com/google-labs-code/stitch-skills) |
| **diagram-design** | Claude Code로 27종의 고품질 아키텍처·개념 다이어그램을 자체완결 HTML로 생성하는 스킬. | [링크](https://github.com/cathrynlavery/diagram-design) |
| **kill-ai-slop** | AI가 생성한 UI와 디자인 결과물에서 천편일률적인 AI 특유의 느낌을 걷어내는 보정 스킬. | [링크](https://github.com/yetone/kill-ai-slop) |
| **im-not-ai / humanizer** | AI가 작성한 글의 번역투와 기계적 패턴을 자연스러운 사람 문체로 다듬어 주는 글쓰기 후처리 스킬. | [링크](https://github.com/blader/humanizer) |

</details>

<details>
<summary><strong>🎮 게임 개발 & 에셋 제작 (12개)</strong> — 클릭해서 펼치기</summary>

👉 [전체 상세 페이지 보기 (`04-game-dev/README.md`)](04-game-dev/README.md)

| 이름 (Name) | 설명 (Description) | URL |
|---|---|---|
| **pixelfx** | 이미지 파일 없이 코드로 불·폭발·얼음·번개 등 244종 픽셀 이펙트를 렌더링하고 투명 스프라이트 시트로 내보내는 MIT 라이브러리. | [링크](https://github.com/patch-gg/pixelfx) |
| **sprite-gen** | 그림 한 장에서 배경이 투명한 2D 게임 스프라이트 시트와 반복 동작 아틀라스를 생성·정렬하는 Python CLI 및 에이전트 스킬. | [링크](https://github.com/aldegad/sprite-gen) |
| **PerfectPixel Studio** | AI 생성 스프라이트의 배경 번짐과 프레임 떨림을 크로마키 매팅·무게중심 정렬·자동 검증 루프로 보정하는 스튜디오 앱. | [링크](https://github.com/gykim80/perfectpixel-studio) |
| **Agent Sprite Forge** | 마스터 캐릭터 이미지 한 장으로 대기·걷기·달리기·공격 동작 시트와 맵·타일 리소스를 투명 PNG·GIF로 제작하는 에이전트 스킬. | [링크](https://github.com/0x0funky/agent-sprite-forge) |
| **Codixel** | 참고 이미지를 도트 캐릭터로 변환하고 배경 제거·색상 양자화·코드 기반 애니메이션을 붙이는 Claude Code 스킬. | [링크](https://github.com/mankidev/codixel) |
| **Pixelbolt** | 색·모양·움직임이 담긴 JSON 설계도로 결정론적 도트 스프라이트·타일·이펙트를 렌더링하는 CLI·웹 스튜디오·MCP 서버. | [링크](https://github.com/skulitom/Pixelbolt) |
| **Sprite Sheet Diffusion** | 로컬 GPU에서 캐릭터 참고 이미지와 자세 순서를 입력해 일관된 2D 동작 프레임을 생성하는 확산 모델. | [링크](https://github.com/chenganhsieh/Sprite-Sheet-Diffusion) |
| **Game-Dev Agentic Skills** | Godot 4.7+와 Bevy 엔진용 에이전트 스킬 및 장르별 설계도 모음 (필요한 스킬을 골라 선택 설치 권장). | [링크](https://github.com/thedivergentai/Game-Dev-Agentic-Skills) |
| **Claude Code Game Studios** | 기획·엔지니어링·QA 등 역할별 서브에이전트 체계를 구성해 Claude Code를 1인 게임 개발 스튜디오처럼 운영하는 프레임워크. | [링크](https://github.com/Donchitos/Claude-Code-Game-Studios) |
| **Kenney Assets** | 2D 스프라이트, 타일맵, UI, 3D 로우폴리 모델, 효과음을 CC0(퍼블릭 도메인) 무료 라이선스로 제공하는 인디게임 표준 에셋 라이브러리. | [링크](https://kenney.nl/assets) |
| **Higgsfield Playable** | 텍스트나 참고 게임 플레이 영상을 바탕으로 실행 가능한 브라우저 게임 코드와 리소스를 함께 생성하는 프로토타이핑 서비스. | [링크](https://higgsfield.ai/playable) |
| **AnyPS5** | PS5 실행 파일을 에뮬레이터 없이 Linux·Windows용으로 다시 링크하는 실험적 오픈소스 프로젝트. | [링크](https://github.com/boykopovar/AnyPS5) |

</details>

<details>
<summary><strong>📚 교육 · 학습 & 연구 (12개)</strong> — 클릭해서 펼치기</summary>

👉 [전체 상세 페이지 보기 (`05-education-and-research/README.md`)](05-education-and-research/README.md)

| 이름 (Name) | 설명 (Description) | URL |
|---|---|---|
| **Microsoft AI-For-Beginners** | PyTorch와 TensorFlow를 함께 다루는 마이크로소프트의 24강 무료 AI 입문 커리큘럼. | [링크](https://github.com/microsoft/AI-For-Beginners) |
| **LLM Agent Book (AI-Agent-Book)** | AI 에이전트 아키텍처 설계 이론과 90여 개 실습 코드를 무료 공개한 오픈소스 교재. | [링크](https://github.com/kyopark2014/llm-agent-book) |
| **500+ AI/ML/DL Projects with Code** | 기초 선형대수부터 딥러닝·컴퓨터 비전·자율 에이전트까지 수백 개 실습 코드를 모은 오픈 학습 저장소. | [링크](https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code) |
| **awesome-llm-apps** | 100개 이상의 AI 에이전트와 RAG 앱 예제를 복제해 바로 실행해 볼 수 있는 실전 레퍼런스 저장소. | [링크](https://github.com/Shubhamsaboo/awesome-llm-apps) |
| **nanochat (Andrej Karpathy)** | 단일 스크립트로 데이터 준비부터 학습·대화까지 미니 ChatGPT를 직접 만들어 보는 카파시의 교육용 오픈소스. | [링크](https://github.com/karpathy/nanochat) |
| **DeepTutor** | 학습자의 이력을 누적 기억해 개인 맞춤형 커리큘럼을 생성해 주는 오픈소스 개인 과외 AI. | [링크](https://github.com/HKUDS/DeepTutor) |
| **OpenMAIC** | 주제를 입력하면 슬라이드·퀴즈·시뮬레이션을 만들고 AI 선생님과 반 친구들이 토론 수업을 진행하는 AI 교실 플랫폼. | [링크](https://github.com/OpenMAIC/OpenMAIC) |
| **book-to-skill** | 기술서 PDF를 챕터별로 분할해 필요할 때만 적은 토큰으로 호출하는 에이전트 스킬로 변환 (저작권상 무단 배포 금지). | [링크](https://github.com/virgiliojr94/book-to-skill) |
| **academic-research-skills** | 문헌 조사부터 구조화, 초안 작성, 마무리 검증까지 이어지는 학술 논문 연구 파이프라인 스킬. | [링크](https://github.com/Imbad0202/academic-research-skills) |
| **PaperOrchestra** | 문헌 조사·도표 생성·개요·집필 역할을 여러 에이전트로 분담해 학술 논문 작성을 보조하는 멀티 에이전트 파이프라인. | [링크](https://github.com/Ar9av/PaperOrchestra) |
| **Scientific Agent Skills** | 생물·화학·의학·물리·데이터 분석 도구 사용법과 검증 절차를 160여 종의 스킬로 정리한 과학 연구 저장소. | [링크](https://github.com/K-Dense-AI/scientific-agent-skills) |
| **System Prompts Leaks Archive** | Claude, GPT, Gemini 등 주요 AI 서비스의 공개된 시스템 프롬프트 설계 패턴을 학습용으로 모아둔 저장소. | [링크](https://github.com/LouisShark/chatgpt_system_prompt) |

</details>

<details>
<summary><strong>🖥️ 로컬 AI · 모델 서빙 & 인프라 (22개)</strong> — 클릭해서 펼치기</summary>

👉 [전체 상세 페이지 보기 (`06-local-ai-and-infra/README.md`)](06-local-ai-and-infra/README.md)

| 이름 (Name) | 설명 (Description) | URL |
|---|---|---|
| **llama.cpp** | GGUF 포맷 기반으로 일반 PC와 서버에서 로컬 LLM을 빠르고 정밀하게 추론하는 C/C++ 표준 엔진. | [링크](https://github.com/ggml-org/llama.cpp) |
| **vLLM** | PagedAttention 기반으로 대규모 동시 요청을 고처리량으로 서빙하는 프로덕션 LLM 추론 엔진. | [링크](https://github.com/vllm-project/vllm) |
| **Strata** | 초거대 로컬 MoE 모델을 소비자 하드웨어에서 효율적으로 구동하기 위한 로컬 추론 엔진. | [링크](https://github.com/Niko1221/Strata) |
| **Colibri** | 수천억 파라미터급 초대형 모델을 RAM에 다 올리지 않고 필요한 부분만 SSD 디스크에서 꺼내 구동하는 로컬 LLM 엔진. | [링크](https://github.com/JustVugg/colibri) |
| **AirLLM** | 모델 레이어를 한 장씩만 GPU 메모리에 올려 적은 VRAM에서도 대형 LLM을 추론할 수 있게 해주는 도구. | [링크](https://github.com/lyogavin/airllm) |
| **FreeToken** | 자주 쓰는 모델 가중치만 GPU에 올려 8GB 노트북에서도 로컬 대형 코딩 모델을 빠르게 실행하는 추론 도구 (Linux+NVIDIA). | [링크](https://github.com/FlashML-org/FreeToken) |
| **Unsloth** | 로컬 GPU 환경에서 LLM 파인튜닝 속도를 높이고 메모리 사용량을 크게 줄여주는 오픈소스 학습 라이브러리. | [링크](https://github.com/unslothai/unsloth) |
| **Open WebUI** | 내 PC에 설치해 ChatGPT처럼 로컬·API 모델을 사용하고 실시간 음성 대화까지 지원하는 오픈소스 웹 인터페이스. | [링크](https://github.com/open-webui/open-webui) |
| **OmniRoute** | 수백 개의 LLM 모델을 하나의 통합 API 엔드포인트로 라우팅하는 MIT 라이선스 오픈소스 게이트웨이. | [링크](https://github.com/cheaper-inference/OmniRoute) |
| **freellmapi** | 무료 티어를 제공하는 34개 제공사와 600여 개 모델 엔드포인트를 개인 실험용으로 정리한 저장소. | [링크](https://github.com/tashfeenahmed/freellmapi) |
| **Cactus Compute (Needle & Mirage)** | 스마트폰·웨어러블·브라우저에서 도는 14MB 도구호출 모델(Needle)과 22MB 비전·OCR 모델(Mirage) 초경량 에지 AI 스위트. | [링크](https://github.com/cactus-compute/cactus) |
| **MarkItDown (Microsoft)** | PDF, Word, Excel, PowerPoint 등 다양한 문서를 LLM이 읽기 좋은 마크다운으로 초고속 변환하는 마이크로소프트 도구. | [링크](https://github.com/microsoft/markitdown) |
| **Docling (IBM)** | 표 구조와 스캔 문서 인식 정확도가 뛰어난 IBM 오픈소스 문서 파싱 라이브러리. | [링크](https://github.com/docling-project/docling) |
| **PaddleOCR (PaddleOCR-VL)** | 스캔본, 표, 순서도, 사진 속 숫자 인식에 강점을 가진 오픈소스 다국어 OCR 엔진. | [링크](https://github.com/PaddlePaddle/PaddleOCR) |
| **MinerU 2.5** | 복잡한 학술 논문과 PDF 문서를 수식·표 포함 마크다운으로 깔끔하게 추출하는 오픈소스 문서 OCR 도구. | [링크](https://github.com/opendatalab/MinerU) |
| **NVIDIA OpenShell** | AI 에이전트의 파일·프로세스·네트워크 접근과 자격 증명을 정책 기반으로 격리하는 NVIDIA 오픈소스 샌드박스. | [링크](https://github.com/NVIDIA/OpenShell) |
| **CubeSandbox** | AI 에이전트가 실행하는 코드를 안전하게 격리하는 텐센트 클라우드 기반 초경량 샌드박스. | [링크](https://github.com/TencentCloud/CubeSandbox) |
| **Flue** | 에이전트 실행 환경을 가볍게 격리해 안전한 자동화 작업을 지원하는 오픈소스 샌드박스. | [링크](https://github.com/withastro/flue) |
| **Omarchy v4.0** | Basecamp(Omacom 재단)가 개발자 환경에 맞춰 구성한 Arch 기반 리눅스 배포판. | [링크](https://github.com/omacom/omarchy) |
| **Hyprland** | 부드러운 애니메이션과 자동 타일링 레이아웃을 제공하는 Wayland 기반 리눅스 창 관리자. | [링크](https://github.com/hyprwm/Hyprland) |
| **OpenLogi** | 무거운 Logitech Options+를 대체하기 위해 Rust로 작성된 가벼운 오픈소스 마우스·키보드 설정 도구. | [링크](https://github.com/AprilNEA/OpenLogi) |
| **DiscImageStudio** | 이미지를 CD·DVD·BD-R 광학 디스크 기록면에 직접 새길 수 있는 디스크 이미지로 변환하는 오픈소스 도구. | [링크](https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio) |

</details>

<details>
<summary><strong>🛡️ 보안 · 역공학 & OSINT (12개)</strong> — 클릭해서 펼치기</summary>

👉 [전체 상세 페이지 보기 (`07-security-and-osint/README.md`)](07-security-and-osint/README.md)

| 이름 (Name) | 설명 (Description) | URL |
|---|---|---|
| **openai/codex-security** | 저장소의 위협 모델을 세우고 취약점 후보를 샌드박스에서 검증한 뒤 패치까지 제안하는 OpenAI 공식 보안 CLI·SDK. | [링크](https://github.com/openai/codex-security) |
| **Cloudflare security-audit-skill** | 코딩 에이전트를 독립적이고 일관된 보안 감사관으로 동작하게 만드는 Cloudflare 오픈소스 다단계 감사 스킬. | [링크](https://github.com/cloudflare/security-audit-skill) |
| **NVIDIA SkillSpector** | 외부에서 받은 AI 에이전트 스킬 내부의 악성 명령이나 프롬프트 인젝션을 탐지하는 NVIDIA 보안 스캐너. | [링크](https://github.com/NVIDIA/SkillSpector) |
| **Claude-BugHunter** | 버그 바운티와 모의 해킹 점검 절차를 정리한 스킬 묶음 (반드시 본인 소유 또는 서면 허가를 받은 자산에만 사용). | [링크](https://github.com/elementalsouls/Claude-BugHunter) |
| **Craft Anything** | 외부 동작과 화면을 관찰해 클린룸(Study→Build→Check) 방식으로 분석·재구현하는 Rust 기반 MCP·CLI 엔진 (저작권·약관 준수 필수). | [링크](https://github.com/storytold/craft-anything) |
| **REA (Reverse Engineer Anything)** | 실행 파일·앱·웹사이트의 구조와 동작 원리를 로컬에서 분석하는 역공학 MCP 도구 겸 스킬 (법·라이선스 확인 필수). | [링크](https://github.com/morluto/rea) |
| **reverse-skill** | IDA, Ghidra 같은 역공학·모의침투 워크플로우 스킬 20여 개를 단일 라우터로 연결한 스킬 모음. | [링크](https://github.com/zhaoxuya520/reverse-skill) |
| **Ghidra** | 미국 국가안보국(NSA)이 오픈소스로 공개한 대표 소프트웨어 리버스 엔지니어링 분석 프레임워크. | [링크](https://github.com/NationalSecurityAgency/ghidra) |
| **Sherlock** | 400개 이상의 웹사이트에서 특정 아이디(Username) 사용 여부를 조회하는 오픈소스 OSINT 도구. | [링크](https://github.com/sherlock-project/sherlock) |
| **Holehe** | 이메일 주소 하나로 어떤 온라인 서비스에 가입되어 있는지 확인하는 개인 보안 점검용 OSINT 도구. | [링크](https://github.com/megadose/holehe) |
| **authentik** | SSO, OAuth2, SAML, LDAP를 지원하는 셀프호스팅 오픈소스 통합 인증(IdP) 서버. | [링크](https://github.com/goauthentik/authentik) |
| **Heretic** | 재학습 없이 오픈 웨이트 모델의 과도한 거절 성향이나 상투적 말투를 조정하는 연구용 도구 (윤리·안전 범위 내 사용). | [링크](https://github.com/p-e-w/heretic) |

</details>

## 📝 관련 블로그 & 데이터 구조

- **블로그 허브 포스트:** [AI 스킬·도구·앱 총정리 허브 (hellollama)](https://godstale.mycafe24.com/?p=1115) — 도구별 심층 분석, 비교표, 실전 세팅 가이드는 워드프레스 블로그와 함께 동기화되어 관리됩니다.
- **단일 데이터 소스:** [`data/tools.json`](data/tools.json) (`name`, `description`, `url` 필수 구조)
- **문서 자동 생성:** `python scripts/build_docs.py` 실행 시 루트 `README.md`, 카테고리별 `README.md`, 웹 검색 데이터(`docs/tools.json`)가 일괄 갱신됩니다.
