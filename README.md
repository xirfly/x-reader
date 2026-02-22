# x-reader

Universal content reader — fetch, normalize, and digest content from 7+ platforms.

## Supported Platforms

| Platform | Method |
|----------|--------|
| WeChat (微信公众号) | Jina Reader |
| Telegram | Telethon API |
| X / Twitter | Jina Reader |
| YouTube | Jina Reader |
| Bilibili (B站) | Official API |
| Xiaohongshu (小红书) | Jina Reader |
| RSS | feedparser |
| Any web page | Jina Reader (fallback) |

## Install

```bash
pip install x-reader
```

With Telegram support:
```bash
pip install "x-reader[telegram]"
```

## Quick Start

```bash
# Fetch a single URL
x-reader https://mp.weixin.qq.com/s/abc123

# Fetch a tweet
x-reader https://x.com/elonmusk/status/123456

# Fetch a Bilibili video
x-reader https://www.bilibili.com/video/BV1xx411c7XW

# Fetch a Xiaohongshu note
x-reader https://www.xiaohongshu.com/explore/abc123

# Fetch multiple URLs at once
x-reader https://url1.com https://url2.com

# View inbox
x-reader list
```

## How It Works

```
URL → Platform Detection → Fetcher → Unified Schema → Inbox (JSON + Markdown)
```

1. **Platform Detection** — auto-detects which platform a URL belongs to
2. **Fetcher** — uses the best method for each platform (API, Jina Reader, feedparser)
3. **Unified Schema** — normalizes all content into one format (`UnifiedContent`)
4. **Dual Output** — saves to `unified_inbox.json` (for AI) and optional Markdown (for you)

## Configuration

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

Required for Telegram only:
- `TG_API_ID` — from https://my.telegram.org
- `TG_API_HASH` — from https://my.telegram.org

Optional:
- `INBOX_FILE` — path to inbox JSON (default: `./unified_inbox.json`)
- `OUTPUT_DIR` — directory for Markdown output (default: disabled)

## Use as Library

```python
import asyncio
from x_reader.reader import UniversalReader

async def main():
    reader = UniversalReader()
    content = await reader.read("https://mp.weixin.qq.com/s/abc123")
    print(content.title)
    print(content.content[:200])

asyncio.run(main())
```

## Architecture

```
x_reader/
├── cli.py          # CLI entry point
├── reader.py       # URL dispatcher (UniversalReader)
├── schema.py       # Unified data model (UnifiedContent + Inbox)
├── fetchers/
│   ├── jina.py     # Jina Reader (universal fallback)
│   ├── bilibili.py # Bilibili API
│   ├── rss.py      # feedparser
│   ├── telegram.py # Telethon
│   ├── twitter.py  # Jina-based
│   ├── wechat.py   # Jina-based
│   ├── xhs.py      # Jina-based
│   └── youtube.py  # Jina-based
└── utils/
    └── storage.py  # JSON + Markdown dual output
```

## License

MIT
