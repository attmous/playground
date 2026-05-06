def allowed_actions(roles: list[str], grants: dict[str, list[str]]) -> list[str]:
    """Return sorted unique actions granted to the provided roles."""
    actions: set[str] = set()

    for role in roles:
        actions.update(grants.get(role, []))

    return sorted(actions)
