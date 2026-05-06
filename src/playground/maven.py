from fnmatch import fnmatchcase


def match_paths(
    paths: list[str],
    include: list[str],
    exclude: list[str] | None = None,
) -> list[str]:
    """Return paths matched by include patterns and not removed by exclude patterns."""
    if not include:
        return []

    exclude_patterns = exclude or []
    matched: list[str] = []

    for path in paths:
        if not any(fnmatchcase(path, pattern) for pattern in include):
            continue
        if any(fnmatchcase(path, pattern) for pattern in exclude_patterns):
            continue
        matched.append(path)

    return matched
