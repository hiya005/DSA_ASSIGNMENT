def load_sample_data(pm, graph):
    pm.add_user(1, "Alice", ["music", "sports"])
    pm.add_user(2, "Bob", ["music", "coding"])
    pm.add_user(3, "Charlie", ["sports", "travel"])
    pm.add_user(4, "David", ["coding", "travel"])
    pm.add_user(5, "Eve", ["music", "travel"])

    connections = [(1,2), (1,3), (2,4), (3,5)]

    for u, v in connections:
        graph.add_connection(u, v)