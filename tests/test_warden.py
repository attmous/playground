import pytest

from playground.warden import is_locked


def test_is_locked_matches_normal_window_inclusively() -> None:
    windows = [(60, 120)]

    assert is_locked(60, windows) is True
    assert is_locked(90, windows) is True
    assert is_locked(120, windows) is True
    assert is_locked(59, windows) is False
    assert is_locked(121, windows) is False


def test_is_locked_matches_any_normal_window() -> None:
    windows = [(90, 120), (300, 330)]

    assert is_locked(105, windows) is True
    assert is_locked(315, windows) is True
    assert is_locked(200, windows) is False


def test_is_locked_matches_wrapped_window_across_midnight() -> None:
    windows = [(1320, 60)]

    assert is_locked(1320, windows) is True
    assert is_locked(1439, windows) is True
    assert is_locked(0, windows) is True
    assert is_locked(60, windows) is True
    assert is_locked(720, windows) is False


def test_is_locked_accepts_boundary_minutes() -> None:
    assert is_locked(0, [(0, 0)]) is True
    assert is_locked(1439, [(1439, 1439)]) is True
    assert is_locked(0, [(1, 1439)]) is False
    assert is_locked(1439, [(0, 1438)]) is False


def test_is_locked_returns_false_for_empty_windows() -> None:
    assert is_locked(720, []) is False


@pytest.mark.parametrize("minute_of_day", [-1, 1440])
def test_is_locked_rejects_invalid_minute(minute_of_day: int) -> None:
    with pytest.raises(ValueError, match="minute_of_day"):
        is_locked(minute_of_day, [(0, 1)])


@pytest.mark.parametrize(
    "windows",
    [
        [(-1, 60)],
        [(60, -1)],
        [(1440, 60)],
        [(60, 1440)],
    ],
)
def test_is_locked_rejects_invalid_windows(
    windows: list[tuple[int, int]]
) -> None:
    with pytest.raises(ValueError, match="window"):
        is_locked(30, windows)
