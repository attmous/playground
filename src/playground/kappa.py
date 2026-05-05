def kappa_token(name: str = "Sprints") -> str:
    """Return the Kappa token for smoke tests."""
    clean_name = name.strip()
    return f"Kappa: {clean_name or 'Sprints'}"
