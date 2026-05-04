def glimmer_token(name: str = "Daedalus") -> str:
    """Return the Glimmer token for smoke tests."""
    clean_name = name.strip()
    return f"Glimmer: {clean_name or 'Daedalus'}"
