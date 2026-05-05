def aurora_token(name: str = "Sprints") -> str:
    """Return the Aurora token for smoke tests."""
    clean_name = name.strip()
    return f"Aurora: {clean_name or 'Sprints'}"
