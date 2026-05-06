import os
from bst import BST
from graph import Graph
from hashing import HashTable

os.makedirs("results", exist_ok=True)


def run_bst():
    output = "\n--- BST Demo ---\n"
    bst = BST()
    root = None

    for key in [50, 30, 70, 20, 40, 60, 80]:
        root = bst.insert(root, key)

    output += f"Inorder: {bst.inorder(root)}\n"

    root = bst.delete(root, 30)
    output += f"After deleting 30: {bst.inorder(root)}\n"

    return output


def run_graph():
    output = "\n--- Graph Demo ---\n"
    g = Graph()

    edges = [(1,2), (1,3), (2,4), (3,5), (4,6)]
    for u, v in edges:
        g.add_edge(u, v)

    output += "Adjacency List:\n"
    for node in g.adj:
        output += f"{node} -> {g.adj[node]}\n"

    output += f"\nBFS: {g.bfs(1)}\n"
    output += f"DFS: {g.dfs(1)}\n"

    return output


def run_hash():
    output = "\n--- Hash Table Demo ---\n"
    ht = HashTable()

    ht.insert(1, "A")
    ht.insert(11, "B")  # collision
    ht.insert(21, "C")  # collision

    output += "Initial Table:\n"
    for i, bucket in enumerate(ht.table):
        output += f"{i}: {bucket}\n"

    output += f"\nGet(11): {ht.get(11)}\n"

    ht.delete(11)

    output += "\nAfter deleting 11:\n"
    for i, bucket in enumerate(ht.table):
        output += f"{i}: {bucket}\n"

    return output


if __name__ == "__main__":
    final_output = ""
    final_output += run_bst()
    final_output += run_graph()
    final_output += run_hash()

    print(final_output)

    with open("results/output.txt", "w") as f:
        f.write(final_output)