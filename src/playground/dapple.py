"""Small row summarization helper for table-like dictionaries."""


def summarize_rows(rows: list[dict[str, object]], key: str) -> dict[str, object]:
    """Summarize non-missing values for one key across row dictionaries."""
    missing = 0
    unique_values: list[object] = []
    first: object | None = None
    last: object | None = None

    for row in rows:
        value = row.get(key)
        if value is None:
            missing += 1
            continue

        if first is None:
            first = value
        last = value

        if not any(value == existing for existing in unique_values):
            unique_values.append(value)

    return {
        "count": len(rows),
        "missing": missing,
        "unique": len(unique_values),
        "first": first,
        "last": last,
    }
