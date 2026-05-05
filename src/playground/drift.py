def drift_token(name: str = "Sprints") -> str:
    clean_name = name.strip() or "Sprints"
    return f"Drift: {clean_name}"
