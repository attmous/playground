import copy

import pytest

from playground.kiln import flatten_config


def test_flatten_config_flattens_nested_data() -> None:
    data: dict[str, object] = {
        "service": {
            "host": "localhost",
            "database": {
                "port": 5432,
                "ssl": True,
            },
        },
        "debug": False,
    }

    assert flatten_config(data) == {
        "service.host": "localhost",
        "service.database.port": 5432,
        "service.database.ssl": True,
        "debug": False,
    }


def test_flatten_config_preserves_lists_without_traversing() -> None:
    data: dict[str, object] = {
        "service": {
            "ports": [80, 443],
            "routes": [{"path": "/health"}],
        },
    }

    result = flatten_config(data)

    assert result == {
        "service.ports": [80, 443],
        "service.routes": [{"path": "/health"}],
    }
    service = data["service"]
    assert isinstance(service, dict)
    assert result["service.ports"] is service["ports"]


def test_flatten_config_omits_empty_dictionaries() -> None:
    data: dict[str, object] = {
        "service": {
            "empty": {},
            "nested": {"empty": {}},
            "host": "localhost",
        },
        "root_empty": {},
    }

    assert flatten_config(data) == {"service.host": "localhost"}


def test_flatten_config_accepts_custom_separator() -> None:
    data: dict[str, object] = {"service": {"database": {"port": 5432}}}

    assert flatten_config(data, sep="__") == {"service__database__port": 5432}


def test_flatten_config_rejects_empty_separator() -> None:
    with pytest.raises(ValueError):
        flatten_config({"service": {"host": "localhost"}}, sep="")


def test_flatten_config_does_not_mutate_input() -> None:
    data: dict[str, object] = {
        "service": {
            "database": {"port": 5432},
            "features": ["metrics", "alerts"],
        },
    }
    original = copy.deepcopy(data)

    flatten_config(data)

    assert data == original
