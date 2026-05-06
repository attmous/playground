def sample_logs(
    lines: list[str],
    *,
    every: int = 1,
    contains: str | None = None,
    limit: int | None = None,
) -> list[str]:
    """Return sampled log lines after optional substring filtering."""
    if every <= 0:
        raise ValueError("every must be positive")
    if limit is not None and limit < 0:
        raise ValueError("limit must be non-negative")

    matching_lines = lines
    if contains is not None:
        matching_lines = [line for line in lines if contains in line]

    sampled = [
        line
        for index, line in enumerate(matching_lines, start=1)
        if index % every == 0
    ]

    if limit is not None:
        return sampled[:limit]

    return sampled
