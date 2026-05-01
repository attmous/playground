def greeting(name: str = "Daedalus") -> str:
    """Return a predictable greeting for smoke tests."""
    clean_name = name.strip() or "Daedalus"
    return f"Hello, {clean_name}!"


def excited_greeting(name: str = "Daedalus") -> str:
    """Return an enthusiastic greeting for smoke tests."""
    clean_name = name.strip() or "Daedalus"
    return f"Hello, {clean_name}!!"
