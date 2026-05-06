from numbers import Real


UNKNOWN_GROUP = "unknown"


def _is_metric_value(value: object) -> bool:
    return isinstance(value, Real) and not isinstance(value, bool)


def rollup_metrics(
    rows: list[dict[str, object]], group_key: str, value_key: str
) -> dict[str, dict[str, float]]:
    """Roll up numeric row values by group."""
    groups: dict[str, list[float]] = {}

    for row in rows:
        value = row.get(value_key)
        if not _is_metric_value(value):
            continue

        raw_group = row.get(group_key)
        group = UNKNOWN_GROUP if raw_group is None else str(raw_group)
        groups.setdefault(group, []).append(float(value))

    return {
        group: {
            "count": float(len(values)),
            "total": sum(values),
            "average": sum(values) / len(values),
            "min": min(values),
            "max": max(values),
        }
        for group, values in sorted(groups.items())
    }
