from playground.dune import summarize_window


def test_summarize_window_returns_empty_for_empty_values() -> None:
    assert summarize_window([], 3) == []


def test_summarize_window_clamps_size_to_one() -> None:
    assert summarize_window([2.0, 4.0, 8.0], 0) == [
        {"min": 2.0, "max": 2.0, "average": 2.0},
        {"min": 4.0, "max": 4.0, "average": 4.0},
        {"min": 8.0, "max": 8.0, "average": 8.0},
    ]


def test_summarize_window_exact_size_window() -> None:
    assert summarize_window([1.0, 3.0, 5.0], 3) == [
        {"min": 1.0, "max": 5.0, "average": 3.0}
    ]


def test_summarize_window_multiple_sliding_windows() -> None:
    assert summarize_window([1.0, 4.0, 2.0, 8.0], 2) == [
        {"min": 1.0, "max": 4.0, "average": 2.5},
        {"min": 2.0, "max": 4.0, "average": 3.0},
        {"min": 2.0, "max": 8.0, "average": 5.0},
    ]
