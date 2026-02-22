# -*- coding: utf-8 -*-
"""
X/Twitter fetcher — uses Jina Reader for content extraction.

No API key needed. Works by converting tweet URLs to readable markdown.
"""

import re
from loguru import logger
from typing import Dict, Any

from x_reader.fetchers.jina import fetch_via_jina


async def fetch_twitter(url: str) -> Dict[str, Any]:
    """
    Fetch a tweet or X post via Jina Reader.

    Args:
        url: Tweet URL (x.com or twitter.com)

    Returns:
        Dict with: text, author, url, likes, retweets
    """
    logger.info(f"Fetching Twitter: {url}")

    # Normalize URL
    url = url.replace("twitter.com", "x.com")

    data = fetch_via_jina(url)

    # Try to extract author from URL pattern /username/status/
    author = ""
    match = re.search(r'x\.com/(\w+)/status', url)
    if match:
        author = f"@{match.group(1)}"

    return {
        "text": data["content"],
        "author": author,
        "url": url,
        "title": data["title"],
        "platform": "twitter",
    }
