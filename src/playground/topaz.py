def sanitize_row(
    row: dict[str, object],
    required: list[str] | None = None,
) -> dict[str, str]:
    """Return a normalized string-only CSV row."""
    sanitized: dict[str, str] = {}

    for key, value in row.items():
        stripped_key = key.strip()
        if not stripped_key:
            continue

        if value is None:
            sanitized[stripped_key] = ""
        elif isinstance(value, str):
            sanitized[stripped_key] = value.strip()
        else:
            sanitized[stripped_key] = str(value)

    if required is not None:
        for key in required:
            stripped_key = key.strip()
            if stripped_key:
                sanitized.setdefault(stripped_key, "")

    return sanitized


__all__ = ["sanitize_row"]
