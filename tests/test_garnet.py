from playground.garnet import allowed_actions


def test_allowed_actions_for_single_role() -> None:
    grants = {"admin": ["delete", "read"]}

    assert allowed_actions(["admin"], grants) == ["delete", "read"]


def test_allowed_actions_combines_multiple_roles() -> None:
    grants = {
        "editor": ["write", "read"],
        "auditor": ["export"],
    }

    assert allowed_actions(["editor", "auditor"], grants) == [
        "export",
        "read",
        "write",
    ]


def test_allowed_actions_ignores_unknown_roles() -> None:
    grants = {"viewer": ["read"]}

    assert allowed_actions(["viewer", "missing"], grants) == ["read"]


def test_allowed_actions_deduplicates_and_sorts_actions() -> None:
    grants = {
        "admin": ["write", "read", "write"],
        "editor": ["read", "archive"],
    }

    assert allowed_actions(["admin", "editor", "admin"], grants) == [
        "archive",
        "read",
        "write",
    ]


def test_allowed_actions_matches_roles_case_sensitively() -> None:
    grants = {
        "Admin": ["delete"],
        "admin": ["read"],
    }

    assert allowed_actions(["admin"], grants) == ["read"]


def test_allowed_actions_returns_empty_list_for_empty_roles() -> None:
    grants = {"admin": ["delete"]}

    assert allowed_actions([], grants) == []


def test_allowed_actions_does_not_mutate_inputs() -> None:
    roles = ["admin", "viewer"]
    grants = {
        "admin": ["delete", "read"],
        "viewer": ["read"],
    }
    original_roles = list(roles)
    original_grants = {role: list(actions) for role, actions in grants.items()}

    assert allowed_actions(roles, grants) == ["delete", "read"]
    assert roles == original_roles
    assert grants == original_grants
