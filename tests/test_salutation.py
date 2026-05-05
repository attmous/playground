from playground import salutation


def test_salutation_uses_default_name() -> None:
    assert salutation() == "Salutations, Sprints."


def test_salutation_uses_custom_name() -> None:
    assert salutation("Hermes") == "Salutations, Hermes."


def test_salutation_trims_custom_name() -> None:
    assert salutation("  Hermes  ") == "Salutations, Hermes."


def test_salutation_uses_default_for_blank_name() -> None:
    assert salutation("   ") == "Salutations, Sprints."
