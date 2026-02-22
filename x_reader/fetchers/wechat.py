# -*- coding: utf-8 -*-
"""
WeChat article fetcher — uses Jina Reader for content extraction.

Works with mp.weixin.qq.com article URLs.
No login or session needed.
"""

from loguru import logger
from typing import Dict, Any

from x_reader.fetchers.jina import fetch_via_jina


async def fetch_wechat(url: str) -> Dict[str, Any]:
    """
    Fetch a WeChat public account article via Jina Reader.

    Args:
        url: mp.weixin.qq.com article URL

    Returns:
        Dict with: title, content, author, url
    """
    logger.info(f"Fetching WeChat: {url}")

    data = fetch_via_jina(url)

    return {
        "title": data["title"],
        "content": data["content"],
        "author": data.get("author", ""),
        "url": url,
        "platform": "wechat",
    }
