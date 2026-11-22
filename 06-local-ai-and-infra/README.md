# 🖥️ 로컬 AI · 모델 서빙 & 인프라 (Local AI, Serving & Infrastructure)

> 로컬 LLM 추론·파인튜닝 엔진, LLM 게이트웨이, 초경량 온디바이스 모델, 문서 파싱/OCR, 에이전트 샌드박스

[🏠 메인으로 돌아가기](../README.md) · [🔍 웹에서 실시간 검색하기](https://godstale.github.io/Agent-Toolbox/?cat=06-local-ai-and-infra) · [📂 GitHub 내 검색](https://github.com/godstale/Agent-Toolbox/search?q=path%3A06-local-ai-and-infra)

총 **22개** 항목 수록 · 최종 업데이트: `2026-11-22`

## 세부 분류 목차

- [로컬 LLM 추론 & 파인튜닝 엔진](#로컬-llm-추론-파인튜닝-엔진) (8)
- [LLM 게이트웨이 & 초경량 모델](#llm-게이트웨이-초경량-모델) (3)
- [문서 파싱 & OCR](#문서-파싱-ocr) (4)
- [에이전트 샌드박스 & OS 유틸리티](#에이전트-샌드박스-os-유틸리티) (7)

## 로컬 LLM 추론 & 파인튜닝 엔진

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **llama.cpp** | GGUF 포맷 기반으로 일반 PC와 서버에서 로컬 LLM을 빠르고 정밀하게 추론하는 C/C++ 표준 엔진. ([심층 가이드](https://godstale.mycafe24.com/?p=1100)) | `Framework/Harness` | [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) |
| **vLLM** | PagedAttention 기반으로 대규모 동시 요청을 고처리량으로 서빙하는 프로덕션 LLM 추론 엔진. ([심층 가이드](https://godstale.mycafe24.com/?p=1100)) | `Framework/Harness` | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) |
| **Strata** | 초거대 로컬 MoE 모델을 소비자 하드웨어에서 효율적으로 구동하기 위한 로컬 추론 엔진. ([심층 가이드](https://godstale.mycafe24.com/?p=1100)) | `Framework/Harness` | [github.com/Niko1221/Strata](https://github.com/Niko1221/Strata) |
| **Colibri** | 수천억 파라미터급 초대형 모델을 RAM에 다 올리지 않고 필요한 부분만 SSD 디스크에서 꺼내 구동하는 로컬 LLM 엔진. ([심층 가이드](https://godstale.mycafe24.com/?p=1155)) | `Framework/Harness` | [github.com/JustVugg/colibri](https://github.com/JustVugg/colibri) |
| **AirLLM** | 모델 레이어를 한 장씩만 GPU 메모리에 올려 적은 VRAM에서도 대형 LLM을 추론할 수 있게 해주는 도구. | `Library` | [github.com/lyogavin/airllm](https://github.com/lyogavin/airllm) |
| **FreeToken** | 자주 쓰는 모델 가중치만 GPU에 올려 8GB 노트북에서도 로컬 대형 코딩 모델을 빠르게 실행하는 추론 도구 (Linux+NVIDIA). ([심층 가이드](https://godstale.mycafe24.com/?p=1155)) | `Framework/Harness` | [github.com/FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) |
| **Unsloth** | 로컬 GPU 환경에서 LLM 파인튜닝 속도를 높이고 메모리 사용량을 크게 줄여주는 오픈소스 학습 라이브러리. ([심층 가이드](https://godstale.mycafe24.com/?p=848)) | `Library` | [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth) |
| **Open WebUI** | 내 PC에 설치해 ChatGPT처럼 로컬·API 모델을 사용하고 실시간 음성 대화까지 지원하는 오픈소스 웹 인터페이스. | `App` | [github.com/open-webui/open-webui](https://github.com/open-webui/open-webui) |

## LLM 게이트웨이 & 초경량 모델

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **OmniRoute** | 수백 개의 LLM 모델을 하나의 통합 API 엔드포인트로 라우팅하는 MIT 라이선스 오픈소스 게이트웨이. | `Tool/CLI` | [github.com/cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) |
| **freellmapi** | 무료 티어를 제공하는 34개 제공사와 600여 개 모델 엔드포인트를 개인 실험용으로 정리한 저장소. | `Resource/Guide` | [github.com/tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) |
| **Cactus Compute (Needle & Mirage)** | 스마트폰·웨어러블·브라우저에서 도는 14MB 도구호출 모델(Needle)과 22MB 비전·OCR 모델(Mirage) 초경량 에지 AI 스위트. | `Model` | [github.com/cactus-compute/cactus](https://github.com/cactus-compute/cactus) |

## 문서 파싱 & OCR

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **MarkItDown (Microsoft)** | PDF, Word, Excel, PowerPoint 등 다양한 문서를 LLM이 읽기 좋은 마크다운으로 초고속 변환하는 마이크로소프트 도구. ([심층 가이드](https://godstale.mycafe24.com/?p=867)) | `Tool/CLI` | [github.com/microsoft/markitdown](https://github.com/microsoft/markitdown) |
| **Docling (IBM)** | 표 구조와 스캔 문서 인식 정확도가 뛰어난 IBM 오픈소스 문서 파싱 라이브러리. | `Library` | [github.com/docling-project/docling](https://github.com/docling-project/docling) |
| **PaddleOCR (PaddleOCR-VL)** | 스캔본, 표, 순서도, 사진 속 숫자 인식에 강점을 가진 오픈소스 다국어 OCR 엔진. ([심층 가이드](https://godstale.mycafe24.com/?p=855)) | `Library` | [github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |
| **MinerU 2.5** | 복잡한 학술 논문과 PDF 문서를 수식·표 포함 마크다운으로 깔끔하게 추출하는 오픈소스 문서 OCR 도구. ([심층 가이드](https://godstale.mycafe24.com/?p=855)) | `Tool/CLI` | [github.com/opendatalab/MinerU](https://github.com/opendatalab/MinerU) |

## 에이전트 샌드박스 & OS 유틸리티

| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |
|---|---|---|---|
| **NVIDIA OpenShell** | AI 에이전트의 파일·프로세스·네트워크 접근과 자격 증명을 정책 기반으로 격리하는 NVIDIA 오픈소스 샌드박스. | `Tool/CLI` | [github.com/NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) |
| **CubeSandbox** | AI 에이전트가 실행하는 코드를 안전하게 격리하는 텐센트 클라우드 기반 초경량 샌드박스. | `Tool/CLI` | [github.com/TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) |
| **Flue** | 에이전트 실행 환경을 가볍게 격리해 안전한 자동화 작업을 지원하는 오픈소스 샌드박스. | `Tool/CLI` | [github.com/withastro/flue](https://github.com/withastro/flue) |
| **Omarchy v4.0** | Basecamp(Omacom 재단)가 개발자 환경에 맞춰 구성한 Arch 기반 리눅스 배포판. | `App` | [github.com/omacom/omarchy](https://github.com/omacom/omarchy) |
| **Hyprland** | 부드러운 애니메이션과 자동 타일링 레이아웃을 제공하는 Wayland 기반 리눅스 창 관리자. | `App` | [github.com/hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) |
| **OpenLogi** | 무거운 Logitech Options+를 대체하기 위해 Rust로 작성된 가벼운 오픈소스 마우스·키보드 설정 도구. | `App` | [github.com/AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) |
| **DiscImageStudio** | 이미지를 CD·DVD·BD-R 광학 디스크 기록면에 직접 새길 수 있는 디스크 이미지로 변환하는 오픈소스 도구. | `App` | [github.com/JiaFeiMiao-K-Cat/DiscImageSt...](https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio) |

---

### 다른 카테고리 둘러보기

[💻 IT · 코딩 & 개발 워크플로우](../01-coding-and-dev/README.md) · [⚡ 생산성 · 협업 & 비즈니스](../02-productivity-and-business/README.md) · [🎨 미디어 · 디자인 & 크리에이티브](../03-media-and-creative/README.md) · [🎮 게임 개발 & 에셋 제작](../04-game-dev/README.md) · [📚 교육 · 학습 & 연구](../05-education-and-research/README.md) · **🖥️ 로컬 AI · 모델 서빙 & 인프라** · [🛡️ 보안 · 역공학 & OSINT](../07-security-and-osint/README.md)
