🌐 **English** | [한국어 (Korean)](README.ko.md)

# 🖥️ Local AI, Serving & Infrastructure

> Local LLM inference & fine-tuning engines, LLM gateways, ultra-light edge models, document parsing/OCR, and agent sandboxes

[🏠 Back to Home](../README.md) · [🔍 Interactive Web Search](https://godstale.github.io/Agent-Toolbox/?lang=en&cat=06-local-ai-and-infra) · [📂 Search in GitHub](https://github.com/godstale/Agent-Toolbox/search?q=path%3A06-local-ai-and-infra)

**22 tools** listed · Last updated: `2026-11-22`

## Subcategories

- [Local LLM Inference & Fine-Tuning Engines](#local-llm-inference-fine-tuning-engines) (8)
- [LLM Gateways & Ultra-Light Edge Models](#llm-gateways-ultra-light-edge-models) (3)
- [Document Parsing & OCR](#document-parsing-ocr) (4)
- [Agent Sandboxes & OS Utilities](#agent-sandboxes-os-utilities) (7)

## Local LLM Inference & Fine-Tuning Engines

| Name | Description | Type | URL |
|---|---|---|---|
| **llama.cpp** | Standard C/C++ inference engine for fast, quantized local LLM execution using the GGUF format. ([Deep Dive (KR)](https://godstale.mycafe24.com/?p=1100)) | `Framework/Harness` | [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) |
| **vLLM** | High-throughput production LLM serving engine powered by PagedAttention. ([Deep Dive (KR)](https://godstale.mycafe24.com/?p=1100)) | `Framework/Harness` | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) |
| **Strata** | Local inference engine optimized for running ultra-large Mixture-of-Experts (MoE) models on consumer hardware. ([Deep Dive (KR)](https://godstale.mycafe24.com/?p=1100)) | `Framework/Harness` | [github.com/Niko1221/Strata](https://github.com/Niko1221/Strata) |
| **Colibri** | Local LLM engine that streams active experts from SSD storage to run hundreds-of-billions-parameter models with limited RAM. ([Deep Dive (KR)](https://godstale.mycafe24.com/?p=1155)) | `Framework/Harness` | [github.com/JustVugg/colibri](https://github.com/JustVugg/colibri) |
| **AirLLM** | Python library loading one model layer at a time to run large LLMs on low-VRAM GPUs. | `Library` | [github.com/lyogavin/airllm](https://github.com/lyogavin/airllm) |
| **FreeToken** | Fast local inference engine keeping hot weights on GPU so 8GB NVIDIA Linux laptops can run large local coding models. ([Deep Dive (KR)](https://godstale.mycafe24.com/?p=1155)) | `Framework/Harness` | [github.com/FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken) |
| **Unsloth** | Open-source fine-tuning library accelerating local LLM training while cutting GPU memory usage. ([Deep Dive (KR)](https://godstale.mycafe24.com/?p=848)) | `Library` | [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth) |
| **Open WebUI** | Self-hosted ChatGPT-style web interface for local and API models with real-time voice conversation support. | `App` | [github.com/open-webui/open-webui](https://github.com/open-webui/open-webui) |

## LLM Gateways & Ultra-Light Edge Models

| Name | Description | Type | URL |
|---|---|---|---|
| **OmniRoute** | MIT-licensed open-source LLM gateway routing hundreds of models behind a single unified API endpoint. | `Tool/CLI` | [github.com/cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) |
| **freellmapi** | Community directory cataloging 34 free-tier LLM providers and 600+ endpoints for personal experimentation. | `Resource/Guide` | [github.com/tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) |
| **Cactus Compute (Needle & Mirage)** | Ultra-light edge AI suite featuring a 14MB tool-calling model (Needle) and a 22MB single-pass vision/OCR model (Mirage). | `Model` | [github.com/cactus-compute/cactus](https://github.com/cactus-compute/cactus) |

## Document Parsing & OCR

| Name | Description | Type | URL |
|---|---|---|---|
| **MarkItDown (Microsoft)** | Fast Microsoft utility converting PDF, Word, Excel, and PowerPoint files into clean LLM-friendly Markdown. ([Deep Dive (KR)](https://godstale.mycafe24.com/?p=867)) | `Tool/CLI` | [github.com/microsoft/markitdown](https://github.com/microsoft/markitdown) |
| **Docling (IBM)** | IBM's open-source document parsing library with strong accuracy on complex tables and scanned PDFs. | `Library` | [github.com/docling-project/docling](https://github.com/docling-project/docling) |
| **PaddleOCR (PaddleOCR-VL)** | Open-source multilingual OCR engine excelling at scans, tables, flowcharts, and photographed numbers. ([Deep Dive (KR)](https://godstale.mycafe24.com/?p=855)) | `Library` | [github.com/PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |
| **MinerU 2.5** | Open-source PDF and academic paper OCR tool extracting formulas and tables cleanly into Markdown. ([Deep Dive (KR)](https://godstale.mycafe24.com/?p=855)) | `Tool/CLI` | [github.com/opendatalab/MinerU](https://github.com/opendatalab/MinerU) |

## Agent Sandboxes & OS Utilities

| Name | Description | Type | URL |
|---|---|---|---|
| **NVIDIA OpenShell** | Open-source policy-based sandbox from NVIDIA isolating agent file, process, network, and credential access. | `Tool/CLI` | [github.com/NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) |
| **CubeSandbox** | Ultra-lightweight sandbox from Tencent Cloud for safely isolating AI agent code execution. | `Tool/CLI` | [github.com/TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox) |
| **Flue** | Lightweight open-source sandbox environment for safe automated agent execution. | `Tool/CLI` | [github.com/withastro/flue](https://github.com/withastro/flue) |
| **Omarchy v4.0** | Developer-focused Arch Linux distribution maintained by Basecamp's Omacom foundation. | `App` | [github.com/omacom/omarchy](https://github.com/omacom/omarchy) |
| **Hyprland** | Dynamic tiling Wayland compositor for Linux with smooth animations and flexible layouts. | `App` | [github.com/hyprwm/Hyprland](https://github.com/hyprwm/Hyprland) |
| **OpenLogi** | Lightweight open-source Rust alternative to Logitech Options+ for mouse and keyboard configuration. | `App` | [github.com/AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi) |
| **DiscImageStudio** | Open-source C# tool that converts artwork into optical disc data for etching visible images onto CD/DVD/BD-R surfaces. | `App` | [github.com/JiaFeiMiao-K-Cat/DiscImageSt...](https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio) |

---

### Browse Other Categories

[💻 Coding & Dev Workflows](../01-coding-and-dev/README.md) · [⚡ Productivity, Collaboration & Business](../02-productivity-and-business/README.md) · [🎨 Media, Design & Creative](../03-media-and-creative/README.md) · [🎮 Game Dev & Assets](../04-game-dev/README.md) · [📚 Education, Learning & Research](../05-education-and-research/README.md) · **🖥️ Local AI, Serving & Infrastructure** · [🛡️ Security, Reverse Engineering & OSINT](../07-security-and-osint/README.md)
