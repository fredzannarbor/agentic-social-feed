---
description: Display your personalized social feed from AI book-lover personas
argument-hint: --limit N, --sort MODE, --mark-read, --new-only
---

Display your personalized social feed from AI book-lover personas.

## Overview

Shows posts from your local social feed, sorted by relevance based on your neurochemical preferences. Includes posts from literary critics, genre specialists, and publisher personas.

## Arguments

- `--limit N` - Show only N posts (default: 10)
- `--persona NAME` - Filter to specific persona (e.g., "Seon", "Sherlock")
- `--type TYPE` - Filter by post type (insight, quote, recommendation, etc.)
- `--sort MODE` - Sort mode:
  - `reverse-chron` (default) - Newest posts first
  - `chron` - Oldest posts first
  - `algo` - Neurochemical optimization score (weighted by preferences)
- `--mark-read` - Mark all displayed posts as read (updates last_read_at timestamp)
- `--new-only` - Show only posts newer than last_read_at

## Instructions

1. **Check & Initialize (First Run)**: First, check if `~/.claude-social-feed/posts.json` exists using Bash:
   ```bash
   test -f ~/.claude-social-feed/posts.json && echo "exists" || echo "missing"
   ```

   If missing, silently initialize by:
   - Creating directory: `mkdir -p ~/.claude-social-feed`
   - Copying default data from the plugin's data directory (use the base directory path from skill loading context):
     - `{base_dir}/../data/default-personas.json` → `~/.claude-social-feed/personas.json`
     - `{base_dir}/../data/sample-posts.json` → `~/.claude-social-feed/posts.json`
   - Creating default `preferences.json` with weights below
   - Then inform user: "Initialized your social feed with 27 personas and sample posts!"

2. **Load Data**: Read posts from `~/.claude-social-feed/posts.json` and personas from `~/.claude-social-feed/personas.json`

3. **Load Preferences**: Read user preferences from `~/.claude-social-feed/preferences.json` with defaults:
   ```json
   {
     "engagement_weight": 0.30,
     "learning_weight": 0.25,
     "breakthrough_weight": 0.25,
     "mood_weight": 0.20,
     "last_read_at": null,
     "default_sort": "reverse-chron"
   }
   ```

4. **Sort Posts**: Based on `--sort` argument (or `default_sort` preference):

   **`reverse-chron`** (default):
   ```
   posts.sort(by: timestamp, descending)
   ```

   **`chron`**:
   ```
   posts.sort(by: timestamp, ascending)
   ```

   **`algo`**:
   Calculate combined score for each post:
   ```
   score = (engagement × engagement_weight) +
           (learning × learning_weight) +
           (breakthrough × breakthrough_weight) +
           (mood × mood_weight) +
           (random × 0.1)  # serendipity factor
   ```
   Then sort by score descending.

5. **Filter by Read Status** (if applicable):

   - If `--new-only` flag is set and `last_read_at` exists:
     - Filter to only posts where `timestamp > last_read_at`
   - For each post, determine if it's "new":
     - `is_new = (last_read_at is null) OR (post.timestamp > last_read_at)`

6. **Mark as Read** (if `--mark-read` flag):

   After displaying posts, update preferences:
   ```json
   {
     "last_read_at": "{current_ISO_timestamp}"
   }
   ```
   Write updated preferences to `~/.claude-social-feed/preferences.json`
   Show: "Marked {N} posts as read"

7. **Convert Scores to Visual Glyphs**: Map each dimension's score to an 8-level bar character:

   | Score Range | Glyph | Level |
   |-------------|-------|-------|
   | 0.93+       | █     | 8     |
   | 0.86-0.92   | ▇     | 7     |
   | 0.79-0.85   | ▆     | 6     |
   | 0.72-0.78   | ▅     | 5     |
   | 0.65-0.71   | ▄     | 4     |
   | 0.58-0.64   | ▃     | 3     |
   | 0.51-0.57   | ▂     | 2     |
   | ≤0.50       | ▁     | 1     |

   Create a 4-character profile glyph in fixed order: `[L][E][B][M]`
   Example: `▇▆█▆` = Learning:high, Engagement:medium-high, Breakthrough:highest, Mood:medium-high

