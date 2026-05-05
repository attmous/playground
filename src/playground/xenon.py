def xenon_token(name: str = "Sprints") -> str:
    """Return the Xenon token for smoke tests."""
    clean_name = name.strip()
    return f"Xenon: {clean_name or 'Sprints'}"
