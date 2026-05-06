def dependency_depths(
    graph: dict[str, list[str] | tuple[str, ...]],
) -> dict[str, int]:
    """Return the longest dependency-chain depth for each node in graph."""
    # Normalize dependencies so dependency-only nodes can be traversed like keys.
    dependencies_by_node: dict[str, tuple[str, ...]] = {
        node: tuple(dependencies) for node, dependencies in graph.items()
    }
    for dependencies in graph.values():
        for dependency in dependencies:
            dependencies_by_node.setdefault(dependency, ())

    depths: dict[str, int] = {}
    # Track the DFS path separately from completed nodes to catch back edges.
    visiting: set[str] = set()
    visited: set[str] = set()

    def depth_for(node: str) -> int:
        if node in visited:
            return depths[node]
        if node in visiting:
            raise ValueError("cycle detected")

        visiting.add(node)
        dependencies = dependencies_by_node[node]
        # A node's depth is one more than its deepest direct dependency.
        if dependencies:
            depth = 1 + max(depth_for(dependency) for dependency in dependencies)
        else:
            depth = 0
        visiting.remove(node)
        visited.add(node)
        depths[node] = depth
        return depth

    for node in dependencies_by_node:
        depth_for(node)

    return depths
