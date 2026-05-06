from playground.river import build_cursor


def test_build_cursor_reports_first_page() -> None:
    assert build_cursor(1, 10, 95) == {
        "page": 1,
        "per_page": 10,
        "total": 95,
        "total_pages": 10,
        "has_previous": False,
        "has_next": True,
    }


def test_build_cursor_reports_middle_page() -> None:
    assert build_cursor(3, 20, 95) == {
        "page": 3,
        "per_page": 20,
        "total": 95,
        "total_pages": 5,
        "has_previous": True,
        "has_next": True,
    }


def test_build_cursor_clamps_over_large_page() -> None:
    assert build_cursor(99, 0, 3) == {
        "page": 3,
        "per_page": 1,
        "total": 3,
        "total_pages": 3,
        "has_previous": True,
        "has_next": False,
    }
