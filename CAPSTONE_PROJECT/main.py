import os
from profiles import ProfileManager
from network.graph import SocialGraph
from algorithms.bfs import shortest_path
from algorithms.dfs import dfs
from recommendations.recommend import recommend_users
from data.sample_data import load_sample_data

os.makedirs("results", exist_ok=True)

pm = ProfileManager()
graph = SocialGraph()

load_sample_data(pm, graph)

output = ""

# Show profiles
output += "\n--- Profiles ---\n"
for uid in pm.users:
    output += pm.display_profile(uid) + "\n"

# BFS shortest path
output += "\n--- Shortest Path (1 -> 4) ---\n"
output += str(shortest_path(graph.graph, 1, 4)) + "\n"

# DFS exploration
output += "\n--- DFS Depth 2 from 1 ---\n"
output += str(dfs(graph.graph, 1, 2)) + "\n"

# Recommendations
output += "\n--- Recommendations for 1 ---\n"
output += str(recommend_users(pm, graph.graph, 1)) + "\n"

print(output)

with open("results/output.txt", "w") as f:
    f.write(output)