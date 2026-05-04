def drift_token(name: str = "Daedalus") -> str:
    clean_name = name.strip() or "Daedalus"
    return f"Drift: {clean_name}"
