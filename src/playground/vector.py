def vector_token(name: str = "Sprints") -> str:
    """Return the Vector token for smoke tests."""
    clean_name = name.strip()
    return f"Vector: {clean_name or 'Sprints'}"
