MINUTE_MIN = 0
MINUTE_MAX = 1439


def is_locked(minute_of_day: int, windows: list[tuple[int, int]]) -> bool:
    """Return whether the minute falls inside any inclusive lock window."""
    _validate_minute("minute_of_day", minute_of_day)

    for start, end in windows:
        _validate_minute("window start", start)
        _validate_minute("window end", end)

        if start <= end:
            if start <= minute_of_day <= end:
                return True
        elif minute_of_day >= start or minute_of_day <= end:
            return True

    return False


def _validate_minute(name: str, value: int) -> None:
    if value < MINUTE_MIN or value > MINUTE_MAX:
        raise ValueError(f"{name} must be between 0 and 1439 inclusive")
