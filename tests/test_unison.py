from copy import deepcopy

from playground.unison import resolve_options


def test_resolve_options_applies_direct_overrides() -> None:
    assert resolve_options(
        {"enabled": False, "timeout": 5}, {"enabled": True}
    ) == {"enabled": True, "timeout": 5}


def test_resolve_options_removes_keys_with_none_override() -> None:
    assert resolve_options(
        {"enabled": True, "timeout": 5}, {"timeout": None, "missing": None}
    ) == {"enabled": True}


def test_resolve_options_merges_nested_dictionaries() -> None:
    assert resolve_options(
        {
            "sync": {
                "enabled": True,
                "retries": 2,
                "paths": {"source": "src", "target": "dist"},
            }
        },
        {"sync": {"retries": 3, "paths": {"target": "build"}}},
    ) == {
        "sync": {
            "enabled": True,
            "retries": 3,
            "paths": {"source": "src", "target": "build"},
        }
    }


def test_resolve_options_replaces_nested_dict_with_scalar() -> None:
    assert resolve_options(
        {"sync": {"enabled": True, "retries": 2}}, {"sync": "disabled"}
    ) == {"sync": "disabled"}


def test_resolve_options_adds_new_keys() -> None:
    assert resolve_options(
        {"enabled": True}, {"timeout": 5, "sync": {"retries": 2}}
    ) == {"enabled": True, "timeout": 5, "sync": {"retries": 2}}


def test_resolve_options_does_not_mutate_inputs() -> None:
    defaults: dict[str, object] = {
        "sync": {"enabled": True, "paths": {"source": "src", "target": "dist"}},
        "timeout": 5,
    }
    overrides: dict[str, object | None] = {
        "sync": {"paths": {"target": "build"}},
        "timeout": None,
        "mode": "fast",
    }
    original_defaults = deepcopy(defaults)
    original_overrides = deepcopy(overrides)

    result = resolve_options(defaults, overrides)

    assert result == {
        "sync": {"enabled": True, "paths": {"source": "src", "target": "build"}},
        "mode": "fast",
    }
    assert defaults == original_defaults
    assert overrides == original_overrides


def test_resolve_options_result_does_not_share_nested_input_dictionaries() -> None:
    defaults: dict[str, object] = {"sync": {"enabled": True}}
    overrides: dict[str, object | None] = {"paths": {"target": "build"}}

    result = resolve_options(defaults, overrides)
    result["sync"]["enabled"] = False  # type: ignore[index]
    result["paths"]["target"] = "dist"  # type: ignore[index]

    assert defaults == {"sync": {"enabled": True}}
    assert overrides == {"paths": {"target": "build"}}
