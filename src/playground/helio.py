from string import hexdigits


def parse_hex_color(value: str) -> tuple[int, int, int]:
    """Parse a short or long hex color into RGB components."""
    color = value.strip()
    if color.startswith("#"):
        color = color[1:]

    if len(color) not in (3, 6):
        raise ValueError("hex color must contain 3 or 6 hex digits")

    if any(character not in hexdigits for character in color):
        raise ValueError("hex color contains non-hex characters")

    if len(color) == 3:
        color = "".join(character * 2 for character in color)

    return (
        int(color[0:2], 16),
        int(color[2:4], 16),
        int(color[4:6], 16),
    )
