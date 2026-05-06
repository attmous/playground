from playground.umber import find_cycle


def test_find_cycle_returns_empty_list_for_acyclic_graph() -> None:
    graph = {
        "build": ["lint", "test"],
        "lint": ["format"],
        "test": ["package"],
    }

    assert find_cycle(graph) == []


def test_find_cycle_reports_simple_cycle() -> None:
    graph = {
        "api": ["service"],
        "service": ["database"],
        "database": ["api"],
    }

    assert find_cycle(graph) == ["api", "service", "database", "api"]


def test_find_cycle_includes_dependency_only_nodes() -> None:
    graph = {
        "root": ["leaf"],
    }

    assert find_cycle(graph) == []


def test_find_cycle_selects_cycle_deterministically() -> None:
    graph = {
        "zeta": ["zeta"],
        "alpha": ["beta", "gamma"],
        "gamma": ["alpha"],
        "beta": ["delta"],
        "delta": ["beta"],
    }

    assert find_cycle(graph) == ["beta", "delta", "beta"]
