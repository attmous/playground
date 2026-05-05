from playground.beacon2 import group_events


def test_group_events_groups_by_requested_key() -> None:
    events: list[dict[str, object]] = [
        {"kind": "click", "id": 1},
        {"kind": "view", "id": 2},
        {"kind": "click", "id": 3},
    ]

    assert group_events(events, "kind") == {
        "click": [
            {"kind": "click", "id": 1},
            {"kind": "click", "id": 3},
        ],
        "view": [{"kind": "view", "id": 2}],
    }


def test_group_events_uses_unknown_for_missing_and_none_keys() -> None:
    events: list[dict[str, object]] = [
        {"kind": None, "id": 1},
        {"id": 2},
        {"kind": "view", "id": 3},
    ]

    assert group_events(events, "kind") == {
        "unknown": [{"kind": None, "id": 1}, {"id": 2}],
        "view": [{"kind": "view", "id": 3}],
    }


def test_group_events_preserves_original_order_within_groups() -> None:
    events: list[dict[str, object]] = [
        {"kind": "view", "id": 1},
        {"kind": "click", "id": 2},
        {"kind": "view", "id": 3},
        {"kind": "click", "id": 4},
    ]

    grouped = group_events(events, "kind")

    assert [event["id"] for event in grouped["click"]] == [2, 4]
    assert [event["id"] for event in grouped["view"]] == [1, 3]


def test_group_events_returns_group_keys_sorted_alphabetically() -> None:
    events: list[dict[str, object]] = [
        {"kind": "zebra"},
        {"kind": "alpha"},
        {"kind": "middle"},
    ]

    assert list(group_events(events, "kind")) == ["alpha", "middle", "zebra"]


def test_group_events_converts_non_string_values_to_group_keys() -> None:
    events: list[dict[str, object]] = [
        {"status": 200, "path": "/ok"},
        {"status": False, "path": "/disabled"},
        {"status": 200, "path": "/health"},
    ]

    assert group_events(events, "status") == {
        "200": [
            {"status": 200, "path": "/ok"},
            {"status": 200, "path": "/health"},
        ],
        "False": [{"status": False, "path": "/disabled"}],
    }


def test_group_events_does_not_mutate_input_events() -> None:
    events: list[dict[str, object]] = [
        {"kind": "click", "id": 1},
        {"kind": None, "id": 2},
    ]
    original = [dict(event) for event in events]

    grouped = group_events(events, "kind")
    grouped["click"][0]["id"] = 99

    assert events == original
