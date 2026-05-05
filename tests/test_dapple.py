from copy import deepcopy

from playground.dapple import summarize_rows


def test_summarize_rows_empty_rows() -> None:
    assert summarize_rows([], "name") == {
        "count": 0,
        "missing": 0,
        "unique": 0,
        "first": None,
        "last": None,
    }


def test_summarize_rows_counts_absent_and_none_as_missing() -> None:
    rows = [{"status": "ready"}, {}, {"status": None}, {"status": "done"}]

    summary = summarize_rows(rows, "status")

    assert summary["count"] == 4
    assert summary["missing"] == 2


def test_summarize_rows_counts_unique_non_missing_values_by_equality() -> None:
    rows = [
        {"tags": ["alpha", "beta"]},
        {"tags": ["alpha", "beta"]},
        {"tags": ["beta"]},
    ]

    summary = summarize_rows(rows, "tags")

    assert summary["unique"] == 2


def test_summarize_rows_tracks_first_and_last_non_missing_values() -> None:
    rows = [
        {},
        {"score": None},
        {"score": 10},
        {"score": 20},
        {"score": 10},
    ]

    summary = summarize_rows(rows, "score")

    assert summary["first"] == 10
    assert summary["last"] == 10


def test_summarize_rows_does_not_mutate_input_rows() -> None:
    rows = [{"value": ["same"]}, {"value": None}, {}]
    original = deepcopy(rows)

    summarize_rows(rows, "value")

    assert rows == original
