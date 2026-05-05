def summarize_diff(lines: list[str]) -> dict[str, int]:
    """Summarize unified diff lines by change class."""
    summary = {
        "added": 0,
        "removed": 0,
        "context": 0,
        "metadata": 0,
    }

    for line in lines:
        if line.startswith(("+++", "---", "@@")):
            summary["metadata"] += 1
        elif line.startswith("+"):
            summary["added"] += 1
        elif line.startswith("-"):
            summary["removed"] += 1
        elif line.startswith(" "):
            summary["context"] += 1
        else:
            summary["metadata"] += 1

    return summary


__all__ = ["summarize_diff"]
