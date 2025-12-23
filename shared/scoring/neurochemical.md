# Neurochemical Scoring Algorithm

Shared scoring logic for ranking posts across all platforms.

## Four-Factor Model

| Factor | Neurochemical | Score Range | Optimizes For |
|--------|---------------|-------------|---------------|
| Learning | Acetylcholine | 0.0 - 1.0 | Educational value, facts, knowledge |
| Engagement | Dopamine/Oxytocin | 0.0 - 1.0 | Social connection, relatability |
| Breakthrough | Norepinephrine | 0.0 - 1.0 | Aha moments, unexpected insights |
| Mood | Serotonin/Endorphins | 0.0 - 1.0 | Humor, inspiration, uplift |

## Scoring Formula

```
combined_score = (learning × learning_weight) +
                 (engagement × engagement_weight) +
                 (breakthrough × breakthrough_weight) +
                 (mood × mood_weight) +
                 (random × serendipity_factor)
```

### Default Weights

```json
{
  "learning_weight": 0.25,
  "engagement_weight": 0.30,
  "breakthrough_weight": 0.25,
  "mood_weight": 0.20,
  "serendipity_factor": 0.10
}
```

### Presets

| Preset | Learn | Engage | Break | Mood | Use Case |
|--------|-------|--------|-------|------|----------|
| balanced | 0.25 | 0.30 | 0.25 | 0.20 | General browsing |
| scholar | 0.40 | 0.15 | 0.30 | 0.15 | Deep learning focus |
| social | 0.15 | 0.45 | 0.20 | 0.20 | Community engagement |
| creative | 0.20 | 0.20 | 0.40 | 0.20 | Breakthrough seeking |
| uplifting | 0.15 | 0.25 | 0.20 | 0.40 | Mood boost |

## Implementation

### Swift (iOS)

```swift
struct NeurochemicalScores: Codable {
    let learning: Double
    let engagement: Double
    let breakthrough: Double
    let mood: Double

    func combined(weights: Weights, serendipity: Double = 0.1) -> Double {
        let base = (learning * weights.learning) +
                   (engagement * weights.engagement) +
                   (breakthrough * weights.breakthrough) +
                   (mood * weights.mood)
        let random = Double.random(in: 0...1) * serendipity
        return base + random
    }
}
```

### Python (Web)

```python
def calculate_combined_score(
    scores: dict,
    weights: dict,
    serendipity: float = 0.1
) -> float:
    base = (
        scores["learning"] * weights["learning"] +
        scores["engagement"] * weights["engagement"] +
        scores["breakthrough"] * weights["breakthrough"] +
        scores["mood"] * weights["mood"]
    )
    random_factor = random.random() * serendipity
    return base + random_factor
```

### JavaScript (if needed)

```javascript
function calculateCombinedScore(scores, weights, serendipity = 0.1) {
    const base =
        scores.learning * weights.learning +
        scores.engagement * weights.engagement +
        scores.breakthrough * weights.breakthrough +
        scores.mood * weights.mood;
    const random = Math.random() * serendipity;
    return base + random;
}
```

## Scoring Guidelines for Post Generation

When generating posts, score based on these criteria:

### Learning (0.0 - 1.0)
- 0.9+: Teaches specific, verifiable facts with sources
- 0.7-0.8: Provides educational context or background
- 0.5-0.6: Contains general knowledge
- 0.3-0.4: Light informational content
- <0.3: Entertainment-focused, minimal learning

### Engagement (0.0 - 1.0)
- 0.9+: Directly invites response, highly relatable
- 0.7-0.8: Strong emotional hook, conversation starter
- 0.5-0.6: Interesting but passive consumption
- 0.3-0.4: Niche appeal
- <0.3: Abstract or impersonal

### Breakthrough (0.0 - 1.0)
- 0.9+: Genuinely surprising connection across domains
- 0.7-0.8: Unexpected insight, reframes understanding
- 0.5-0.6: Interesting perspective shift
- 0.3-0.4: Mild novelty
- <0.3: Expected, conventional take

### Mood (0.0 - 1.0)
- 0.9+: Genuinely uplifting, inspiring, or funny
- 0.7-0.8: Warm, positive emotional tone
- 0.5-0.6: Neutral to pleasant
- 0.3-0.4: Serious but not heavy
- <0.3: Heavy, somber, or challenging content
