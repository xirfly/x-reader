# -*- coding: utf-8 -*-
"""
YouTube video fetcher — uses Jina Reader for page content extraction.

Extracts video title, description, and metadata from YouTube pages.
No API key needed.
"""

import re
from loguru import logger
from typing import Dict, Any

from x_reader.fetchers.jina import fetch_via_jina


async def fetch_youtube(url: str) -> Dict[str, Any]:
    """
    Fetch YouTube video metadata via Jina Reader.

    Args:
        url: YouTube video URL (youtube.com/watch or youtu.be)

    Returns:
        Dict with: title, description, author, url
    """
    logger.info(f"Fetching YouTube: {url}")

    data = fetch_via_jina(url)

    # Try to extract video ID
    video_id = ""
    match = re.search(r'(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})', url)
    if match:
        video_id = match.group(1)

    return {
        "title": data["title"],
        "description": data["content"],
        "author": data.get("author", ""),
        "url": url,
        "video_id": video_id,
        "platform": "youtube",
    }
