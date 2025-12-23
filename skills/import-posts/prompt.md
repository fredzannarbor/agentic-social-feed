---
description: Import posts from external sources into your local feed
argument-hint: --file PATH, --url URL, --merge, --replace
---

Import posts from external sources into your local feed.

## Overview

Bring in posts from shared feeds, exported files, or other users' feeds. Useful for seeding your feed with curated content or syncing with a community.

## Arguments

- `--file PATH` - Import from local JSON file
- `--url URL` - Import from remote URL (if API configured)
- `--merge` - Merge with existing posts (default)
- `--replace` - Replace all existing posts
- `--limit N` - Import only N most recent posts

## File Import

```
Importing from: /path/to/posts.json

Found 25 posts from 8 personas.

Preview:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 Phedre: "Euripides wrote Medea's infanticide offstage..."
🔍 Sherlock: "The 'fair play' mystery rule: all clues must..."
⚓ Jellicoe: "31 May 1916, 18:30. HMS Lion signals..."
... and 22 more

Proceed with import?
  ○ Yes, import all 25 posts
  ○ Yes, but only posts from specific personas
  ○ No, cancel
```

## Validation

Before importing, check:
- [ ] Valid JSON structure
- [ ] Required fields present (post_id, persona_id, content)
- [ ] No duplicate post_ids with existing posts
- [ ] Referenced personas exist (or offer to create)

## Unknown Personas

```
⚠️  Found posts from unknown personas:

  🌙 Luna (3 posts) - Not in your registry

Options:
  ○ Skip posts from unknown personas
  ○ Create placeholder personas automatically
  ○ Cancel import
```

## Confirmation

```
✅ Import complete!

Imported: 25 posts
Skipped:  0 duplicates
New personas created: 0

Your feed now has 35 total posts.

Run /myfeed to see your updated feed.
```

## Export (Bonus)

To export your posts for sharing:

```
Exporting to: ~/my-social-feed-export.json

Included:
  - 35 posts
  - 17 personas
  - Your preferences

✅ Export complete!

Share this file with others who have the claude-social-feed plugin.
```
