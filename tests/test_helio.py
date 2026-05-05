import pytest

from playground.helio import parse_hex_color


def test_parse_hex_color_handles_short_form_with_hash() -> None:
    assert parse_hex_color("#0af") == (0, 170, 255)


def test_parse_hex_color_handles_short_form_without_hash() -> None:
    assert parse_hex_color("3c7") == (51, 204, 119)


def test_parse_hex_color_handles_long_form_with_hash() -> None:
    assert parse_hex_color("#1234ab") == (18, 52, 171)


def test_parse_hex_color_handles_long_form_without_hash() -> None:
    assert parse_hex_color("00AAff") == (0, 170, 255)


def test_parse_hex_color_ignores_surrounding_whitespace() -> None:
    assert parse_hex_color(" \n#c0ffee\t") == (192, 255, 238)


@pytest.mark.parametrize("value", ["", "#12", "1234", "#12345", "1234567", "#ggg"])
def test_parse_hex_color_rejects_invalid_values(value: str) -> None:
    with pytest.raises(ValueError):
        parse_hex_color(value)
