from playground.vector import vector_token


def test_vector_token_uses_default_name() -> None:
    assert vector_token() == "Vector: Sprints"


def test_vector_token_trims_custom_name() -> None:
    assert vector_token("  Hermes  ") == "Vector: Hermes"


def test_vector_token_uses_default_for_blank_name() -> None:
    assert vector_token("   ") == "Vector: Sprints"
