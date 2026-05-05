def beacon_token(name: str = "Sprints") -> str:
    clean_name = name.strip() or "Sprints"
    return f"Beacon: {clean_name}"
