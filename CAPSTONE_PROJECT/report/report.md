# Social Network Explorer (SNE)
## Data Structures Capstone Project

---

## Objective

To design and implement a simplified social network system using core data structures such as hashing, graphs, BFS, DFS, and sorting.

---

## Features Implemented

### 1. Profile Management (Hashing)
- Add user
- Get profile
- Update profile

Used Python dictionary as a hash table for fast lookup (O(1) average time).

---

### 2. Social Network Graph
- Represented using adjacency list
- Supports adding/removing connections
- Fetch friend lists

Time Complexity:
O(1) average for insertion

---

### 3. BFS (Shortest Path)
- Finds shortest path between two users
- Represents degrees of separation

Time Complexity:
O(V + E)

---

### 4. DFS (Exploration)
- Explores network up to depth *d*
- Useful for discovering friends-of-friends

---

### 5. Recommendation System
- Suggests users based on common interests
- Uses intersection of interest sets
- Sorted by relevance

---

## Sample Execution

- Created 5 user profiles
- Established connections
- Found shortest path using BFS
- Explored network using DFS
- Generated recommendations

---

## Key Data Structures Used

| Feature | Data Structure |
|--------|--------|
| Profiles | Hash Table |
| Network | Graph (Adjacency List) |
| Traversal | Queue (BFS), Recursion (DFS) |
| Recommendation | Sorting + Sets |

---

## Conclusion

This project demonstrates how multiple data structures work together to solve real-world problems.  
Graphs model relationships, hashing enables fast access, and traversal algorithms enable meaningful insights.

---

## Future Improvements

- Interactive CLI interface
- Better recommendation scoring
- Graph visualization
- Database integration