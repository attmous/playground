from playground.larch import group_by_extension


def test_group_by_extension_lowercases_mixed_case_extensions() -> None:
    paths = ["notes.TXT", "archive.tar.GZ", "photo.JpEg"]

    assert group_by_extension(paths) == {
        "txt": ["notes.TXT"],
        "gz": ["archive.tar.GZ"],
        "jpeg": ["photo.JpEg"],
    }


def test_group_by_extension_uses_empty_key_for_paths_without_extension() -> None:
    paths = ["README", "bin/tool", ".env"]

    assert group_by_extension(paths) == {"": ["README", "bin/tool", ".env"]}


def test_group_by_extension_preserves_order_for_repeated_extensions() -> None:
    paths = ["first.py", "notes.md", "second.PY", "third.py"]

    assert group_by_extension(paths) == {
        "py": ["first.py", "second.PY", "third.py"],
        "md": ["notes.md"],
    }


def test_group_by_extension_accepts_tuple_input() -> None:
    paths = ("src/app.py", "tests/test_app.PY", "LICENSE")

    assert group_by_extension(paths) == {
        "py": ["src/app.py", "tests/test_app.PY"],
        "": ["LICENSE"],
    }
