from hashlib import sha256

from playground.nacre import build_manifest


def test_build_manifest_computes_sha256_digest() -> None:
    manifest = build_manifest({"notes.txt": "hello"})

    assert manifest == [
        {
            "path": "notes.txt",
            "size": 5,
            "sha256": sha256(b"hello").hexdigest(),
        }
    ]


def test_build_manifest_uses_utf8_byte_size() -> None:
    content = "cafe \u2603"

    assert build_manifest({"unicode.txt": content})[0]["size"] == len(
        content.encode("utf-8")
    )


def test_build_manifest_sorts_entries_by_path() -> None:
    manifest = build_manifest(
        {
            "zeta.txt": "last",
            "alpha.txt": "first",
            "middle.txt": "second",
        }
    )

    assert [entry["path"] for entry in manifest] == [
        "alpha.txt",
        "middle.txt",
        "zeta.txt",
    ]


def test_build_manifest_returns_empty_list_for_empty_input() -> None:
    assert build_manifest({}) == []


def test_build_manifest_handles_multiple_files() -> None:
    manifest = build_manifest(
        {
            "b.txt": "bravo",
            "a.txt": "alpha",
        }
    )

    assert manifest == [
        {
            "path": "a.txt",
            "size": len("alpha".encode("utf-8")),
            "sha256": sha256(b"alpha").hexdigest(),
        },
        {
            "path": "b.txt",
            "size": len("bravo".encode("utf-8")),
            "sha256": sha256(b"bravo").hexdigest(),
        },
    ]


def test_build_manifest_does_not_mutate_input() -> None:
    files = {
        "zeta.txt": "last",
        "alpha.txt": "first",
    }
    original = dict(files)

    build_manifest(files)

    assert files == original
