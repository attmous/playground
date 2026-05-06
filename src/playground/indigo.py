def free_slots(
    busy: list[tuple[int, int]],
    start: int,
    end: int,
    min_duration: int,
) -> list[tuple[int, int]]:
    """Return free half-open intervals inside a search window."""
    if start > end:
        raise ValueError("start must be less than or equal to end")
    if min_duration <= 0:
        raise ValueError("min_duration must be positive")

    clipped_busy = sorted(
        (max(busy_start, start), min(busy_end, end))
        for busy_start, busy_end in busy
        if max(busy_start, start) < min(busy_end, end)
    )

    merged_busy: list[tuple[int, int]] = []
    for busy_start, busy_end in clipped_busy:
        if not merged_busy or busy_start > merged_busy[-1][1]:
            merged_busy.append((busy_start, busy_end))
            continue

        merged_start, merged_end = merged_busy[-1]
        merged_busy[-1] = (merged_start, max(merged_end, busy_end))

    slots: list[tuple[int, int]] = []
    cursor = start
    for busy_start, busy_end in merged_busy:
        if busy_start - cursor >= min_duration:
            slots.append((cursor, busy_start))
        cursor = max(cursor, busy_end)

    if end - cursor >= min_duration:
        slots.append((cursor, end))

    return slots
