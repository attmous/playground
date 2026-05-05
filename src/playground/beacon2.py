def group_events(
    events: list[dict[str, object]], key: str
) -> dict[str, list[dict[str, object]]]:
    groups: dict[str, list[dict[str, object]]] = {}

    for event in events:
        value = event.get(key)
        group_key = "unknown" if value is None else str(value)
        groups.setdefault(group_key, []).append(dict(event))

    return {group_key: groups[group_key] for group_key in sorted(groups)}
