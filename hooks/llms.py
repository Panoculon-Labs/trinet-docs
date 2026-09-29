"""MkDocs hook: write llms.txt (page index) and llms-full.txt (all page text) into the site.

These give AI assistants — including the planned "Ask the docs" assistant — a clean, complete,
machine-readable copy of the documentation. Pages appear in navigation order.
"""
from __future__ import annotations

import re
from pathlib import Path

_pages: dict[str, dict] = {}

_SNIPPET_LINE = re.compile(r"^\*\[[^\]]+\]:.*$", re.MULTILINE)      # abbreviation definitions
_HTML_TAG = re.compile(r"<[^>]+>")
_ATTR_LIST = re.compile(r"\{\s*[.#:][^}]*\}")
_ICON = re.compile(r":(?:material|fontawesome|octicons|simple)-[\w-]+:(?:\{[^}]*\})?")


def on_config(config):
    _pages.clear()
    return config


def on_page_markdown(markdown, page, config, files):
    _pages[page.file.src_uri] = {
        "title": page.title,
        "url": config["site_url"].rstrip("/") + "/" + page.url,
        "description": page.meta.get("description", ""),
        "text": _clean(markdown),
    }
    return markdown


def _clean(md: str) -> str:
    md = _SNIPPET_LINE.sub("", md)
    md = _ICON.sub("", md)
    md = _ATTR_LIST.sub("", md)
    md = _HTML_TAG.sub("", md)
    return re.sub(r"\n{3,}", "\n\n", md).strip()


def _nav_order(nav) -> list[str]:
    order = []
    for item in nav:
        if getattr(item, "is_page", False):
            order.append(item.file.src_uri)
        for child in getattr(item, "children", None) or []:
            order.extend(_nav_order([child]))
    return order


def on_post_build(config):
    nav_order = [p for p in _NAV if p in _pages] + [p for p in _pages if p not in _NAV]
    site = config["site_name"]
    index = [f"# {site}", "", f"> {config.get('site_description', '').strip()}", ""]
    full = [f"# {site}", ""]
    for uri in nav_order:
        p = _pages[uri]
        desc = f": {p['description']}" if p["description"] else ""
        index.append(f"- [{p['title']}]({p['url']}){desc}")
        full.extend([f"\n\n---\n\n# {p['title']}", f"Source: {p['url']}", "", p["text"]])
    out = Path(config["site_dir"])
    (out / "llms.txt").write_text("\n".join(index) + "\n", encoding="utf-8")
    (out / "llms-full.txt").write_text("\n".join(full) + "\n", encoding="utf-8")


_NAV: list[str] = []


def on_nav(nav, config, files):
    _NAV[:] = _nav_order(nav.items)
    return nav
