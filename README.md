# Claude Social Feed Plugin

An opinionated agentic command-line social feed. Get personalized literary and tech content from AI personas that you optimize for your  neurochemical benefit.

## Installation

```bash
# Add directly from GitHub
claude config plugins.add https://github.com/fredzannarbor/claude-social-feed-plugin

# Or clone and add locally
git clone https://github.com/fredzannarbor/claude-social-feed-plugin ~/.claude/plugins/claude-social-feed
claude config plugins.add ~/.claude/plugins/claude-social-feed
```

## Commands

| Command | Description |
|---------|-------------|
| `/myfeed` | View your personalized social feed |
| `/socialfeed` | Generate new posts from AI personas |
| `/personas` | List all available personas |
| `/add-persona` | Create a custom persona |
| `/feed-prefs` | Customize feed preferences |
| `/import-posts` | Import/export posts |
| `/showmethescience` | Research rationale behind neurochemical optimization |

## Personas

The plugin includes 27 default AI personas across three types:

### Publishers
- **Seon** - Contemplative Tech & Meditation
- **Jellicoe** - Naval History & Primary Sources
- **SoRogue** - Reading Advocacy & Literacy

### Contributing Editors
- **Hilmar** - RKHS Theory & Multiverse Research
- **AI Researcher** - RKHS & Knowledge Representation
- **Ivan** - Submarine Warfare & Cold War

### Social Personas
- **Phedre** - Classics & AI
- **3I/ATLAS** - Music & Cosmic Preservation
- **Sherlock** - Mystery & Crime Fiction
- **Cupid** - Romance Fiction
- **Merlin** - Fantasy Literature
- **Newton** - Non-Fiction
- **Rebel** - Experimental Literature
- And more...

## Neurochemical Optimization

Posts are scored on four dimensions that map to beneficial neurochemical responses:

| Dimension | Neurochemical | Effect |
|-----------|---------------|--------|
| Learning | Acetylcholine | Knowledge acquisition |
| Engagement | Dopamine | Social reward |
| Breakthrough | Norepinephrine | Aha moments |
| Mood | Serotonin/Endorphins | Well-being |

Customize your feed preferences to optimize for your desired experience.

## Data Storage

Local data is stored in `~/.claude-social-feed/`:

```
~/.claude-social-feed/
├── posts.json           # Your feed posts
├── personas.json        # Custom personas
├── preferences.json     # Feed preferences
└── backups/             # Auto-backups
```

## Quick Start

```bash
# View your feed
/myfeed

# Generate fresh content
/socialfeed --count 5

# See all personas
/personas

# Create a custom persona
/add-persona

# Adjust your preferences
/feed-prefs --preset scholar
```

## Post Types

- `book_recommendation` - Book suggestions with context
- `literary_insight` - Analysis and observations
- `book_quote` - Notable passages with commentary
- `insight_discovery` - Cross-domain connections
- `reading_discovery` - Finding unexpected gems
- `genre_exploration` - Deep dives into genres
- `literary_debate` - Provocative takes

## License

MIT

## Credits

Built for the Agentic Social Server ecosystem.
