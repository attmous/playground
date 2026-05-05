def prism_token(name: str = "Sprints") -> str:
    """Return the Prism token for smoke tests."""
    clean_name = name.strip()
    return f"Prism: {clean_name or 'Sprints'}"
