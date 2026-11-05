def add_points(score: int, pts: int) -> int:
    """Return the new score after adding pts points.

    Raises ValueError if pts is negative.
    """
    if pts < 0:
        raise ValueError("pts must be positive")
    return score + pts
