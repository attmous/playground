from copy import deepcopy

from playground.kelp import rollup_metrics


def test_rollup_metrics_groups_values_by_string_key() -> None:
    rows = [
        {"area": "reef", "height": 2},
        {"area": "reef", "height": 4},
        {"area": 12, "height": 3},
    ]

    assert rollup_metrics(rows, "area", "height") == {
        "12": {
            "count": 1.0,
            "total": 3.0,
            "average": 3.0,
            "min": 3.0,
            "max": 3.0,
        },
        "reef": {
            "count": 2.0,
            "total": 6.0,
            "average": 3.0,
            "min": 2.0,
            "max": 4.0,
        },
    }


def test_rollup_metrics_uses_unknown_for_missing_or_none_group() -> None:
    rows = [
        {"height": 2},
        {"area": None, "height": 4},
    ]

    assert rollup_metrics(rows, "area", "height") == {
        "unknown": {
            "count": 2.0,
            "total": 6.0,
            "average": 3.0,
            "min": 2.0,
            "max": 4.0,
        }
    }


def test_rollup_metrics_ignores_missing_none_and_non_numeric_values() -> None:
    rows = [
        {"area": "reef", "height": 2},
        {"area": "reef"},
        {"area": "reef", "height": None},
        {"area": "reef", "height": "3"},
        {"area": "reef", "height": True},
    ]

    assert rollup_metrics(rows, "area", "height") == {
        "reef": {
            "count": 1.0,
            "total": 2.0,
            "average": 2.0,
            "min": 2.0,
            "max": 2.0,
        }
    }


def test_rollup_metrics_accepts_numeric_ints_and_floats() -> None:
    rows = [
        {"area": "reef", "height": 1},
        {"area": "reef", "height": 2.5},
    ]

    assert rollup_metrics(rows, "area", "height") == {
        "reef": {
            "count": 2.0,
            "total": 3.5,
            "average": 1.75,
            "min": 1.0,
            "max": 2.5,
        }
    }


def test_rollup_metrics_returns_groups_sorted_alphabetically() -> None:
    rows = [
        {"area": "zeta", "height": 1},
        {"area": "alpha", "height": 1},
        {"area": "middle", "height": 1},
    ]

    assert list(rollup_metrics(rows, "area", "height")) == [
        "alpha",
        "middle",
        "zeta",
    ]


def test_rollup_metrics_returns_empty_dict_for_empty_input() -> None:
    assert rollup_metrics([], "area", "height") == {}


def test_rollup_metrics_does_not_mutate_rows() -> None:
    rows = [
        {"area": "reef", "height": 2, "meta": {"source": "sensor"}},
        {"area": None, "height": 4},
        {"area": "reef", "height": "ignored"},
    ]
    original = deepcopy(rows)

    rollup_metrics(rows, "area", "height")

    assert rows == original
