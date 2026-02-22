# -*- coding: utf-8 -*-
"""
Xiaohongshu (RED) note fetcher — uses Jina Reader for content extraction.

Jina handles anti-scraping and JS rendering transparently.
No login or session needed for public notes.
"""

from loguru import logger
from typing import Dict, Any

from x_reader.fetchers.jina import fetch_via_jina


async def fetch_xhs(url: str) -> Dict[str, Any]:
    """
    Fetch a Xiaohongshu note via Jina Reader.

    Args:
        url: xiaohongshu.com or xhslink.com URL

    Returns:
        Dict with: title, content, author, url
    """
    logger.info(f"Fetching Xiaohongshu: {url}")

    data = fetch_via_jina(url)

    return {
        "title": data["title"],
        "content": data["content"],
        "author": data.get("author", ""),
        "url": url,
        "platform": "xhs",
    }
