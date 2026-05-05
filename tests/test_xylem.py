from playground.xylem import normalize_csv_rows


def test_normalize_csv_rows_parses_normal_csv() -> None:
    text = "name,age\nAda,36\nGrace,85\n"

    assert normalize_csv_rows(text) == [
        {"name": "Ada", "age": "36"},
        {"name": "Grace", "age": "85"},
    ]


def test_normalize_csv_rows_trims_headers_and_cell_values() -> None:
    text = " name , age \n Ada , 36 \n"

    assert normalize_csv_rows(text) == [{"name": "Ada", "age": "36"}]


def test_normalize_csv_rows_ignores_completely_blank_rows() -> None:
    text = "name,age\n\n   ,   \nAda,36\n"

    assert normalize_csv_rows(text) == [{"name": "Ada", "age": "36"}]


def test_normalize_csv_rows_fills_missing_cells_with_empty_strings() -> None:
    text = "name,age,city\nAda,36\n"

    assert normalize_csv_rows(text) == [{"name": "Ada", "age": "36", "city": ""}]


def test_normalize_csv_rows_ignores_extra_cells() -> None:
    text = "name,age\nAda,36,London\n"

    assert normalize_csv_rows(text) == [{"name": "Ada", "age": "36"}]


def test_normalize_csv_rows_preserves_quoted_commas() -> None:
    text = 'name,note\nAda,"engineer, mathematician"\n'

    assert normalize_csv_rows(text) == [
        {"name": "Ada", "note": "engineer, mathematician"}
    ]


def test_normalize_csv_rows_returns_empty_list_for_empty_input() -> None:
    assert normalize_csv_rows("") == []
