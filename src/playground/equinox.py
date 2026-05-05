def _validate_hour(hour: int) -> None:
    if hour < 0 or hour > 23:
        raise ValueError("hour must be between 0 and 23")


def window_label(hour: int) -> str:
    """Return the equinox time window label for an hour of day."""
    _validate_hour(hour)

    if hour <= 5:
        return "night"
    if hour <= 11:
        return "morning"
    if hour <= 16:
        return "afternoon"
    if hour <= 20:
        return "evening"
    return "late"


def is_business_hour(hour: int) -> bool:
    """Return whether the hour is within the equinox business window."""
    _validate_hour(hour)
    return 9 <= hour <= 16
