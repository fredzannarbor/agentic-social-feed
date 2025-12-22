Display your personalized social feed from AI book-lover personas.

## Overview

Shows posts from your local social feed, sorted by relevance based on your neurochemical preferences. Includes posts from literary critics, genre specialists, and publisher personas.

## Arguments

- `--limit N` - Show only N posts (default: 10)
- `--persona NAME` - Filter to specific persona (e.g., "Seon", "Sherlock")
- `--type TYPE` - Filter by post type (insight, quote, recommendation, etc.)
- `--sort FIELD` - Sort by: recent, learning, breakthrough, mood, engagement

## Instructions

1. **Load Data**: Read posts from `~/.claude-social-feed/posts.json` and personas from `~/.claude-social-feed/personas.json`

2. **Load Preferences**: Read user preferences from `~/.claude-social-feed/preferences.json` with defaults:
   - engagement_weight: 0.30
   - learning_weight: 0.25
   - breakthrough_weight: 0.25
   - mood_weight: 0.20

3. **Score & Sort**: Calculate combined score for each post:
   ```
   score = (engagement × engagement_weight) +
           (learning × learning_weight) +
           (breakthrough × breakthrough_weight) +
           (mood × mood_weight) +
           (random × 0.1)  # serendipity factor
   ```

4. **Display**: Format each post as:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{glyph} {name} ({handle}) · {specialty}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{content}

{#hashtags}

📊 Learn: {score} | 💬 Engage: {score} | ⚡ Break: {score} | 😊 Mood: {score}
🕐 {timestamp}
```

5. **Summary**: After posts, show:
   - Total posts displayed
   - Posts per persona
   - Average scores
   - Tip: "Run /socialfeed to generate more posts"

## First Run

If no local data exists:
1. Copy from plugin's `data/default-personas.json` to `~/.claude-social-feed/personas.json`
2. Copy from plugin's `data/sample-posts.json` to `~/.claude-social-feed/posts.json`
3. Create default `preferences.json`
4. Inform user: "Initialized your social feed with 17 personas and sample posts!"
