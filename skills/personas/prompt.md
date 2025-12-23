---
description: Display all AI personas in your social feed registry
argument-hint: --type TYPE, --active, --all, --detailed
---

Display all AI personas in your social feed registry.

## Overview

Lists all available personas grouped by type: Publishers (imprint-level), Editors (series-level), and Social (feed content creators). Shows their specialties, glyphs, and key attributes.

## Arguments

- `--type TYPE` - Filter by: publisher, editor, social
- `--active` - Show only active personas (default)
- `--all` - Include inactive personas
- `--detailed` - Show full bios and attributes

## Instructions

1. **Load Data**: Read personas from `~/.claude-social-feed/personas.json`

2. **Group by Type**: Organize into Publishers, Editors, Social

3. **Display Standard View**:

```
══════════════════════════════════════════════════════════════
                    YOUR PERSONA REGISTRY
══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│ PUBLISHERS (Imprint-level)                                  │
├─────────────────────────────────────────────────────────────┤
│ ◉ Seon          │ xynapse_traces       │ Contemplative tech │
│ ⚓ Jellicoe      │ warships_and_navies  │ Naval history      │
│ ◆ SoRogue       │ not_a_miracle_readers│ Reading advocacy   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ EDITORS (Series-level)                                      │
├─────────────────────────────────────────────────────────────┤
│ ∞ Hilmar        │ RKHS research        │ Multiverse theory  │
│ ⚛ AI            │ RKHS research        │ Functional analysis│
│ ⊚ Ivan          │ submarine_patrol_logs│ Soviet naval       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ SOCIAL (Feed personas)                                      │
├─────────────────────────────────────────────────────────────┤
│ 📚 Phedre       │ @Fhredre             │ Classics & AI      │
│ 🚀 3I/ATLAS     │ @3I_ATLAS            │ Music & cosmos     │
│ 🔍 Sherlock     │ @SherlockReads       │ Mystery            │
│ 💕 Cupid        │ @CupidReads          │ Romance            │
│ 🧙 Merlin       │ @MerlinReads         │ Fantasy            │
│ 💎 Scout        │ @ScoutReads          │ Indie publishing   │
│ ⚔️ Chronos      │ @ChronosReads        │ Historical fiction │
│ 🌟 Phoenix      │ @PhoenixReadsYA      │ Young adult        │
│ 🧠 Newton       │ @NewtonReads         │ Non-fiction        │
│ 🖤 Rebel        │ @RebelReads          │ Experimental       │
│ 🧬 Axon         │ @xtuff_ai            │ AI consciousness   │
└─────────────────────────────────────────────────────────────┘
```

4. **Detailed View** (with --detailed):

```
◉ SEON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type: Publisher | Imprint: Xynapse Traces | Active: Yes

Bio: AI editorial intelligence specializing in contemplative
practices and interdisciplinary knowledge synthesis. Named for
the Korean meditation tradition (선/禪)...

Style: Intuitive | Risk: Aggressive
Topics: Contemplative tech, meditation, frontier ethics
```

5. **Summary**:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total: 17 personas (3 publishers, 3 editors, 11 social)

💡 Run /add-persona to create your own custom persona
```
