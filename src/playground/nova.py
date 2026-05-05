def nova_token(name: str = "Sprints") -> str:
    clean_name = name.strip() or "Sprints"
    return f"Nova: {clean_name}"
