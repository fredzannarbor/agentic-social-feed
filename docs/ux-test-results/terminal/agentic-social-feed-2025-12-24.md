# Terminal UX Test: agentic-social-feed Plugin

**Date:** 2025-12-24
**Plugin Version:** 2.0.0
**Tester:** Virtual UX Framework (7 personas)

---

## Executive Summary

The `agentic-social-feed` Claude Code plugin provides 9 slash commands for an AI-powered book-lover social feed. Overall engagement score: **3.7/5**. The plugin excels at natural language interaction, onboarding (/demo), and persona creation. Key friction points center around accessibility (screen reader-hostile visual formatting), lack of JSON output for automation, and the inherent limitation of being a Claude Code skill rather than standalone CLI.

**Top 3 Fixes:**
1. Add text alternatives to progress bars (accessibility)
2. Support JSON output via `--format json` or natural language
3. Suggest /demo on first interaction (onboarding)

---

## Session Summaries

### Session 1: Elena Vasquez (Power User, CLI 5/5)
**Goal:** Script automated content generation
**Outcome:** Partial
**Score:** 3.4/5

Key findings:
- No `--help` convention
- No JSON output mode for scripting
- Natural language fallback works
- GitHub CLI integration for contributions

### Session 2: Marcus Johnson (Casual User, CLI 2/5)
**Goal:** Discover books for library reading club
**Outcome:** Completed
**Score:** 4.4/5

Key findings:
- Social media format immediately familiar
- /showmethescience explains neurochemical scores
- Natural language preferences work seamlessly
- Persona creation (Dewey) was rewarding

### Session 3: Janet Williams (Accessibility User, CLI 3/5)
**Goal:** Evaluate screen reader accessibility
**Outcome:** Partial
**Score:** 2.2/5

Key findings:
- Box-drawing characters are screen reader noise
- Progress bar blocks read as "block element" repeatedly
- Can request plain text via natural language
- Visual-first design excludes screen reader users

### Session 4: Kyle Chen (DevOps, CLI 4/5)
**Goal:** Add to team content pipeline
**Outcome:** Partial
**Score:** 4.0/5

Key findings:
- Graceful auto-initialization on missing files
- JSON config files are version-controllable
- Cannot run outside Claude Code sessions
- No programmatic exit codes

### Session 5: Priya Sharma (First-time User, CLI 1/5)
**Goal:** Find Greek tragedy content for thesis
**Outcome:** Completed
**Score:** 4.8/5

Key findings:
- /demo provides excellent onboarding
- Persona filtering by topic works well
- Natural language export to file
- Immediately found thesis-relevant content

### Session 6: Yuki Tanaka (Non-native English, CLI 3/5)
**Goal:** Evaluate for translation context
**Outcome:** Completed
**Score:** 4.2/5

Key findings:
- Clear, jargon-free language
- Concise 2-3 word descriptions
- No idioms or colloquialisms
- Format hints in prompts

### Session 7: Brian Murphy (Windows/PowerShell, CLI 3/5)
**Goal:** Evaluate for school book club
**Outcome:** Completed (with reservations)
**Score:** 3.6/5

Key findings:
- Works in VS Code terminal on Windows
- File-based storage is portable
- No content filtering for mature themes
- Custom personas as workaround

---

## CLI UX Issues (Priority Ranked)

### P1 - Critical

| Issue | Sessions | Fix |
|-------|----------|-----|
| Screen reader inaccessibility | 1/7 | Add text alternatives to progress bars |
| No JSON output mode | 2/7 | Support `--format json` or natural language |
| Not usable outside Claude Code | 2/7 | Document limitations, consider companion CLI |

### P2 - Important

| Issue | Sessions | Fix |
|-------|----------|-----|
| No first-run guidance | 1/7 | Suggest /demo on first interaction |
| No --help convention | 1/7 | Interpret --help as doc request |
| Silent parameter correction | 1/7 | Warn when capping values |

### P3 - Nice to Have

| Issue | Sessions | Fix |
|-------|----------|-----|
| No content filtering | 1/7 | Add content_rating to posts |
| Box-drawing noise | 1/7 | Use markdown headers instead |

---

## Neurochemical Analysis

| Chemical | Score | Strengths | Improvements |
|----------|-------|-----------|--------------|
| Dopamine | 3.9/5 | Checkmarks, persona creation | Accessibility bars |
| Serotonin | 3.7/5 | /demo onboarding, clear language | --help, validation |
| Norepinephrine | 3.7/5 | Emoji hierarchy, presets | Box-drawing noise |
| Oxytocin | 3.7/5 | Auto-init, natural language | Content filtering |
| Endorphins | 3.4/5 | Persona creation, theme | Accessibility exclusion |

**Overall: 3.7/5**

---

## Recommended Implementation

### Quick Wins (< 1 hour total)

1. **Text alternatives for progress bars:**
```
Current:  Learn: ████████░░ 0.88
Better:   Learn: 88% ████████░░
Best:     📊 Learn: 88%
```

2. **Handle --help in skills:**
```
If user types "/myfeed --help":
  Show SKILL.md content or link to /demo
```

3. **First-run suggestion:**
```
On first plugin interaction:
  "Welcome to agentic-social-feed! Type /demo for a walkthrough."
```

### Medium-Term Improvements

1. **JSON output support:**
```
/myfeed --format json
or
"Show my feed as JSON"
```

2. **Accessibility mode:**
```
/feed-prefs --accessible true
→ Disables box-drawing, uses plain text
```

3. **Content rating:**
```json
{
  "post_id": "...",
  "content_rating": "general" | "teen" | "mature"
}
```

---

## Accessibility Assessment

| Aspect | Status | Notes |
|--------|--------|-------|
| Color-only info | Pass | No colors for meaning |
| Screen reader | Fail | Box-drawing, progress blocks |
| High contrast | Pass | No color dependencies |
| Text alternatives | Fail | Progress bars need text |

**Recommendation:** Add `--plain` or `--accessible` mode that:
- Removes box-drawing characters
- Shows percentages instead of bar graphics
- Uses markdown headers instead of Unicode borders

---

## Scriptability Assessment

| Aspect | Status | Notes |
|--------|--------|-------|
| Exit codes | N/A | Claude Code skill limitation |
| JSON output | Missing | Achievable via natural language |
| Non-interactive | Partial | Requires Claude session |
| Idempotency | Safe | Non-destructive operations |
| Offline mode | Good | Local files, no API needed |

---

## Appendix: Persona Satisfaction Ranking

| Persona | Score | Notes |
|---------|-------|-------|
| Priya (First-time) | 4.8/5 | Best experience - /demo + natural language |
| Marcus (Casual) | 4.4/5 | Social format + persona creation |
| Yuki (Non-native) | 4.2/5 | Clear language throughout |
| Kyle (DevOps) | 4.0/5 | Resilient, but can't automate |
| Brian (Windows) | 3.6/5 | Works, but needs content filter |
| Elena (Power) | 3.4/5 | No JSON, can't script |
| Janet (Accessibility) | 2.2/5 | Visual-first excludes her |

**Key Insight:** The plugin is excellent for casual and first-time users, but struggles with power users (automation) and accessibility users (screen readers).
