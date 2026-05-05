def walk_tree(tree: dict[str, object]) -> list[str]:
    """Return dot-separated paths to every leaf in a nested dictionary tree."""
    paths: list[str] = []

    def visit(path: str, value: object) -> None:
        if not isinstance(value, dict):
            paths.append(path)
            return

        if not value:
            paths.append(path)
            return

        for key in sorted(value):
            visit(f"{path}.{key}", value[key])

    for key in sorted(tree):
        visit(key, tree[key])

    return paths
