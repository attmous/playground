from copy import deepcopy


def resolve_options(
    defaults: dict[str, object], overrides: dict[str, object | None]
) -> dict[str, object]:
    """Resolve options by recursively applying overrides to defaults."""
    resolved = deepcopy(defaults)
    _apply_overrides(resolved, overrides)
    return resolved


def _apply_overrides(
    target: dict[str, object], overrides: dict[str, object | None]
) -> None:
    for key, value in overrides.items():
        if value is None:
            target.pop(key, None)
            continue

        existing = target.get(key)
        if isinstance(existing, dict) and isinstance(value, dict):
            _apply_overrides(existing, value)
            continue

        target[key] = deepcopy(value)
