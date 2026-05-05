import copy

from playground.timber import walk_tree


def test_walk_tree_returns_nested_leaf_paths() -> None:
    tree: dict[str, object] = {
        "forest": {
            "oak": {"height": 12, "rings": 80},
            "pine": {"needles": True},
        },
        "clearing": "sunny",
    }

    assert walk_tree(tree) == [
        "clearing",
        "forest.oak.height",
        "forest.oak.rings",
        "forest.pine.needles",
    ]


def test_walk_tree_uses_depth_first_alphabetical_key_order() -> None:
    tree: dict[str, object] = {
        "b": {"d": 1, "c": 2},
        "a": {"z": 3, "m": {"n": 4}},
    }

    assert walk_tree(tree) == ["a.m.n", "a.z", "b.c", "b.d"]


def test_walk_tree_returns_empty_list_for_empty_root() -> None:
    assert walk_tree({}) == []


def test_walk_tree_includes_empty_child_dictionaries_as_leaves() -> None:
    tree: dict[str, object] = {
        "branch": {
            "empty": {},
            "nested": {"empty": {}},
        },
        "root_empty": {},
    }

    assert walk_tree(tree) == [
        "branch.empty",
        "branch.nested.empty",
        "root_empty",
    ]


def test_walk_tree_includes_scalar_leaves() -> None:
    tree: dict[str, object] = {
        "count": 3,
        "enabled": False,
        "name": "timber",
        "none": None,
    }

    assert walk_tree(tree) == ["count", "enabled", "name", "none"]


def test_walk_tree_does_not_mutate_input() -> None:
    tree: dict[str, object] = {
        "z": {"b": [1, 2], "a": {"leaf": True}},
        "a": {},
    }
    original = copy.deepcopy(tree)

    walk_tree(tree)

    assert tree == original
