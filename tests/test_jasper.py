from playground.jasper import append_checksum, weighted_checksum


def test_weighted_checksum_handles_empty_value() -> None:
    assert weighted_checksum("") == 0


def test_weighted_checksum_handles_single_character() -> None:
    assert weighted_checksum("A") == 65


def test_weighted_checksum_uses_position_weights() -> None:
    assert weighted_checksum("Jasper") == 19


def test_append_checksum_formats_two_digit_suffix() -> None:
    assert append_checksum("ab") == "ab-02"
    assert append_checksum("") == "-00"
