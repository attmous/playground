import pytest

from playground.radix import convert_bytes


def test_convert_bytes_to_bytes() -> None:
    assert convert_bytes(1536, "B") == {
        "value": 1536.0,
        "unit": "B",
        "text": "1536.00 B",
    }


def test_convert_bytes_to_kilobytes() -> None:
    assert convert_bytes(1536, "KB") == {
        "value": 1.5,
        "unit": "KB",
        "text": "1.50 KB",
    }


def test_convert_bytes_to_megabytes() -> None:
    assert convert_bytes(3 * 1024**2, "MB") == {
        "value": 3.0,
        "unit": "MB",
        "text": "3.00 MB",
    }


def test_convert_bytes_to_gigabytes() -> None:
    assert convert_bytes(5 * 1024**3, "GB") == {
        "value": 5.0,
        "unit": "GB",
        "text": "5.00 GB",
    }


def test_convert_bytes_matches_units_case_insensitively() -> None:
    assert convert_bytes(2048, "kb") == {
        "value": 2.0,
        "unit": "KB",
        "text": "2.00 KB",
    }


@pytest.mark.parametrize(
    ("value", "expected_unit", "expected_text"),
    [
        (0, "B", "0.00 B"),
        (1023, "B", "1023.00 B"),
        (1024, "KB", "1.00 KB"),
        (1024**2 - 1, "KB", "1024.00 KB"),
        (1024**2, "MB", "1.00 MB"),
        (1024**3 - 1, "MB", "1024.00 MB"),
        (1024**3, "GB", "1.00 GB"),
    ],
)
def test_convert_bytes_auto_boundaries(
    value: int, expected_unit: str, expected_text: str
) -> None:
    result = convert_bytes(value)

    assert result["unit"] == expected_unit
    assert result["text"] == expected_text


def test_convert_bytes_matches_auto_case_insensitively() -> None:
    assert convert_bytes(1024, "Auto") == {
        "value": 1.0,
        "unit": "KB",
        "text": "1.00 KB",
    }


def test_convert_bytes_rejects_invalid_unit() -> None:
    with pytest.raises(ValueError, match="unsupported unit"):
        convert_bytes(1024, "TB")


def test_convert_bytes_rejects_negative_value() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        convert_bytes(-1)
