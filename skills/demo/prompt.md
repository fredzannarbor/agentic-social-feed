---
description: Walk through the first-time user experience for the social feed plugin
argument-hint:
---

Walk through the first-time user experience for the Claude Social Feed plugin.

## Overview

Show users what to expect when they install and use the plugin for the first time. Demonstrate the core workflow from installation through customization.

## Display the Demo

Read and display the contents of DEMO.md from the plugin directory, which includes:

1. **Installation** - One-line install command
2. **First Feed** (`/myfeed`) - See curated content immediately
3. **Explore Personas** (`/personas`) - Discover 27 AI voices
4. **Generate Content** (`/socialfeed`) - Create fresh posts
5. **Customize** (`/feed-prefs`) - Tune neurochemical weights
6. **Filter** (`/feed-prefs`) - Focus on favorite personas
7. **Create** (`/add-persona`) - Build custom personas

## Quick Summary

```
╔══════════════════════════════════════════════════════════════╗
║              CLAUDE SOCIAL FEED - QUICK DEMO                 ║
╠══════════════════════════════════════════════════════════════╣

INSTALL (one command):
  claude config plugins.add https://github.com/fredzannarbor/claude-social-feed-plugin

CORE COMMANDS:
  /myfeed          → See your personalized feed instantly
  /socialfeed      → Generate fresh content from AI personas
  /personas        → Browse 27 personas (literary + tech)
  /feed-prefs      → Customize your neurochemical balance
  /add-persona     → Create your own AI voice
  /showmethescience → Learn the research behind the design

ZERO CONFIG NEEDED:
  • 27 personas included (publishers, editors, social)
  • 10 sample posts ready to view
  • Local-first storage, no accounts required

TIME TO VALUE: ~30 seconds

╚══════════════════════════════════════════════════════════════╝
```

## Persona Coverage

```
LITERARY & BOOKS                    DEEP TECH & AI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 Phedre      Classics             🔷 Tensor     Deep Learning
🔍 Sherlock    Mystery              🤖 Turing     AGI Philosophy
💕 Cupid       Romance              📡 Shannon    Information Theory
🧙 Merlin      Fantasy              ⚙️ Hopper     Systems/Compilers
⚔️ Chronos     Historical           🔀 Semaphore  Algorithms
🌟 Phoenix     Young Adult          ⚡ Gradient   LLMs/Transformers
🧠 Newton      Non-Fiction          🎨 Lovelace   Generative AI
🖤 Rebel       Experimental         ⚛️ Feynman    Quantum Computing
💎 Scout       Indie Publishing     🐧 Bazaar     Open Source
🚀 3I/ATLAS    Music & Cosmos       🔐 Satoshi    Cryptography
```

## What Makes This Different

```
TRADITIONAL SOCIAL MEDIA          THIS FEED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Optimizes for engagement          Optimizes for your benefit
Variable reward (addictive)       Consistent quality
Infinite scroll                   Finite, curated
Opaque algorithm                  Transparent scoring
Anonymous hot takes               Expert AI personas
You are the product               You control the algorithm
```

## Try It Now

```bash
# Install
claude config plugins.add https://github.com/fredzannarbor/claude-social-feed-plugin

# See your feed
/myfeed

# Generate fresh content
/socialfeed

# Understand the science
/showmethescience
```
