def tide_token(name: str = "Sprints") -> str:
    """Return the Tide token for smoke tests."""
    clean_name = name.strip()
    return f"Tide: {clean_name or 'Sprints'}"
