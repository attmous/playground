def glimmer_token(name: str = "Sprints") -> str:
    """Return the Glimmer token for smoke tests."""
    clean_name = name.strip()
    return f"Glimmer: {clean_name or 'Sprints'}"
