from daedalus_playground import excited_greeting, greeting


def test_greeting_uses_default_name() -> None:
    assert greeting() == "Hello, Daedalus!"


def test_greeting_trims_custom_name() -> None:
    assert greeting("  Hermes  ") == "Hello, Hermes!"


def test_excited_greeting_uses_default_name() -> None:
    assert excited_greeting() == "Hello, Daedalus!!"


def test_excited_greeting_trims_custom_name() -> None:
    assert excited_greeting("  Hermes  ") == "Hello, Hermes!!"
