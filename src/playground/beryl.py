def compact_ranges(values: list[int]) -> list[str]:
    """Return sorted integers compacted into contiguous ranges."""
    compacted: list[str] = []
    unique_values = sorted(set(values))

    if not unique_values:
        return compacted

    start = previous = unique_values[0]

    for value in unique_values[1:]:
        if value == previous + 1:
            previous = value
            continue

        compacted.append(_format_range(start, previous))
        start = previous = value

    compacted.append(_format_range(start, previous))
    return compacted


def _format_range(start: int, end: int) -> str:
    if start == end:
        return str(start)
    return f"{start}-{end}"


__all__ = ["compact_ranges"]
