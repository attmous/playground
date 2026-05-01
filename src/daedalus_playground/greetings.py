def greeting(name: str = "Daedalus") -> str:
    """Return a predictable greeting for smoke tests."""
    clean_name = name.strip() or "Daedalus"
    return f"Hello, {clean_name}!"


def farewell(name: str = "Daedalus") -> str:
    """Return a predictable farewell for smoke tests."""
    clean_name = name.strip() or "Daedalus"
    return f"Goodbye, {clean_name}!"
