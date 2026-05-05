from playground.aurora import aurora_token


def test_aurora_token_uses_default_name() -> None:
    assert aurora_token() == "Aurora: Sprints"


def test_aurora_token_trims_custom_name() -> None:
    assert aurora_token("  Hermes  ") == "Aurora: Hermes"


def test_aurora_token_uses_default_for_blank_name() -> None:
    assert aurora_token("   ") == "Aurora: Sprints"
