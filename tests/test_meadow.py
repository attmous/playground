import pytest

from playground.meadow import rolling_average


def test_rolling_average_window_one_returns_float_values() -> None:
    result = rolling_average([2.0, 4.0, 6.0], 1)

    assert result == [2.0, 4.0, 6.0]
    assert all(isinstance(value, float) for value in result)


def test_rolling_average_uses_larger_window() -> None:
    assert rolling_average([2.0, 4.0, 6.0, 10.0], 3) == [2.0, 3.0, 4.0, 20.0 / 3.0]


def test_rolling_average_handles_window_larger_than_data() -> None:
    assert rolling_average([1.0, 3.0, 8.0], 5) == [1.0, 2.0, 4.0]


def test_rolling_average_rejects_invalid_window() -> None:
    with pytest.raises(ValueError):
        rolling_average([1.0], 0)


def test_rolling_average_handles_empty_list() -> None:
    assert rolling_average([], 3) == []


def test_rolling_average_does_not_mutate_input() -> None:
    values = [3.0, 6.0, 9.0]
    original = values.copy()

    rolling_average(values, 2)

    assert values == original
