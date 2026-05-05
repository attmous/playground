from playground.ember import ember_token


def test_ember_token_uses_default_name() -> None:
    assert ember_token() == "Ember: Sprints"


def test_ember_token_trims_custom_name() -> None:
    assert ember_token("  Hermes  ") == "Ember: Hermes"


def test_ember_token_falls_back_for_blank_name() -> None:
    assert ember_token("   ") == "Ember: Sprints"
