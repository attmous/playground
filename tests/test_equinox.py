import pytest

from playground.equinox import is_business_hour, window_label


@pytest.mark.parametrize(
    ("hour", "label"),
    [
        (0, "night"),
        (5, "night"),
        (6, "morning"),
        (11, "morning"),
        (12, "afternoon"),
        (16, "afternoon"),
        (17, "evening"),
        (20, "evening"),
        (21, "late"),
        (23, "late"),
    ],
)
def test_window_label_boundaries(hour: int, label: str) -> None:
    assert window_label(hour) == label


@pytest.mark.parametrize(
    ("hour", "expected"),
    [
        (8, False),
        (9, True),
        (16, True),
        (17, False),
    ],
)
def test_is_business_hour_boundaries(hour: int, expected: bool) -> None:
    assert is_business_hour(hour) is expected


@pytest.mark.parametrize("hour", [-1, 24])
def test_window_label_rejects_invalid_hours(hour: int) -> None:
    with pytest.raises(ValueError):
        window_label(hour)


@pytest.mark.parametrize("hour", [-1, 24])
def test_is_business_hour_rejects_invalid_hours(hour: int) -> None:
    with pytest.raises(ValueError):
        is_business_hour(hour)
