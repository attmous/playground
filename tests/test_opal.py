import pytest

from playground.opal import plan_retries


def test_plan_retries_returns_attempts_within_budget() -> None:
    assert plan_retries(10, [1, 2, 3, 5]) == {
        "attempts": 3,
        "used_seconds": 6,
        "remaining_seconds": 4,
        "schedule": [1, 3, 6],
    }


def test_plan_retries_includes_exact_deadline() -> None:
    assert plan_retries(6, [1, 2, 3]) == {
        "attempts": 3,
        "used_seconds": 6,
        "remaining_seconds": 0,
        "schedule": [1, 3, 6],
    }


def test_plan_retries_stops_before_over_budget_delay() -> None:
    assert plan_retries(5, [2, 4, 0]) == {
        "attempts": 1,
        "used_seconds": 2,
        "remaining_seconds": 3,
        "schedule": [2],
    }


def test_plan_retries_handles_zero_deadline() -> None:
    assert plan_retries(0, [0, 0, 1]) == {
        "attempts": 2,
        "used_seconds": 0,
        "remaining_seconds": 0,
        "schedule": [0, 0],
    }


def test_plan_retries_handles_empty_delays() -> None:
    assert plan_retries(8, []) == {
        "attempts": 0,
        "used_seconds": 0,
        "remaining_seconds": 8,
        "schedule": [],
    }


@pytest.mark.parametrize(
    ("deadline_seconds", "delays"),
    [
        (-1, [1]),
        (5, [-1]),
        (5, [1, 1.5]),
        (5, [True]),
        (False, [1]),
        (0, [1, -1]),
    ],
)
def test_plan_retries_validates_budget_inputs(
    deadline_seconds: int,
    delays: list[int],
) -> None:
    with pytest.raises(ValueError):
        plan_retries(deadline_seconds, delays)


def test_plan_retries_does_not_mutate_delays() -> None:
    delays = [2, 3, 4]
    original = list(delays)

    plan_retries(5, delays)

    assert delays == original
