def juno_token(name: str = "Sprints") -> str:
    """Return the Juno token for smoke tests."""
    clean_name = name.strip()
    return f"Juno: {clean_name or 'Sprints'}"
