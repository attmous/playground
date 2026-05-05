def umbra_token(name: str = "Sprints") -> str:
    """Return the Umbra token for smoke tests."""
    clean_name = name.strip()
    return f"Umbra: {clean_name or 'Sprints'}"
