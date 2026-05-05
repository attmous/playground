from playground.quartz import quartz_token


def test_quartz_token_uses_default_name() -> None:
    assert quartz_token() == "Quartz: Sprints"


def test_quartz_token_trims_custom_name() -> None:
    assert quartz_token("  Hermes  ") == "Quartz: Hermes"


def test_quartz_token_uses_default_for_blank_name() -> None:
    assert quartz_token("   ") == "Quartz: Sprints"
