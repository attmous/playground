def matrix_token(name: str = "Sprints") -> str:
    """Return the Matrix token for smoke tests."""
    clean_name = name.strip()
    return f"Matrix: {clean_name or 'Sprints'}"
