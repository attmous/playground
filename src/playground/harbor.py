def harbor_token(name: str = "Sprints") -> str:
    """Return the Harbor token for smoke tests."""
    clean_name = name.strip()
    return f"Harbor: {clean_name or 'Sprints'}"
