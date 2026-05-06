from pathlib import PurePath


def group_by_extension(paths: list[str] | tuple[str, ...]) -> dict[str, list[str]]:
    """Group paths by lowercase extension without the leading dot."""
    grouped: dict[str, list[str]] = {}

    for path in paths:
        suffix = PurePath(path).suffix
        extension = suffix[1:].lower() if suffix else ""
        grouped.setdefault(extension, []).append(path)

    return grouped
