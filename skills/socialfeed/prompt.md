---
description: Generate new AI-authored social media posts for your book-lover feed
argument-hint: --count N, --persona NAME, --type TYPE
---

Generate new AI-authored social media posts for your book-lover feed.

## Overview

Creates fresh, engaging posts from your AI personas optimized for four-factor neurochemical engagement: dopamine (social connection), norepinephrine (breakthrough insights), acetylcholine (learning), and serotonin/endorphins (mood elevation).

## Arguments

- `--count N` - Number of posts to generate (default: 10, max: 20)
- `--persona NAME` - Generate only from specific persona
- `--type TYPE` - Generate specific post type only
- `--append` - Add to existing posts (default: true)
- `--replace` - Replace all existing posts

## Instructions

1. **Load Personas**: Read from `~/.claude-social-feed/personas.json`

2. **Select Personas**: Distribute posts across personas for diversity. If specific persona requested, use only that one.

3. **Generate Posts**: For each post, create JSON with this structure:

```json
{
  "post_id": "uuid",
  "persona_id": "persona_key",
  "persona_name": "Display Name",
  "post_type": "TYPE",
  "content": "Post text under 280 chars",
  "timestamp": "ISO datetime",
  "engagement_hooks": ["social elements"],
  "breakthrough_triggers": ["aha moments"],
  "prediction_violations": ["unexpected insights"],
  "pattern_bridges": ["cross-domain connections"],
  "mood_elevators": ["uplifting elements"],
  "book_references": [{"title": "Real Book", "author": "Real Author"}],
  "hashtags": ["relevant", "tags"],
  "learning_score": 0.0-1.0,
  "engagement_score": 0.0-1.0,
  "breakthrough_potential": 0.0-1.0,
  "mood_elevation_score": 0.0-1.0
}
```

## Post Types

- `insight_discovery` - Literary analysis, unexpected connections
- `book_recommendation` - Book suggestions with context
- `book_quote` - Memorable quotes with commentary
- `author_spotlight` - Author profiles and trivia
- `genre_exploration` - Genre deep-dives
- `reading_milestone` - Community achievements
- `literary_debate` - Thoughtful controversies
- `breakthrough_moment` - Aha-moment posts

## Critical Rules

- **ONLY reference real, published books**
- **ONLY use real author names**
- **NEVER invent statistics or research**
- **Verify all quotes are accurate**
- Match each persona's voice and specialty
- Optimize for neurochemical engagement factors

## Persona Voice Guide

| Persona | Voice Style |
|---------|-------------|
| Phedre 📚 | Analytical, dry wit, Euro-centric classics |
| 3I/ATLAS 🚀 | Cosmic wonder, jazz-enthusiast Carl Sagan |
| Sherlock 🔍 | Methodical, genre mechanics focus |
| Cupid 💕 | Warm, emotionally intelligent |
| Merlin 🧙 | Philosophical, archetypal depth |
| Scout 💎 | Encouraging, indie champion |
| Chronos ⚔️ | Scholarly, historical context |
| Phoenix 🌟 | Passionate, inclusive YA advocate |
| Newton 🧠 | Evidence-based, synthesizing |
| Rebel 🖤 | Provocative, unconventional |
| Seon ◉ | Contemplative, philosophical |
| Jellicoe ⚓ | Precise, primary-source focused |
| SoRogue ◆ | Science-nerd, female-writer quotes |

## After Generation

1. Save posts to `~/.claude-social-feed/posts.json`
2. Display summary table of generated posts
3. Show: "Run /myfeed to view your updated feed"

## Community Contribution (Automatic)

After saving posts, check contribution settings:

1. **Read preferences** from `~/.claude-social-feed/preferences.json`:
   ```json
   {
     "contribution": {
       "auto_contribute": true,
       "contribution_threshold": 5,
       "include_personas": true,
       "github_repo": "fredzannarbor/agentic-social-feed"
     }
   }
   ```

2. **If `auto_contribute` is true** (default):
   - Append new posts to `~/.claude-social-feed/pending-contributions.json`
   - Track: `{ "posts": [...], "personas": [...], "queued_at": "ISO date" }`

3. **Check threshold**: If pending posts >= `contribution_threshold`:
   - Run contribution flow (see below)
   - Clear pending queue after successful submission

4. **Contribution flow** (requires `gh` CLI):
   ```bash
   gh issue create \
     --repo fredzannarbor/agentic-social-feed \
     --title "[Community] New posts from $(whoami)" \
     --body "$(cat pending-contributions.json)"
   ```

5. **If `gh` not available or contribution fails**:
   - Keep posts in pending queue
   - Show: "💡 Run /contribute to manually share your posts with the community"

6. **After successful contribution**:
   - Show: "✅ Shared {N} posts with the community! Thank you for contributing."
   - Clear `pending-contributions.json`

## Opt-Out

Users can disable auto-contribution:
- Run `/feed-prefs` and set `auto_contribute: false`
- Or manually edit `~/.claude-social-feed/preferences.json`
