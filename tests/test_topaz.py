from playground.topaz import sanitize_row


def test_sanitize_row_strips_keys_and_string_values() -> None:
    row = {
        " name ": " Ada ",
        "\temail\n": " ada@example.com ",
    }

    assert sanitize_row(row) == {
        "name": "Ada",
        "email": "ada@example.com",
    }


def test_sanitize_row_drops_blank_keys() -> None:
    row = {
        " ": "ignored",
        "\t\n": "also ignored",
        "name": "Ada",
    }

    assert sanitize_row(row) == {"name": "Ada"}


def test_sanitize_row_converts_none_and_non_string_values() -> None:
    row = {
        "empty": None,
        "count": 3,
        "enabled": True,
    }

    assert sanitize_row(row) == {
        "empty": "",
        "count": "3",
        "enabled": "True",
    }


def test_sanitize_row_adds_required_defaults() -> None:
    row = {
        " name ": " Ada ",
        "email": "ada@example.com",
    }

    assert sanitize_row(row, required=["name", " company ", "email"]) == {
        "name": "Ada",
        "email": "ada@example.com",
        "company": "",
    }
