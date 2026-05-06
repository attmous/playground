from playground.beryl import compact_ranges


def test_compact_ranges_returns_empty_list_for_empty_input() -> None:
    assert compact_ranges([]) == []


def test_compact_ranges_removes_duplicates() -> None:
    assert compact_ranges([2, 2, 3, 3, 5]) == ["2-3", "5"]


def test_compact_ranges_sorts_unsorted_input() -> None:
    assert compact_ranges([9, 1, 3, 2, 8]) == ["1-3", "8-9"]


def test_compact_ranges_keeps_singletons_as_plain_strings() -> None:
    assert compact_ranges([1, 3, 5]) == ["1", "3", "5"]


def test_compact_ranges_collapses_contiguous_runs() -> None:
    assert compact_ranges([1, 2, 3, 7, 8, 10]) == ["1-3", "7-8", "10"]
