---
description: Create a new custom AI persona for your social feed
argument-hint: --type TYPE, --quick, --from-template NAME
---

Create a new custom AI persona for your social feed.

## Overview

Interactively design a new persona with unique voice, specialty, and characteristics. The persona will be added to your local registry and can generate posts in your feed.

## Arguments

- `--type TYPE` - Persona type: social (default), publisher, editor
- `--quick` - Minimal prompts, use smart defaults
- `--from-template NAME` - Clone existing persona as starting point

## Interactive Flow

### Step 1: Basic Identity

```
╔══════════════════════════════════════════════════════════════╗
║                    CREATE NEW PERSONA                        ║
╠══════════════════════════════════════════════════════════════╣

What type of persona?
  ○ Social      - Creates feed content (posts, insights)
  ○ Publisher   - Imprint-level editorial voice
  ○ Editor      - Series-level specialist

Name: _______________
  (e.g., "Luna", "Hemingway", "DataDruid")

Glyph/Emoji: _____
  (Unique identifier, e.g., 🌙, ⚗️, 📊)

Handle: @_______________
  (Social media style, e.g., @LunaReads)
```

### Step 2: Specialty & Voice

```
Specialty area: _______________
  (e.g., "Speculative Fiction", "Data Science Books", "Poetry")

Writing style (describe in a few words): _______________
  (e.g., "Lyrical and dreamy with moon metaphors")

Personality traits (comma-separated): _______________
  (e.g., "contemplative, poetic, night-owl, cosmic")
```

### Step 3: Content Focus

```
Primary interests (3-5 topics): _______________
  (e.g., "lunar imagery, speculative worlds, dream logic, astronomy")

Neurochemical strength - what does this persona optimize for?
  ○ Learning (educational, factual)
  ○ Breakthrough (aha moments, unexpected connections)
  ○ Engagement (social, relatable)
  ○ Mood (inspiring, uplifting, humorous)
```

### Step 4: Additional Details (optional)

```
Bio (1-2 sentences): _______________

For Publishers:
  - Imprint name: _______________
  - Risk tolerance: Conservative / Moderate / Aggressive
  - Decision style: Data-driven / Intuitive / Collaborative

For Editors:
  - Series/focus: _______________
  - Expertise type: Subject expert / Technical / Literary
```

## Validation

Before saving, validate:
- [ ] Name is unique in registry
- [ ] Glyph is unique in registry
- [ ] Handle is unique in registry
- [ ] Required fields are filled

## Save Persona

Create JSON entry:

```json
{
  "persona_id": "lowercase_name",
  "persona_type": "social",
  "name": "Luna",
  "glyph": "🌙",
  "handle": "@LunaReads",
  "bio": "Nocturnal literary wanderer...",
  "specialty": "Speculative Fiction",
  "personality_traits": ["contemplative", "poetic"],
  "interests": ["lunar imagery", "speculative worlds"],
  "writing_style": "Lyrical and dreamy",
  "neurochemical_benefit": "Expands imagination through cosmic wonder",
  "active": true,
  "created_at": "ISO timestamp"
}
```

Append to `~/.claude-social-feed/personas.json`

## Confirmation

```
✅ Persona created successfully!

🌙 Luna (@LunaReads)
Type: Social | Specialty: Speculative Fiction
"Lyrical and dreamy with moon metaphors"

Your registry now has 18 personas.

💡 Run /socialfeed --persona Luna to generate posts from your new persona
```
