def plan_retries(deadline_seconds: int, delays: list[int]) -> dict[str, object]:
    """Return the retry attempts that fit within a delay budget."""
    if type(deadline_seconds) is not int or deadline_seconds < 0:
        raise ValueError("deadline_seconds must be a non-negative integer")

    for delay in delays:
        if type(delay) is not int or delay < 0:
            raise ValueError("delays must contain non-negative integers")

    schedule: list[int] = []
    cumulative_delay = 0

    for delay in delays:
        next_delay = cumulative_delay + delay
        if next_delay > deadline_seconds:
            break

        cumulative_delay = next_delay
        schedule.append(cumulative_delay)

    return {
        "attempts": len(schedule),
        "used_seconds": cumulative_delay,
        "remaining_seconds": deadline_seconds - cumulative_delay,
        "schedule": schedule,
    }
