def quartz_token(name: str = "Sprints") -> str:
    """Return the Quartz token for smoke tests."""
    clean_name = name.strip()
    return f"Quartz: {clean_name or 'Sprints'}"
