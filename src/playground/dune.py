def summarize_window(values: list[float], size: int) -> list[dict[str, float]]:
    """Return min, max, and average summaries for full sliding windows."""
    if not values:
        return []

    window_size = max(size, 1)
    summaries: list[dict[str, float]] = []

    for start in range(len(values) - window_size + 1):
        window = values[start : start + window_size]
        summaries.append(
            {
                "min": float(min(window)),
                "max": float(max(window)),
                "average": sum(window) / window_size,
            }
        )

    return summaries
