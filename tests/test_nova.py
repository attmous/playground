from playground.nova import nova_token


def test_nova_token_uses_default_name() -> None:
    assert nova_token() == "Nova: Sprints"


def test_nova_token_trims_custom_name() -> None:
    assert nova_token("  Hermes  ") == "Nova: Hermes"


def test_nova_token_falls_back_for_blank_name() -> None:
    assert nova_token("   ") == "Nova: Sprints"
