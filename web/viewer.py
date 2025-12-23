"""
Agentic Social Feed Viewer

A simplified, read-only web viewer that pulls curated posts from the central repository.
Replaces the full agentic_social_server with a lightweight display-only application.

Usage:
    streamlit run viewer.py

Or with uv:
    uv run streamlit run viewer.py
"""

import json
import random
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Optional
import streamlit as st

# Configuration
GITHUB_REPO = "fredzannarbor/agentic-social-feed"
GITHUB_BRANCH = "main"
CACHE_TTL = 3600  # 1 hour

# Default weights
DEFAULT_WEIGHTS = {
    "learning": 0.25,
    "engagement": 0.30,
    "breakthrough": 0.25,
    "mood": 0.20,
    "serendipity": 0.10
}

PRESETS = {
    "balanced": {"learning": 0.25, "engagement": 0.30, "breakthrough": 0.25, "mood": 0.20},
    "scholar": {"learning": 0.40, "engagement": 0.15, "breakthrough": 0.30, "mood": 0.15},
    "social": {"learning": 0.15, "engagement": 0.45, "breakthrough": 0.20, "mood": 0.20},
    "creative": {"learning": 0.20, "engagement": 0.20, "breakthrough": 0.40, "mood": 0.20},
    "uplifting": {"learning": 0.15, "engagement": 0.25, "breakthrough": 0.20, "mood": 0.40},
}


@st.cache_data(ttl=CACHE_TTL)
def fetch_from_github(path: str) -> dict:
    """Fetch JSON data from GitHub raw content."""
    url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{GITHUB_BRANCH}/{path}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        st.error(f"Failed to fetch {path}: {e}")
        return {}


def fetch_posts() -> list:
    """Fetch curated posts from repository."""
    data = fetch_from_github("data/posts.json")
    return data.get("posts", [])


def fetch_personas() -> dict:
    """Fetch personas from repository."""
    data = fetch_from_github("data/personas.json")
    return data.get("personas", {})


def calculate_score(post: dict, weights: dict) -> float:
    """Calculate combined neurochemical score for a post."""
    scores = post.get("scores", {})
    base = (
        scores.get("learning", 0) * weights["learning"] +
        scores.get("engagement", 0) * weights["engagement"] +
        scores.get("breakthrough", 0) * weights["breakthrough"] +
        scores.get("mood", 0) * weights["mood"]
    )
    serendipity = random.random() * weights.get("serendipity", 0.1)
    return base + serendipity


def filter_posts(posts: list, filters: dict) -> list:
    """Filter posts by tag, imprint, or persona."""
    filtered = posts

    if filters.get("tag"):
        filtered = [p for p in filtered if filters["tag"] in p.get("tags", [])]

    if filters.get("imprint"):
        filtered = [p for p in filtered if p.get("imprint") == filters["imprint"]]

    if filters.get("persona"):
        filtered = [p for p in filtered if p.get("persona_id") == filters["persona"]]

    return filtered


def render_post(post: dict, personas: dict):
    """Render a single post in the feed."""
    persona = personas.get(post.get("persona_id", ""), {})
    glyph = persona.get("glyph", "•")
    name = persona.get("name", post.get("persona_id", "Unknown"))
    handle = persona.get("handle", "")
    specialty = persona.get("specialty", "")

    scores = post.get("scores", {})

    # Post header
    st.markdown(f"### {glyph} {name} {handle}")
    if specialty:
        st.caption(specialty)

    # Content
    st.markdown(post.get("content", ""))

    # Hashtags
    hashtags = post.get("hashtags", [])
    if hashtags:
        st.markdown(" ".join([f"`#{tag}`" for tag in hashtags]))

    # Book references
    refs = post.get("book_references", [])
    for ref in refs:
        st.caption(f"📖 *{ref.get('title')}* by {ref.get('author')}")

    # Scores
    cols = st.columns(4)
    cols[0].metric("📊 Learn", f"{scores.get('learning', 0):.2f}")
    cols[1].metric("💬 Engage", f"{scores.get('engagement', 0):.2f}")
    cols[2].metric("⚡ Break", f"{scores.get('breakthrough', 0):.2f}")
    cols[3].metric("😊 Mood", f"{scores.get('mood', 0):.2f}")

    # Timestamp
    ts = post.get("timestamp", "")
    if ts:
        try:
            dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            st.caption(f"🕐 {dt.strftime('%Y-%m-%d %H:%M')}")
        except:
            st.caption(f"🕐 {ts}")

    st.divider()


def main():
    st.set_page_config(
        page_title="Agentic Social Feed",
        page_icon="📚",
        layout="wide"
    )

    st.title("📚 Agentic Social Feed")
    st.caption("AI-powered book content with neurochemical optimization")

    # Sidebar - Filters & Weights
    with st.sidebar:
        st.header("Feed Settings")

        # Preset selector
        preset = st.selectbox(
            "Preset",
            options=["balanced", "scholar", "social", "creative", "uplifting"],
            index=0
        )
        weights = PRESETS[preset].copy()
        weights["serendipity"] = 0.10

        st.subheader("Filters")

        # Fetch data for filter options
        posts = fetch_posts()
        personas = fetch_personas()

        # Get unique values for filters
        all_tags = set()
        all_imprints = set()
        for post in posts:
            all_tags.update(post.get("tags", []))
            if post.get("imprint"):
                all_imprints.add(post["imprint"])

        # Filter controls
        tag_filter = st.selectbox(
            "Topic Tag",
            options=["All"] + sorted(all_tags),
            index=0
        )

        imprint_filter = st.selectbox(
            "Imprint",
            options=["All"] + sorted(all_imprints),
            index=0
        )

        persona_filter = st.selectbox(
            "Persona",
            options=["All"] + sorted(personas.keys()),
            index=0
        )

        # Build filters dict
        filters = {}
        if tag_filter != "All":
            filters["tag"] = tag_filter
        if imprint_filter != "All":
            filters["imprint"] = imprint_filter
        if persona_filter != "All":
            filters["persona"] = persona_filter

        st.divider()
        st.caption(f"📡 Source: github.com/{GITHUB_REPO}")
        if st.button("🔄 Refresh"):
            st.cache_data.clear()
            st.rerun()

    # Main content
    if not posts:
        st.warning("No posts available. Check your connection.")
        return

    # Filter and sort posts
    filtered = filter_posts(posts, filters)

    # Calculate scores and sort
    for post in filtered:
        post["_combined_score"] = calculate_score(post, weights)

    sorted_posts = sorted(filtered, key=lambda p: p["_combined_score"], reverse=True)

    # Display stats
    col1, col2, col3 = st.columns(3)
    col1.metric("Posts", len(sorted_posts))
    col2.metric("Personas", len(set(p.get("persona_id") for p in sorted_posts)))
    col3.metric("Preset", preset.title())

    st.divider()

    # Render posts
    for post in sorted_posts:
        render_post(post, personas)

    # Footer
    st.caption("---")
    st.caption("Powered by [agentic-social-feed](https://github.com/fredzannarbor/agentic-social-feed)")


if __name__ == "__main__":
    main()
