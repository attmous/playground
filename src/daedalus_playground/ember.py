def ember_token(name: str = "Daedalus") -> str:
    clean_name = name.strip() or "Daedalus"
    return f"Ember: {clean_name}"
