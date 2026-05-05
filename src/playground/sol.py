def sol_token(name: str = "Sprints") -> str:
    """Return the Sol token for smoke tests."""
    clean_name = name.strip()
    return f"Sol: {clean_name or 'Sprints'}"
