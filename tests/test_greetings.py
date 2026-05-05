from playground import greeting


def test_greeting_uses_default_name() -> None:
    assert greeting() == "Hello, Sprints!"


def test_greeting_trims_custom_name() -> None:
    assert greeting("  Hermes  ") == "Hello, Hermes!"


def test_greeting_uses_default_for_blank_name() -> None:
    assert greeting("   ") == "Hello, Sprints!"
