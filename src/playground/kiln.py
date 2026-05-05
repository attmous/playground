def flatten_config(data: dict[str, object], sep: str = ".") -> dict[str, object]:
    """Flatten nested dictionaries into separator-joined leaf keys."""
    if not sep:
        raise ValueError("sep must be non-empty")

    flattened: dict[str, object] = {}

    def visit(prefix: str, value: object) -> None:
        if isinstance(value, dict):
            for key, nested_value in value.items():
                nested_key = str(key)
                next_key = f"{prefix}{sep}{nested_key}" if prefix else nested_key
                visit(next_key, nested_value)
            return

        flattened[prefix] = value

    for key, value in data.items():
        visit(key, value)

    return flattened
