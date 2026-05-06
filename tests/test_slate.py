from copy import deepcopy

from playground.slate import resolve_overlay


def test_resolve_overlay_merges_nested_dictionaries() -> None:
    base: dict[str, object] = {
        "service": {
            "host": "api.local",
            "limits": {"retries": 3, "timeout": 10},
        },
    }
    override: dict[str, object] = {
        "service": {
            "limits": {"timeout": 30},
            "enabled": True,
        },
    }

    assert resolve_overlay(base, override) == {
        "service": {
            "host": "api.local",
            "limits": {"retries": 3, "timeout": 30},
            "enabled": True,
        },
    }


def test_resolve_overlay_deletes_existing_keys_with_none() -> None:
    base: dict[str, object] = {
        "service": {
            "host": "api.local",
            "token": "secret",
        },
        "debug": True,
    }
    override: dict[str, object] = {
        "service": {"token": None},
        "debug": None,
        "missing": None,
    }

    assert resolve_overlay(base, override) == {
        "service": {"host": "api.local"},
    }


def test_resolve_overlay_overrides_scalar_and_list_values() -> None:
    base: dict[str, object] = {
        "retries": 2,
        "features": ["stable"],
    }
    override: dict[str, object] = {
        "retries": 5,
        "features": ["stable", "preview"],
    }

    assert resolve_overlay(base, override) == {
        "retries": 5,
        "features": ["stable", "preview"],
    }


def test_resolve_overlay_does_not_mutate_inputs() -> None:
    base: dict[str, object] = {
        "service": {
            "host": "api.local",
            "limits": {"retries": 3, "timeout": 10},
        },
        "features": ["stable"],
    }
    override: dict[str, object] = {
        "service": {
            "limits": {"timeout": 30},
            "enabled": True,
        },
        "features": ["stable", "preview"],
    }
    original_base = deepcopy(base)
    original_override = deepcopy(override)

    result = resolve_overlay(base, override)

    assert base == original_base
    assert override == original_override
    assert result is not base
    assert result["service"] is not base["service"]
    assert result["features"] is not override["features"]
