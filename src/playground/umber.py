def find_cycle(graph: dict[str, list[str]]) -> list[str]:
    """Return one deterministic dependency cycle from graph, if present."""
    nodes = set(graph)
    for dependencies in graph.values():
        nodes.update(dependencies)

    visited: set[str] = set()
    visiting: set[str] = set()
    stack: list[str] = []

    def visit(node: str) -> list[str]:
        visiting.add(node)
        stack.append(node)

        for neighbor in sorted(graph.get(node, [])):
            if neighbor in visiting:
                cycle_start = stack.index(neighbor)
                return stack[cycle_start:] + [neighbor]
            if neighbor not in visited:
                cycle = visit(neighbor)
                if cycle:
                    return cycle

        stack.pop()
        visiting.remove(node)
        visited.add(node)
        return []

    for node in sorted(nodes):
        if node not in visited:
            cycle = visit(node)
            if cycle:
                return cycle

    return []
