def fable_token(name: str = "Sprints") -> str:
    """Return the Fable token for smoke tests."""
    clean_name = name.strip()
    return f"Fable: {clean_name or 'Sprints'}"
