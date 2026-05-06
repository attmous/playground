import pytest

from playground.indigo import free_slots


def test_free_slots_returns_gaps_between_busy_intervals() -> None:
    assert free_slots([(10, 20), (30, 40)], 0, 50, 5) == [
        (0, 10),
        (20, 30),
        (40, 50),
    ]


def test_free_slots_merges_unsorted_overlapping_busy_intervals() -> None:
    assert free_slots([(25, 30), (10, 20), (18, 26)], 0, 40, 1) == [
        (0, 10),
        (30, 40),
    ]


def test_free_slots_clips_busy_intervals_to_search_window() -> None:
    assert free_slots([(0, 12), (18, 30)], 10, 20, 1) == [(12, 18)]


def test_free_slots_returns_empty_when_busy_covers_window() -> None:
    assert free_slots([(0, 20)], 5, 15, 1) == []


def test_free_slots_filters_gaps_shorter_than_min_duration() -> None:
    assert free_slots([(5, 7), (10, 20), (24, 25)], 0, 30, 5) == [
        (0, 5),
        (25, 30),
    ]


@pytest.mark.parametrize(
    ("start", "end", "min_duration"),
    [
        (10, 5, 1),
        (0, 10, 0),
        (0, 10, -1),
    ],
)
def test_free_slots_validates_search_window_and_min_duration(
    start: int,
    end: int,
    min_duration: int,
) -> None:
    with pytest.raises(ValueError):
        free_slots([], start, end, min_duration)


def test_free_slots_does_not_mutate_busy_intervals() -> None:
    busy = [(20, 25), (5, 10), (8, 12)]
    original = list(busy)

    free_slots(busy, 0, 30, 1)

    assert busy == original
