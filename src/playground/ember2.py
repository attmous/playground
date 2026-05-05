from decimal import Decimal, ROUND_FLOOR


def histogram(values: list[float], bucket_size: float) -> dict[str, int]:
    """Build a histogram with buckets sorted by numeric start."""
    bucket = Decimal(str(bucket_size))
    if bucket <= 0:
        raise ValueError("bucket_size must be positive")

    counts: dict[Decimal, int] = {}
    for value in values:
        decimal_value = Decimal(str(value))
        start = (decimal_value / bucket).to_integral_value(
            rounding=ROUND_FLOOR
        ) * bucket
        counts[start] = counts.get(start, 0) + 1

    return {
        _label(start, start + bucket): counts[start]
        for start in sorted(counts)
    }


def _label(start: Decimal, end: Decimal) -> str:
    return f"{_format_bound(start)}-{_format_bound(end)}"


def _format_bound(value: Decimal) -> str:
    if value == value.to_integral_value():
        return str(value.quantize(Decimal("1")))

    return format(value.normalize(), "f")


__all__ = ["histogram"]
