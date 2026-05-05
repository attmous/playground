import pytest

from playground.iris import merge_intervals


def test_merge_intervals_returns_empty_list_for_empty_input() -> None:
    assert merge_intervals([]) == []


def test_merge_intervals_preserves_sorted_separated_intervals() -> None:
    assert merge_intervals([(1, 2), (5, 7), (10, 10)]) == [(1, 2), (5, 7), (10, 10)]


def test_merge_intervals_sorts_unsorted_input_before_merging() -> None:
    assert merge_intervals([(8, 9), (1, 3), (5, 6)]) == [(1, 3), (5, 6), (8, 9)]


def test_merge_intervals_merges_overlapping_closed_intervals() -> None:
    assert merge_intervals([(1, 4), (2, 6), (6, 8)]) == [(1, 8)]


def test_merge_intervals_merges_directly_adjacent_intervals() -> None:
    assert merge_intervals([(1, 2), (3, 5), (7, 7), (6, 6)]) == [(1, 7)]


def test_merge_intervals_rejects_invalid_intervals() -> None:
    with pytest.raises(ValueError):
        merge_intervals([(1, 3), (5, 4)])


def test_merge_intervals_does_not_mutate_input_list() -> None:
    intervals = [(5, 7), (1, 2), (3, 4)]
    original = list(intervals)

    assert merge_intervals(intervals) == [(1, 7)]
    assert intervals == original
