from daedalus_playground import farewell, greeting


def test_greeting_uses_default_name() -> None:
    assert greeting() == "Hello, Daedalus!"


def test_greeting_trims_custom_name() -> None:
    assert greeting("  Hermes  ") == "Hello, Hermes!"


def test_farewell_uses_default_name() -> None:
    assert farewell() == "Goodbye, Daedalus!"


def test_farewell_trims_custom_name() -> None:
    assert farewell("  Hermes  ") == "Goodbye, Hermes!"


def test_farewell_falls_back_on_blank_name() -> None:
    assert farewell("   ") == "Goodbye, Daedalus!"
