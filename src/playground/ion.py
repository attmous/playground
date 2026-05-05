def ion_token(name: str = "Sprints") -> str:
    """Return the Ion token for smoke tests."""
    clean_name = name.strip()
    return f"Ion: {clean_name or 'Sprints'}"
