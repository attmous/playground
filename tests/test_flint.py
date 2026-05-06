import pytest

from playground.flint import sample_logs


def test_sample_logs_returns_all_lines_by_default() -> None:
    lines = ["debug boot", "info ready", "error failed"]

    assert sample_logs(lines) == ["debug boot", "info ready", "error failed"]


def test_sample_logs_filters_by_substring_before_sampling() -> None:
    lines = [
        "info startup",
        "error disk",
        "debug cache",
        "error network",
    ]

    assert sample_logs(lines, contains="error") == ["error disk", "error network"]


def test_sample_logs_keeps_every_nth_matching_line() -> None:
    lines = ["line 1", "line 2", "line 3", "line 4", "line 5"]

    assert sample_logs(lines, every=2) == ["line 2", "line 4"]


def test_sample_logs_applies_limit_last() -> None:
    lines = ["line 1", "line 2", "line 3", "line 4", "line 5"]

    assert sample_logs(lines, limit=3) == ["line 1", "line 2", "line 3"]


def test_sample_logs_combines_filter_sampling_and_limit_in_order() -> None:
    lines = [
        "info startup",
        "error disk",
        "error network",
        "debug cache",
        "error memory",
        "error cpu",
    ]

    assert sample_logs(lines, contains="error", every=2, limit=1) == [
        "error network"
    ]


def test_sample_logs_rejects_non_positive_every() -> None:
    with pytest.raises(ValueError):
        sample_logs(["line"], every=0)

    with pytest.raises(ValueError):
        sample_logs(["line"], every=-1)


def test_sample_logs_rejects_negative_limit() -> None:
    with pytest.raises(ValueError):
        sample_logs(["line"], limit=-1)


def test_sample_logs_accepts_zero_limit() -> None:
    assert sample_logs(["line 1", "line 2"], limit=0) == []


def test_sample_logs_does_not_mutate_input() -> None:
    lines = ["debug boot", "info ready", "error failed"]
    original = list(lines)

    sample_logs(lines, contains="o", every=2, limit=1)

    assert lines == original
