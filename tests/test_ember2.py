import pytest

from playground.ember2 import histogram


def test_histogram_groups_positive_values_by_bucket() -> None:
    assert histogram([0.2, 0.7, 1.0, 1.9, 2.1], 1.0) == {
        "0-1": 2,
        "1-2": 2,
        "2-3": 1,
    }


def test_histogram_supports_negative_values() -> None:
    assert histogram([-2.1, -2.0, -1.2, -0.1, 0.0], 1.0) == {
        "-3--2": 1,
        "-2--1": 2,
        "-1-0": 1,
        "0-1": 1,
    }


def test_histogram_supports_fractional_bucket_size() -> None:
    assert histogram([0.1, 0.4, 0.5, 0.9, 1.0], 0.5) == {
        "0-0.5": 2,
        "0.5-1": 2,
        "1-1.5": 1,
    }


def test_histogram_returns_empty_dict_for_empty_input() -> None:
    assert histogram([], 1.0) == {}


@pytest.mark.parametrize("bucket_size", [0.0, -1.0])
def test_histogram_rejects_invalid_bucket_size(bucket_size: float) -> None:
    with pytest.raises(ValueError, match="bucket_size must be positive"):
        histogram([1.0], bucket_size)


def test_histogram_formats_integral_bounds_without_trailing_decimal() -> None:
    assert histogram([2.0, 2.5, 3.0], 0.5) == {
        "2-2.5": 1,
        "2.5-3": 1,
        "3-3.5": 1,
    }
