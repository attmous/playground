def format_glyph_token(name: str | None = None) -> str:
    """Return the Glyph token for smoke tests."""
    clean_name = name.strip() if name is not None else ""
    return f"Glyph: {clean_name or 'Sprints'}"
