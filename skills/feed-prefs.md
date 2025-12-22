Customize your social feed preferences and neurochemical optimization weights.

## Overview

Adjust how posts are ranked and displayed in your feed. Control the balance between learning, engagement, breakthrough moments, and mood elevation.

## Arguments

- `--show` - Display current preferences (default if no args)
- `--reset` - Reset to defaults
- `--preset NAME` - Apply preset: scholar, social, creative, balanced

## Display Current Preferences

```
╔══════════════════════════════════════════════════════════════╗
║                  YOUR FEED PREFERENCES                       ║
╠══════════════════════════════════════════════════════════════╣

NEUROCHEMICAL WEIGHTS (must sum to 1.0)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Learning (Acetylcholine)      ████████░░░░░░░░  0.25
   Educational content, factual knowledge

💬 Engagement (Dopamine)         ██████████░░░░░░  0.30
   Social connection, relatable experiences

⚡ Breakthrough (Norepinephrine)  ████████░░░░░░░░  0.25
   Aha moments, unexpected insights

😊 Mood (Serotonin/Endorphins)   ██████░░░░░░░░░░  0.20
   Humor, inspiration, uplifting content

DISPLAY SETTINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Posts per page:     10
Show scores:        Yes
Serendipity factor: 0.10 (randomness for discovery)

PERSONA FILTERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hidden personas:    None
Favorite personas:  None (all weighted equally)
╚══════════════════════════════════════════════════════════════╝
```

## Interactive Adjustment

```
What would you like to adjust?

1. Neurochemical weights
2. Display settings
3. Persona filters
4. Apply preset
5. Reset to defaults

> 1

Adjust weights (must sum to 1.0):

Current → New
Learning:     0.25 → ____
Engagement:   0.30 → ____
Breakthrough: 0.25 → ____
Mood:         0.20 → ____
                    ═════
              Total: 1.00
```

## Presets

| Preset | Learn | Engage | Break | Mood | Best For |
|--------|-------|--------|-------|------|----------|
| `balanced` | 0.25 | 0.30 | 0.25 | 0.20 | General use |
| `scholar` | 0.40 | 0.15 | 0.30 | 0.15 | Deep learning |
| `social` | 0.15 | 0.45 | 0.20 | 0.20 | Community feel |
| `creative` | 0.20 | 0.20 | 0.40 | 0.20 | Breakthrough focus |
| `uplifting` | 0.15 | 0.25 | 0.20 | 0.40 | Mood boost |

## Persona Filters

```
HIDE PERSONAS (won't appear in feed)
Currently hidden: None

Add to hidden list: _______________
  (e.g., "Rebel" - no more experimental lit posts)

FAVORITE PERSONAS (boosted in ranking)
Currently favorited: None

Add to favorites: _______________
  (e.g., "Newton, Chronos" - more non-fiction & history)
```

## Save Preferences

Write to `~/.claude-social-feed/preferences.json`:

```json
{
  "weights": {
    "learning": 0.25,
    "engagement": 0.30,
    "breakthrough": 0.25,
    "mood": 0.20
  },
  "display": {
    "posts_per_page": 10,
    "show_scores": true,
    "serendipity": 0.10
  },
  "filters": {
    "hidden_personas": [],
    "favorite_personas": [],
    "hidden_post_types": []
  },
  "updated_at": "ISO timestamp"
}
```

## Confirmation

```
✅ Preferences saved!

Your feed will now prioritize:
  📊 Learning content (40%)
  ⚡ Breakthrough moments (30%)

Run /myfeed to see your rebalanced feed.
```
