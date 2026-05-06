def dfs(graph, start, depth, visited=None):
    if visited is None:
        visited = set()

    if depth < 0:
        return []

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, depth - 1, visited))

    return result