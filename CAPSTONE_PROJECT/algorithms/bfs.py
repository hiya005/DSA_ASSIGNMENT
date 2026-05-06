from collections import deque

def shortest_path(graph, start, target):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        if node == target:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                queue.append((neighbor, path + [neighbor]))

    return None