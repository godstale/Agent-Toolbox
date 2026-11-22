#!/usr/bin/env python3
"""Generate bilingual (English default README.md + Korean README.ko.md) docs and sync docs/tools.json."""

from __future__ import annotations

import json
import shutil
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "tools.json"
DOCS_DATA_FILE = ROOT / "docs" / "tools.json"


def escape_md(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def make_anchor(text: str) -> str:
    anchor = (
        text.lower()
        .replace("·", "")
        .replace("&", "")
        .replace("/", "")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
        .strip()
    )
    return "-".join(anchor.split())


def validate_data(data: dict) -> None:
    cat_ids = {c["id"] for c in data["categories"]}
    seen = set()
    for idx, t in enumerate(data["tools"]):
        for field in ("name", "description", "description_en", "url", "category"):
            if not t.get(field) or not str(t[field]).strip():
                raise ValueError(f"Tool #{idx} missing required field '{field}': {t}")
        if t["category"] not in cat_ids:
            raise ValueError(f"Tool '{t['name']}' has unknown category '{t['category']}'")
        key = (t["name"].lower(), t["url"].lower())
        if key in seen:
            raise ValueError(f"Duplicate tool entry: {t['name']} ({t['url']})")
        seen.add(key)


def lang_switcher(lang: str) -> str:
    if lang == "en":
        return "🌐 **English** | [한국어 (Korean)](README.ko.md)"
    return "🌐 [English](README.md) | **한국어 (Korean)**"


def build_category_readme(
    cat: dict, all_cats: list[dict], tools: list[dict], meta: dict, lang: str
) -> str:
    is_en = lang == "en"
    readme_file = "README.md" if is_en else "README.ko.md"
    title = cat["en_name"] if is_en else f"{cat['name']} ({cat['en_name']})"
    summary = cat["summary_en"] if is_en else cat["summary"]

    lines: list[str] = []
    lines.append(lang_switcher(lang))
    lines.append("")
    lines.append(f"# {cat['icon']} {title}")
    lines.append("")
    lines.append(f"> {summary}")
    lines.append("")

    if is_en:
        lines.append(
            f"[🏠 Back to Home](../{readme_file}) · "
            f"[🔍 Interactive Web Search]({meta['pages_url']}?lang=en&cat={cat['id']}) · "
            f"[📂 Search in GitHub]({meta['repo_url']}/search?q=path%3A{cat['id']})"
        )
        lines.append("")
        lines.append(f"**{len(tools)} tools** listed · Last updated: `{meta['updated_at']}`")
        lines.append("")
        lines.append("## Subcategories")
    else:
        lines.append(
            f"[🏠 메인으로 돌아가기](../{readme_file}) · "
            f"[🔍 웹에서 실시간 검색하기]({meta['pages_url']}?lang=ko&cat={cat['id']}) · "
            f"[📂 GitHub 내 검색]({meta['repo_url']}/search?q=path%3A{cat['id']})"
        )
        lines.append("")
        lines.append(f"총 **{len(tools)}개** 항목 수록 · 최종 업데이트: `{meta['updated_at']}`")
        lines.append("")
        lines.append("## 세부 분류 목차")

    grouped: dict[str, list[dict]] = defaultdict(list)
    for t in tools:
        sub = t.get("subcategory_en", "Other") if is_en else t.get("subcategory", "기타")
        grouped[sub].append(t)

    lines.append("")
    for sub, items in grouped.items():
        lines.append(f"- [{sub}](#{make_anchor(sub)}) ({len(items)})")
    lines.append("")

    for sub, items in grouped.items():
        lines.append(f"## {sub}")
        lines.append("")
        if is_en:
            lines.append("| Name | Description | Type | URL |")
        else:
            lines.append("| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |")
        lines.append("|---|---|---|---|")
        for t in items:
            raw_name = t.get("name_en", t["name"]) if is_en else t["name"]
            raw_desc = t["description_en"] if is_en else t["description"]
            name = escape_md(raw_name)
            desc = escape_md(raw_desc)
            if t.get("wp_url"):
                guide_label = "Deep Dive (KR)" if is_en else "심층 가이드"
                desc += f" ([{guide_label}]({t['wp_url']}))"
            ttype = f"`{escape_md(t.get('type', 'Tool'))}`"
            url = t["url"]
            short_link = url.replace("https://", "").replace("http://", "").rstrip("/")
            if len(short_link) > 42:
                short_link = short_link[:39] + "..."
            lines.append(f"| **{name}** | {desc} | {ttype} | [{short_link}]({url}) |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("### Browse Other Categories" if is_en else "### 다른 카테고리 둘러보기")
    lines.append("")
    nav = []
    for c in all_cats:
        c_label = c["en_name"] if is_en else c["name"]
        if c["id"] == cat["id"]:
            nav.append(f"**{c['icon']} {c_label}**")
        else:
            nav.append(f"[{c['icon']} {c_label}](../{c['id']}/{readme_file})")
    lines.append(" · ".join(nav))
    lines.append("")
    return "\n".join(lines)


def build_root_readme(data: dict, lang: str) -> str:
    is_en = lang == "en"
    meta = data["meta"]
    cats = data["categories"]
    tools = data["tools"]
    readme_file = "README.md" if is_en else "README.ko.md"

    counts = defaultdict(int)
    for t in tools:
        counts[t["category"]] += 1

    lines: list[str] = []
    lines.append(lang_switcher(lang))
    lines.append("")
    lines.append(f"# 🧰 {meta['title']}")
    lines.append("")

    if is_en:
        lines.append(f"**{meta['subtitle_en']}**")
        lines.append("")
        lines.append(
            "A curated, domain-organized directory of the latest open-source repositories, agent skills, "
            "MCP servers, desktop apps, libraries, and learning resources for AI coding agents "
            "(Claude Code, Codex, Gemini, etc.).  "
        )
        lines.append(
            "Every entry follows a clean **`[Name, Description, URL]`** schema with plain, concise explanations."
        )
    else:
        lines.append(f"**{meta['subtitle']}**")
        lines.append("")
        lines.append(
            "AI 에이전트(Claude Code, Codex, Gemini 등)와 함께 활용할 수 있는 최신 GitHub 오픈소스, "
            "스킬(Skills), MCP 서버, 앱, 라이브러리, 학습 자료를 **사용 분야별**로 정리한 저장소입니다.  "
        )
        lines.append(
            "모든 항목은 **`[Name, Description, URL]`** 표준 구조로 관리되며, 누구나 한눈에 파악할 수 있도록 "
            "쉽고 담백한 설명을 제공합니다."
        )

    lines.append("")
    lines.append(
        f"![Total Tools](https://img.shields.io/badge/Tools-{len(tools)}-blue?style=flat-square) "
        f"![Categories](https://img.shields.io/badge/Categories-{len(cats)}-green?style=flat-square) "
        f"![Updated](https://img.shields.io/badge/Updated-{meta['updated_at'].replace('-', '--')}-orange?style=flat-square)"
    )
    lines.append("")

    # Search section
    if is_en:
        lines.append("## 🔍 Search Tools")
        lines.append("")
        lines.append(
            f"> **⚡ Interactive Search Web App (Auto-detects EN/KO):** [**Open Agent Toolbox Search (GitHub Pages)**]({meta['pages_url']}?lang=en)  \n"
            "> Filter instantly by keyword, domain category, and tool type."
        )
        lines.append("")
        lines.append(
            "To search directly inside GitHub, press **`/`** on your keyboard or click a quick-search tag below:"
        )
    else:
        lines.append("## 🔍 도구 검색하기 (Search)")
        lines.append("")
        lines.append(
            f"> **⚡ 실시간 검색창 (언어 자동 감지 EN/KO):** [**Agent Toolbox 검색 페이지 열기 (GitHub Pages)**]({meta['pages_url']}?lang=ko)  \n"
            "> 키워드 입력창, 카테고리 필터, 유형별 필터로 원하는 도구를 즉시 찾을 수 있습니다."
        )
        lines.append("")
        lines.append(
            "GitHub 화면에서 바로 검색하려면 키보드에서 **`/`** 키를 누르거나 아래 인기 키워드 버튼을 클릭하세요:"
        )

    lines.append("")
    quick_keywords = [
        "Claude Code",
        "MCP",
        "Skill",
        "Worktree",
        "Sprite",
        "Motion",
        "Local LLM",
        "OCR",
        "Security",
        "Design",
        "Godot",
        "Memory",
    ]
    search_links = [
        f"[`🔎 {kw}`]({meta['repo_url']}/search?q={quote_plus(kw)})" for kw in quick_keywords
    ]
    lines.append(" ".join(search_links))
    lines.append("")

    # Latest Trends
    lines.append("## 🔥 Latest AI Agent Trends" if is_en else "## 🔥 최신 AI 에이전트 트렌드 요약")
    lines.append("")
    for tr in data.get("trends", []):
        t_title = tr["title_en"] if is_en else tr["title"]
        t_summary = tr["summary_en"] if is_en else tr["summary"]
        link_label = "Deep Dive (KR)" if is_en else "관련 심층 포스트"
        link_str = f" — [{link_label}]({tr['related_url']})" if tr.get("related_url") else ""
        lines.append(f"- **{t_title}**: {t_summary}{link_str}")
    lines.append("")

    # Category directory table
    if is_en:
        lines.append("## 📂 Categories")
        lines.append("")
        lines.append("| Category | Count | What's Inside | Folder |")
        lines.append("|---|---:|---|---|")
    else:
        lines.append("## 📂 분야별 카테고리 (Categories)")
        lines.append("")
        lines.append("| 분야 (Category) | 수록 수 | 주요 다루는 내용 | 폴더 바로가기 |")
        lines.append("|---|---:|---|---|")

    for c in cats:
        cnt = counts[c["id"]]
        c_name = c["en_name"] if is_en else c["name"]
        c_summary = c["summary_en"] if is_en else c["summary"]
        cnt_str = f"{cnt}" if is_en else f"{cnt}개"
        lines.append(
            f"| {c['icon']} **{c_name}** | {cnt_str} | {c_summary} | [`{c['id']}/`]({c['id']}/{readme_file}) |"
        )
    lines.append("")

    # Quick browse
    if is_en:
        lines.append("## 📋 Quick Browse")
        lines.append("")
        lines.append("Expand any category below, or open its folder `README.md` for subcategory tables.")
    else:
        lines.append("## 📋 전체 목록 한눈에 보기 (Quick Browse)")
        lines.append("")
        lines.append("각 분야를 클릭해 펼쳐 보거나, 분야별 폴더의 `README.ko.md`에서 세부 분류별로 열람할 수 있습니다.")
    lines.append("")

    by_cat: dict[str, list[dict]] = defaultdict(list)
    for t in tools:
        by_cat[t["category"]].append(t)

    for c in cats:
        items = by_cat[c["id"]]
        c_name = c["en_name"] if is_en else c["name"]
        lines.append("<details>")
        if is_en:
            lines.append(
                f"<summary><strong>{c['icon']} {c_name} ({len(items)})</strong> — click to expand</summary>"
            )
            lines.append("")
            lines.append(f"👉 [Open full category page (`{c['id']}/{readme_file}`)]({c['id']}/{readme_file})")
            lines.append("")
            lines.append("| Name | Description | URL |")
        else:
            lines.append(
                f"<summary><strong>{c['icon']} {c_name} ({len(items)}개)</strong> — 클릭해서 펼치기</summary>"
            )
            lines.append("")
            lines.append(f"👉 [전체 상세 페이지 보기 (`{c['id']}/{readme_file}`)]({c['id']}/{readme_file})")
            lines.append("")
            lines.append("| 이름 (Name) | 설명 (Description) | URL |")
        lines.append("|---|---|---|")
        for t in items:
            raw_name = t.get("name_en", t["name"]) if is_en else t["name"]
            raw_desc = t["description_en"] if is_en else t["description"]
            link_txt = "Link" if is_en else "링크"
            lines.append(f"| **{escape_md(raw_name)}** | {escape_md(raw_desc)} | [{link_txt}]({t['url']}) |")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    # Footer / Blog & Data schema
    if is_en:
        lines.append("## 📝 Related Blog & Data Schema")
        lines.append("")
        lines.append(
            f"- **Companion Blog Hub (Korean):** [AI Skills, Tools & Apps Hub (hellollama)]({meta['hub_post_url']}) — "
            "In-depth guides, benchmarks, and setup walkthroughs synchronized with this repository."
        )
        lines.append("- **Single Source of Truth:** [`data/tools.json`](data/tools.json) (`name`, `description`, `description_en`, `url`)")
        lines.append("- **Auto-generation:** Run `python scripts/build_docs.py` to regenerate all English (`README.md`) and Korean (`README.ko.md`) pages plus `docs/tools.json`.")
    else:
        lines.append("## 📝 관련 블로그 & 데이터 구조")
        lines.append("")
        lines.append(
            f"- **블로그 허브 포스트:** [AI 스킬·도구·앱 총정리 허브 (hellollama)]({meta['hub_post_url']}) — "
            "도구별 심층 분석, 비교표, 실전 세팅 가이드는 워드프레스 블로그와 함께 동기화되어 관리됩니다."
        )
        lines.append("- **단일 데이터 소스:** [`data/tools.json`](data/tools.json) (`name`, `description`, `url` 필수 구조)")
        lines.append("- **문서 자동 생성:** `python scripts/build_docs.py` 실행 시 영문(`README.md`)·한글(`README.ko.md`) 문서와 웹 검색 데이터(`docs/tools.json`)가 일괄 갱신됩니다.")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    validate_data(data)

    DOCS_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(DATA_FILE, DOCS_DATA_FILE)

    by_cat: dict[str, list[dict]] = defaultdict(list)
    for t in data["tools"]:
        by_cat[t["category"]].append(t)

    for cat in data["categories"]:
        cat_dir = ROOT / cat["id"]
        cat_dir.mkdir(parents=True, exist_ok=True)
        for lang, fname in (("en", "README.md"), ("ko", "README.ko.md")):
            cat_md = build_category_readme(cat, data["categories"], by_cat[cat["id"]], data["meta"], lang)
            (cat_dir / fname).write_text(cat_md, encoding="utf-8")

    for lang, fname in (("en", "README.md"), ("ko", "README.ko.md")):
        (ROOT / fname).write_text(build_root_readme(data, lang), encoding="utf-8")

    print(
        f"Generated EN (README.md) & KO (README.ko.md) for root + {len(data['categories'])} categories "
        f"and synced docs/tools.json ({len(data['tools'])} tools total)."
    )


if __name__ == "__main__":
    main()
