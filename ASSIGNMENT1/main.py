import os
from recursion import factorial, fib_naive, fib_memo, hanoi, binary_search

os.makedirs("results", exist_ok=True)

output = ""

# Factorial
output += "--- Factorial ---\n"
output += f"Factorial(5): {factorial(5)}\n\n"

# Fibonacci
output += "--- Fibonacci ---\n"
output += f"Naive Fib(6): {fib_naive(6)}\n"
output += f"Memoized Fib(6): {fib_memo(6)}\n\n"

# Tower of Hanoi
output += "--- Tower of Hanoi (n=3) ---\n"
moves = []
hanoi(3, 'A', 'B', 'C', moves)
for m in moves:
    output += m + "\n"

output += f"Total Moves: {len(moves)}\n\n"

# Binary Search
output += "--- Binary Search ---\n"
arr = [10, 20, 30, 40, 50]
output += f"Search 30: Index {binary_search(arr, 30, 0, len(arr)-1)}\n"
output += f"Search 99: Index {binary_search(arr, 99, 0, len(arr)-1)}\n"

print(output)

with open("results/output.txt", "w") as f:
    f.write(output)