"""Interval merging helper for closed integer ranges."""


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return sorted, merged closed intervals without mutating the input list."""
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
    merged: list[tuple[int, int]] = []

    for start, end in sorted_intervals:
        if start > end:
            raise ValueError("interval start must be less than or equal to end")

        if not merged:
            merged.append((start, end))
            continue

        previous_start, previous_end = merged[-1]
        if start <= previous_end + 1:
            merged[-1] = (previous_start, max(previous_end, end))
        else:
            merged.append((start, end))

    return merged
