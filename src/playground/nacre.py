from hashlib import sha256


def build_manifest(files: dict[str, str]) -> list[dict[str, object]]:
    """Return checksum manifest entries sorted by path."""
    manifest: list[dict[str, object]] = []

    for path in sorted(files):
        content_bytes = files[path].encode("utf-8")
        manifest.append(
            {
                "path": path,
                "size": len(content_bytes),
                "sha256": sha256(content_bytes).hexdigest(),
            }
        )

    return manifest
