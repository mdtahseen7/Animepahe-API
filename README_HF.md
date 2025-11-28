---
title: Animepahe API
emoji: 🎬
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
app_port: 7860
---

# Animepahe API

A FastAPI-based web scraper for Animepahe.

## Endpoints

- `/search?q=naruto` - Search for anime
- `/episodes?session=anime-session` - Get episodes for an anime
- `/sources?anime_session=xxx&episode_session=yyy` - Get video sources
- `/m3u8?url=kwik-url` - Resolve m3u8 URL from kwik link
- `/health` - Health check
