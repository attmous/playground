UNITS = {
    "B": 1,
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3,
}


def convert_bytes(value: int, unit: str = "auto") -> dict[str, object]:
    """Convert a byte count to the requested base-1024 unit."""
    if value < 0:
        raise ValueError("value must be non-negative")

    normalized_unit = unit.upper()
    if normalized_unit == "AUTO":
        normalized_unit = _auto_unit(value)

    if normalized_unit not in UNITS:
        raise ValueError(f"unsupported unit: {unit}")

    converted = value / UNITS[normalized_unit]
    return {
        "value": converted,
        "unit": normalized_unit,
        "text": f"{converted:.2f} {normalized_unit}",
    }


def _auto_unit(value: int) -> str:
    for unit in ("GB", "MB", "KB"):
        if value / UNITS[unit] >= 1:
            return unit
    return "B"
