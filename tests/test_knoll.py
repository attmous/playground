import pytest

from playground.knoll import dependency_depths


def test_dependency_depths_for_simple_chain() -> None:
    graph = {
        "app": ["library"],
        "library": ["foundation"],
        "foundation": [],
    }

    assert dependency_depths(graph) == {
        "app": 2,
        "library": 1,
        "foundation": 0,
    }


def test_dependency_depths_use_longest_branch() -> None:
    graph = {
        "app": ("short", "long"),
        "short": ["leaf"],
        "long": ["middle"],
        "middle": ["leaf"],
        "leaf": [],
    }

    assert dependency_depths(graph) == {
        "app": 3,
        "short": 1,
        "long": 2,
        "middle": 1,
        "leaf": 0,
    }


def test_dependency_depths_include_dependency_only_nodes() -> None:
    assert dependency_depths({"app": ["plugin"]}) == {
        "app": 1,
        "plugin": 0,
    }


def test_dependency_depths_raise_value_error_for_cycle() -> None:
    graph = {
        "app": ["library"],
        "library": ["app"],
    }

    with pytest.raises(ValueError):
        dependency_depths(graph)
