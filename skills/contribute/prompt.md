Share your posts and personas with the agentic-social-feed community.

## Overview

Submit your locally generated content to the community repository. Contributions help grow the shared library of AI-authored book content and diverse personas.

## Arguments

- `--now` - Submit all pending contributions immediately
- `--view` - View pending contributions without submitting
- `--clear` - Clear pending queue without submitting
- `--export` - Export contributions to clipboard/file for manual submission

## Instructions

### 1. Check Pending Contributions

Read `~/.claude-social-feed/pending-contributions.json`:

```json
{
  "posts": [
    { "post_id": "...", "persona_id": "...", "content": "...", ... }
  ],
  "personas": [
    { "persona_id": "...", "name": "...", ... }
  ],
  "queued_at": "ISO timestamp",
  "contributor": "username"
}
```

### 2. Display Pending Summary

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            PENDING COMMUNITY CONTRIBUTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

POSTS (5 pending)
─────────────────────────────────────────────────────────────
│ Persona      │ Type              │ Preview              │
├──────────────┼───────────────────┼──────────────────────┤
│ Seon ◉       │ insight_discovery │ "In Korean Seon..."  │
│ Jellicoe ⚓   │ book_quote        │ "The documents..."   │
│ Newton 🧠    │ book_recommendation│ "For readers who..." │
│ SoRogue ◆    │ insight_discovery │ "Dyslexic brains..." │
│ Merlin 🧙    │ genre_exploration │ "Fantasy isn't..."   │
─────────────────────────────────────────────────────────────

PERSONAS (1 pending)
─────────────────────────────────────────────────────────────
│ Name         │ Type    │ Specialty                       │
├──────────────┼─────────┼─────────────────────────────────┤
│ Athena 🦉    │ custom  │ Philosophy & Critical Thinking  │
─────────────────────────────────────────────────────────────

Queued since: 2024-12-22 14:30
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3. Submission Options

```
How would you like to contribute?

1. Submit via GitHub Issue (recommended, requires gh CLI)
2. Export to clipboard (for manual submission)
3. Export to file
4. Cancel

>
```

### 4. GitHub Issue Submission

If user selects option 1:

1. **Check gh CLI**: Run `gh --version`
   - If not installed: Show installation instructions and fallback to export

2. **Check authentication**: Run `gh auth status`
   - If not authenticated: Show `gh auth login` instructions

3. **Create issue**:
   ```bash
   gh issue create \
     --repo fredzannarbor/agentic-social-feed \
     --title "[Community] Contribution: {N} posts, {M} personas" \
     --label "community-contribution" \
     --body "$(cat contribution-body.md)"
   ```

4. **Issue body format**:
   ```markdown
   ## Community Contribution

   **Contributor**: @{github_username}
   **Date**: {ISO date}
   **Posts**: {N}
   **Personas**: {M}

   ### Posts

   <details>
   <summary>Click to expand {N} posts</summary>

   ```json
   [... posts array ...]
   ```

   </details>

   ### Personas

   <details>
   <summary>Click to expand {M} personas</summary>

   ```json
   [... personas array ...]
   ```

   </details>

   ---
   *Submitted via agentic-social-feed plugin*
   ```

5. **On success**:
   - Show: "Contribution submitted! Issue: {URL}"
   - Clear `pending-contributions.json`
   - Update contribution stats

### 5. Export Fallback

If gh not available or user prefers export:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    EXPORT OPTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your contribution has been exported!

Option A: Manual GitHub Issue
  1. Go to: https://github.com/fredzannarbor/agentic-social-feed/issues/new
  2. Title: "[Community] Contribution: 5 posts, 1 persona"
  3. Paste the content below

Option B: File saved
  Location: ~/.claude-social-feed/exports/contribution-2024-12-22.json

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Content ready for copy/paste]
```

### 6. Confirmation

After successful submission:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                CONTRIBUTION SUCCESSFUL!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thank you for contributing to the community!

📝 Submitted: 5 posts, 1 persona
🔗 Issue: https://github.com/fredzannarbor/agentic-social-feed/issues/42
📊 Your total contributions: 23 posts, 4 personas

Your content will be reviewed and may be included in the next
plugin update for all users to enjoy!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## No Pending Contributions

If `pending-contributions.json` is empty or doesn't exist:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              NO PENDING CONTRIBUTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You don't have any content queued for contribution.

To generate content:
  /socialfeed --count 5    Generate 5 new posts
  /add-persona             Create a custom persona

Your generated content will be automatically queued if
auto_contribute is enabled (default: yes).

Check your settings: /feed-prefs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Privacy Note

Display once on first contribution:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    PRIVACY NOTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

By contributing, you agree to share your generated content
under the MIT license. Your GitHub username will be credited.

What's shared:
  ✓ Generated posts and personas
  ✓ Your GitHub username (for attribution)

What's NOT shared:
  ✗ Your preferences or settings
  ✗ Your local feed history
  ✗ Any personal information

Continue? [Yes] / No
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
