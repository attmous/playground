def ion_token(name: str = "Daedalus") -> str:
    """Return the Ion token for smoke tests."""
    clean_name = name.strip()
    return f"Ion: {clean_name or 'Daedalus'}"
