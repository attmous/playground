def comet_token(name: str = "Daedalus") -> str:
    """Return a predictable comet token for smoke tests."""
    clean_name = name.strip()
    return f"Comet: {clean_name or 'Daedalus'}"
