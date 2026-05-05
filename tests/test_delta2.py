import copy

import pytest

from playground.delta2 import chunk_by_weight


def test_chunk_by_weight_groups_items_without_exceeding_max_weight() -> None:
    items = [
        {"id": "a", "weight": 2},
        {"id": "b", "weight": 3},
        {"id": "c", "weight": 1},
        {"id": "d", "weight": 4},
    ]

    assert chunk_by_weight(items, 5) == [
        [{"id": "a", "weight": 2}, {"id": "b", "weight": 3}],
        [{"id": "c", "weight": 1}, {"id": "d", "weight": 4}],
    ]


def test_chunk_by_weight_defaults_missing_weight_to_one() -> None:
    items = [
        {"id": "a"},
        {"id": "b", "weight": 2},
        {"id": "c"},
    ]

    assert chunk_by_weight(items, 3) == [
        [{"id": "a"}, {"id": "b", "weight": 2}],
        [{"id": "c"}],
    ]


def test_chunk_by_weight_keeps_exact_boundaries_in_same_chunk() -> None:
    items = [
        {"id": "a", "weight": 2},
        {"id": "b", "weight": 2},
        {"id": "c", "weight": 4},
    ]

    assert chunk_by_weight(items, 4) == [
        [{"id": "a", "weight": 2}, {"id": "b", "weight": 2}],
        [{"id": "c", "weight": 4}],
    ]


def test_chunk_by_weight_places_overweight_item_in_own_chunk() -> None:
    items = [
        {"id": "a", "weight": 2},
        {"id": "b", "weight": 7},
        {"id": "c", "weight": 1},
        {"id": "d", "weight": 3},
    ]

    assert chunk_by_weight(items, 4) == [
        [{"id": "a", "weight": 2}],
        [{"id": "b", "weight": 7}],
        [{"id": "c", "weight": 1}, {"id": "d", "weight": 3}],
    ]


@pytest.mark.parametrize("max_weight", [0, -1, 1.5, True])
def test_chunk_by_weight_rejects_invalid_max_weight(max_weight: object) -> None:
    with pytest.raises(ValueError, match="max_weight"):
        chunk_by_weight([{"id": "a"}], max_weight)  # type: ignore[arg-type]


@pytest.mark.parametrize("weight", [0, -1, 1.5, "2", False])
def test_chunk_by_weight_rejects_invalid_item_weight(weight: object) -> None:
    with pytest.raises(ValueError, match="weight"):
        chunk_by_weight([{"id": "a", "weight": weight}], 5)


def test_chunk_by_weight_does_not_mutate_input() -> None:
    items = [
        {"id": "a", "weight": 2, "tags": ["ready"]},
        {"id": "b"},
        {"id": "c", "weight": 3},
    ]
    original = copy.deepcopy(items)

    chunk_by_weight(items, 3)

    assert items == original
