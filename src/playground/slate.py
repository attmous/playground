from copy import deepcopy


def resolve_overlay(
    base: dict[str, object],
    override: dict[str, object],
) -> dict[str, object]:
    """Return base overlaid with override without mutating either input."""
    resolved = deepcopy(base)

    for key, value in override.items():
        if value is None:
            resolved.pop(key, None)
            continue

        current = resolved.get(key)
        if isinstance(current, dict) and isinstance(value, dict):
            resolved[key] = resolve_overlay(current, value)
            continue

        resolved[key] = deepcopy(value)

    return resolved
