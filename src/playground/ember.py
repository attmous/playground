def ember_token(name: str = "Sprints") -> str:
    clean_name = name.strip() or "Sprints"
    return f"Ember: {clean_name}"
