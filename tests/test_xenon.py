from playground.xenon import xenon_token


def test_xenon_token_uses_default_name() -> None:
    assert xenon_token() == "Xenon: Sprints"


def test_xenon_token_trims_custom_name() -> None:
    assert xenon_token("  Hermes  ") == "Xenon: Hermes"


def test_xenon_token_uses_default_for_blank_name() -> None:
    assert xenon_token("   ") == "Xenon: Sprints"
