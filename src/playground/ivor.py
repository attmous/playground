import re


def normalize_ivor_key(value: str | None = None) -> str:
    """Return a normalized Ivor key for smoke tests."""
    if value is None:
        clean_value = "sprints"
    else:
        clean_value = value.strip()

    if not clean_value:
        clean_value = "sprints"

    return re.sub(r"\s+", "-", clean_value.lower()).strip("-")
