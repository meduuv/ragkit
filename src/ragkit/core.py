"""Score-based retrieval over in-memory records."""


def top_k(items: list[dict], k: int, score_key: str = "score") -> list[dict]:
    """Return the highest-scoring records without mutating the input."""
    if k < 0:
        raise ValueError("k must be non-negative")
    return sorted(items, key=lambda item: item.get(score_key, 0), reverse=True)[:k]
