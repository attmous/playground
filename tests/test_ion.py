from playground.ion import ion_token


def test_ion_token_uses_default_name() -> None:
    assert ion_token() == "Ion: Sprints"


def test_ion_token_trims_custom_name() -> None:
    assert ion_token("  Hermes  ") == "Ion: Hermes"


def test_ion_token_uses_default_for_blank_name() -> None:
    assert ion_token("   ") == "Ion: Sprints"
