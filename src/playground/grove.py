import re
import unicodedata


_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def make_slug(value: str, max_length: int = 48) -> str:
    """Build a lowercase ASCII slug from a text value."""
    if max_length <= 0:
        raise ValueError("max_length must be positive")

    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    slug = _NON_ALNUM.sub("-", ascii_value).strip("-")

    if slug == "":
        return "item"

    return slug[:max_length].rstrip("-") or "item"