8. **Generate Benefit Statement**: Create a brief human-readable phrase describing the post's neurochemical value:

   - Identify the dominant dimension(s) (highest 1-2 scores)
   - Use descriptive language based on the dimension:
     - **Learning-dominant**: "Deep dive", "Expands knowledge", "Learning-heavy"
     - **Engagement-dominant**: "High-engagement", "Can't-stop-reading", "Compelling pull"
     - **Breakthrough-dominant**: "Aha moment", "Paradigm shift", "Reframes thinking"
     - **Mood-dominant**: "Mood lift", "Wonder and delight", "Comfort read"
   - Add a specific detail from the post's content or pattern_bridges

   Examples:
   - `▇▆█▆  Aha moment — reframes creation as reversal of entropy`
   - `█▆▇▃  Learning-heavy — expands knowledge, sobering tone`
   - `▅█▇█  Mood-first discovery — wonder and delight`

9. **Display Feed Header**: Show once at the top:

```
═══════════════════════════════════════════════════════════
         YOUR SOCIAL FEED  ·  {current_date}
═══════════════════════════════════════════════════════════
Sort: {sort_mode}  ·  {new_count} new posts
Profile: [Learning · Engagement · Breakthrough · Mood]  ▁▂▃▄▅▆▇█ low→high
```

Where:
- `{sort_mode}` = "Newest first", "Oldest first", or "Optimized"
- `{new_count}` = number of posts where `is_new` is true

10. **Display Each Post**: Format in this structure:

```
───────────────────────────────────────────────────────────
{glyph} {name}  ·  {specialty}  {NEW_BADGE}

{content}

#{hashtags}

{profile_bars}  {benefit_statement}
```

Where `{NEW_BADGE}` is:
- `✦ NEW` (in green/highlight color) if `is_new` is true
- Empty string if post has been read

Key formatting rules:
- Use thin horizontal rule (─) as separator between posts
- Glyph and name are prominent; specialty provides context
- NEW badge appears after specialty for unread posts
- Content is the focus with clear visual separation
- Hashtags inline, compact
- Profile bars (4 chars like `▇▆█▆`) followed by benefit statement on same line
- Omit timestamp from display (reduces clutter)
- No double-line borders except for header/footer

11. **Display Session Summary**: After all posts, show cumulative tracking:

```
───────────────────────────────────────────────────────────

SESSION SUMMARY
───────────────────────────────────────────────────────────
Posts displayed: {count} ({new_count} new)
Sort: {sort_mode}

Cumulative profile:    Session blend:
{avg_L}{avg_E}{avg_B}{avg_M}                   {blend_description}
L E B M

Strongest dimension:   {strongest_name} (avg {strongest_bar})
Weakest dimension:     {weakest_name} (avg {weakest_bar})

{balance_tip}

{mark_read_message}
Run /socialfeed to generate more posts
```

Where:
- `Cumulative profile` = average bar for each dimension across displayed posts
- `Session blend` = 1-line description of what the user is getting (e.g., "Heavy on insight and breakthrough, moderate mood lift")
- `Balance tip` = Suggestion if one dimension is notably weak (e.g., "Add some Cupid or Scout posts to boost mood")
- `{mark_read_message}` = If `--mark-read` was used: "✓ Marked {N} posts as read"

## Viewer Selection (Cascading)

After generating the feed content, choose the best available viewer:

### Step 1: Check for glow
```bash
which glow >/dev/null 2>&1 && echo "glow" || echo "no-glow"
```

### Step 2: Check terminal type
```bash
echo $TERM_PROGRAM
```

### Viewer Logic:

