from playground.matrix import matrix_token


def test_matrix_token_uses_default_name() -> None:
    assert matrix_token() == "Matrix: Sprints"


def test_matrix_token_trims_custom_name() -> None:
    assert matrix_token("  Hermes  ") == "Matrix: Hermes"


def test_matrix_token_uses_default_for_blank_name() -> None:
    assert matrix_token("   ") == "Matrix: Sprints"
