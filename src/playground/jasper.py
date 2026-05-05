def weighted_checksum(value: str) -> int:
    """Return a weighted ordinal checksum modulo 97."""
    total = sum(
        position * ord(character)
        for position, character in enumerate(value, 1)
    )
    return total % 97


def append_checksum(value: str) -> str:
    """Append the two-digit weighted checksum to a value."""
    return f"{value}-{weighted_checksum(value):02d}"