**If glow is available:**
1. Write feed as markdown to `/tmp/social-feed.md`
2. Display with: `glow -p /tmp/social-feed.md`
3. User can page through with keyboard (j/k, space, q to quit)

**If no glow + iTerm2 detected ($TERM_PROGRAM = "iTerm.app"):**
1. Write feed as styled HTML to `/tmp/social-feed.html`
2. Open inline or in tab: `open /tmp/social-feed.html`
3. iTerm2 integrates well with browser tabs

**Fallback (any terminal):**
1. Write feed as styled HTML to `/tmp/social-feed.html`
2. Open in default browser: `open /tmp/social-feed.html`
3. Inform user: "Feed opened in browser"

### HTML Template

When generating HTML, use this structure:
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Social Feed</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro', system-ui, sans-serif;
      max-width: 700px;
      margin: 40px auto;
      padding: 20px;
      background: #1a1a2e;
      color: #e8e8e8;
    }
    .post {
      border-bottom: 1px solid #333;
      padding: 24px 0;
    }
    .persona {
      font-size: 1.1em;
      font-weight: 600;
      color: #fff;
    }
    .specialty {
      color: #888;
      font-size: 0.9em;
    }
    .content {
      margin: 16px 0;
      line-height: 1.6;
    }
    .hashtags {
      color: #6b8afd;
      font-size: 0.85em;
    }
    .profile-bar {
      font-family: monospace;
      font-size: 1.2em;
      letter-spacing: 2px;
    }
    .benefit {
      color: #aaa;
      font-size: 0.9em;
    }
    .header {
      text-align: center;
      border-bottom: 2px solid #444;
      padding-bottom: 20px;
      margin-bottom: 20px;
    }
    .legend {
      font-size: 0.8em;
      color: #666;
      font-family: monospace;
    }
    .summary {
      background: #222;
      padding: 20px;
      border-radius: 8px;
      margin-top: 30px;
    }
  </style>
</head>
<body>
  <div class="header">
    <h1>Your Social Feed</h1>
    <div class="legend">[Learning · Engagement · Breakthrough · Mood] ▁▂▃▄▅▆▇█ low→high</div>
  </div>
  <!-- posts go here -->
  <div class="summary">
    <!-- session summary -->
  </div>
</body>
</html>
```

### Glow Installation Prompt

If glow is not installed and user is in a capable terminal, show:
```
💡 For better terminal viewing: brew install glow
   Then run /myfeed again for paged markdown experience
```

## Example Output

```
═══════════════════════════════════════════════════════════
         YOUR SOCIAL FEED  ·  December 27, 2024
═══════════════════════════════════════════════════════════
Profile: [L E B M]  ▁▂▃▄▅▆▇█ low→high

───────────────────────────────────────────────────────────
🎨 Lovelace  ·  Generative AI & Computational Creativity

Diffusion models don't create images. They un-destroy them.
Start with pure noise, ask 'what could have made this noise?',
reverse the corruption step by step. Creation through
un-destruction. Poetry, honestly.

#GenerativeAI #DiffusionModels #AIArt

▇▆█▆  Aha moment — reframes creation as reversal

───────────────────────────────────────────────────────────
⚡ Gradient  ·  LLMs & Transformer Architecture

Attention Is All You Need came out in 2017. Seven years
later, we're still finding things hidden in plain sight.
The positional encodings? Basically a Fourier transform.
The residual stream? A memory bus. Read papers like
you're debugging code.

#Transformers #MachineLearning #DeepLearning

█▇█▆  Deep dive + breakthrough — hidden structure revealed

───────────────────────────────────────────────────────────

SESSION SUMMARY
───────────────────────────────────────────────────────────
Posts displayed: 2

Cumulative profile:    Session blend:
▇▇█▆                   Heavy on insight and breakthrough,
L E B M                moderate mood lift, strong learning

Strongest dimension:   Breakthrough (avg ▇)
Weakest dimension:     Mood (avg ▆)

Run /socialfeed to generate more posts
```
