#!/usr/bin/env python3
"""Generate root README.md, category README.md files, and sync docs/tools.json from data/tools.json."""

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


def validate_data(data: dict) -> None:
    cat_ids = {c["id"] for c in data["categories"]}
    seen = set()
    for idx, t in enumerate(data["tools"]):
        for field in ("name", "description", "url", "category"):
            if not t.get(field) or not str(t[field]).strip():
                raise ValueError(f"Tool #{idx} missing required field '{field}': {t}")
        if t["category"] not in cat_ids:
            raise ValueError(f"Tool '{t['name']}' has unknown category '{t['category']}'")
        key = (t["name"].lower(), t["url"].lower())
        if key in seen:
            raise ValueError(f"Duplicate tool entry: {t['name']} ({t['url']})")
        seen.add(key)


def build_category_readme(cat: dict, all_cats: list[dict], tools: list[dict], meta: dict) -> str:
    lines: list[str] = []
    lines.append(f"# {cat['icon']} {cat['name']} ({cat['en_name']})")
    lines.append("")
    lines.append(f"> {cat['summary']}")
    lines.append("")
    lines.append(
        f"[🏠 메인으로 돌아가기](../README.md) · "
        f"[🔍 웹에서 실시간 검색하기]({meta['pages_url']}?cat={cat['id']}) · "
        f"[📂 GitHub 내 검색]({meta['repo_url']}/search?q=path%3A{cat['id']})"
    )
    lines.append("")

    # Subcategory grouping preserving insertion order
    grouped: dict[str, list[dict]] = defaultdict(list)
    for t in tools:
        grouped[t.get("subcategory", "기타")].append(t)

    lines.append(f"총 **{len(tools)}개** 항목 수록 · 최종 업데이트: `{meta['updated_at']}`")
    lines.append("")

    # Table of contents
    lines.append("## 세부 분류 목차")
    lines.append("")
    for sub, items in grouped.items():
        anchor = (
            sub.lower()
            .replace("·", "")
            .replace("&", "")
            .replace("/", "")
            .replace("(", "")
            .replace(")", "")
            .strip()
        )
        anchor = "-".join(anchor.split())
        lines.append(f"- [{sub}](#{anchor}) ({len(items)})")
    lines.append("")

    # Tables per subcategory
    for sub, items in grouped.items():
        lines.append(f"## {sub}")
        lines.append("")
        lines.append("| 이름 (Name) | 설명 (Description) | 유형 | 바로가기 (URL) |")
        lines.append("|---|---|---|---|")
        for t in items:
            name = escape_md(t["name"])
            desc = escape_md(t["description"])
            if t.get("wp_url"):
                desc += f" ([심층 가이드]({t['wp_url']}))"
            ttype = f"`{escape_md(t.get('type', 'Tool'))}`"
            url = t["url"]
            short_link = url.replace("https://", "").replace("http://", "").rstrip("/")
            if len(short_link) > 42:
                short_link = short_link[:39] + "..."
            lines.append(f"| **{name}** | {desc} | {ttype} | [{short_link}]({url}) |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("### 다른 카테고리 둘러보기")
    lines.append("")
    nav = []
    for c in all_cats:
        if c["id"] == cat["id"]:
            nav.append(f"**{c['icon']} {c['name']}**")
        else:
            nav.append(f"[{c['icon']} {c['name']}](../{c['id']}/README.md)")
    lines.append(" · ".join(nav))
    lines.append("")
    return "\n".join(lines)


def build_root_readme(data: dict) -> str:
    meta = data["meta"]
    cats = data["categories"]
    tools = data["tools"]

    counts = defaultdict(int)
    for t in tools:
        counts[t["category"]] += 1

    lines: list[str] = []
    lines.append(f"# 🧰 {meta['title']}")
    lines.append("")
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

    # Search section (GitHub Pages interactive search + GitHub native search links)
    lines.append("## 🔍 도구 검색하기 (Search)")
    lines.append("")
    lines.append(
        f"> **⚡ 실시간 검색창 (웹 앱):** [**Agent Toolbox 검색 페이지 열기 (GitHub Pages)**]({meta['pages_url']})  \n"
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
    lines.append("## 🔥 최신 AI 에이전트 트렌드 요약")
    lines.append("")
    for tr in data.get("trends", []):
        link_str = f" — [관련 심층 포스트]({tr['related_url']})" if tr.get("related_url") else ""
        lines.append(f"- **{tr['title']}**: {tr['summary']}{link_str}")
    lines.append("")

    # Category directory table
    lines.append("## 📂 분야별 카테고리 (Categories)")
    lines.append("")
    lines.append("| 분야 (Category) | 수록 수 | 주요 다루는 내용 | 폴더 바로가기 |")
    lines.append("|---|---:|---|---|")
    for c in cats:
        cnt = counts[c["id"]]
        lines.append(
            f"| {c['icon']} **{c['name']}** | {cnt}개 | {c['summary']} | [`{c['id']}/`]({c['id']}/README.md) |"
        )
    lines.append("")

    # Quick browse by category (collapsible full preview right on README!)
    lines.append("## 📋 전체 목록 한눈에 보기 (Quick Browse)")
    lines.append("")
    lines.append("각 분야를 클릭해 펼쳐 보거나, 분야별 폴더의 `README.md`에서 세부 분류별로 열람할 수 있습니다.")
    lines.append("")

    by_cat: dict[str, list[dict]] = defaultdict(list)
    for t in tools:
        by_cat[t["category"]].append(t)

    for c in cats:
        items = by_cat[c["id"]]
        lines.append("<details>")
        lines.append(f"<summary><strong>{c['icon']} {c['name']} ({len(items)}개)</strong> — 클릭해서 펼치기</summary>")
        lines.append("")
        lines.append(f"👉 [전체 상세 페이지 보기 (`{c['id']}/README.md`)]({c['id']}/README.md)")
        lines.append("")
        lines.append("| 이름 (Name) | 설명 (Description) | URL |")
        lines.append("|---|---|---|")
        for t in items:
            name = escape_md(t["name"])
            desc = escape_md(t["description"])
            url = t["url"]
            lines.append(f"| **{name}** | {desc} | [링크]({url}) |")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    # WordPress blog integration & Data schema
    lines.append("## 📝 관련 블로그 & 데이터 구조")
    lines.append("")
    lines.append(
        f"- **블로그 허브 포스트:** [AI 스킬·도구·앱 총정리 허브 (hellollama)]({meta['hub_post_url']}) — "
        "도구별 심층 분석, 비교표, 실전 세팅 가이드는 워드프레스 블로그와 함께 동기화되어 관리됩니다."
    )
    lines.append("- **단일 데이터 소스:** [`data/tools.json`](data/tools.json) (`name`, `description`, `url` 필수 구조)")
    lines.append("- **문서 자동 생성:** `python scripts/build_docs.py` 실행 시 루트 `README.md`, 카테고리별 `README.md`, 웹 검색 데이터(`docs/tools.json`)가 일괄 갱신됩니다.")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    validate_data(data)

    # Sync docs/tools.json for GitHub Pages
    DOCS_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(DATA_FILE, DOCS_DATA_FILE)

    # Generate category folders & READMEs
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for t in data["tools"]:
        by_cat[t["category"]].append(t)

    for cat in data["categories"]:
        cat_dir = ROOT / cat["id"]
        cat_dir.mkdir(parents=True, exist_ok=True)
        cat_md = build_category_readme(cat, data["categories"], by_cat[cat["id"]], data["meta"])
        (cat_dir / "README.md").write_text(cat_md, encoding="utf-8")

    # Generate root README.md
    root_md = build_root_readme(data)
    (ROOT / "README.md").write_text(root_md, encoding="utf-8")

    print(
        f"Generated root README.md, {len(data['categories'])} category READMEs, "
        f"and docs/tools.json ({len(data['tools'])} tools total)."
    )


if __name__ == "__main__":
    main()
