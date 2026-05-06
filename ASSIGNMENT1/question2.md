---

## 1️ Factorial (Simple Recursion)

### Time Complexity: O(n)

**Justification:**
- The function makes one recursive call for each value from `n` down to `1`.
- So total calls = `n`.
- Each call performs one multiplication.
- Therefore, total operations grow linearly with `n`.

**Time Complexity = O(n)**

### Space Complexity: O(n)

**Justification:**
- Each recursive call stays in the call stack until the base case is reached.
- Maximum recursion depth = `n`.
- So stack space used is proportional to `n`.

➡ **Space Complexity = O(n)**

---
2️⃣ Factorial (Using Stored Values)
Time Complexity: O(n)
Justification:

Even though we use storage (memoization), factorial naturally calculates each value only once.
fact(n) calls fact(n-1), then fact(n-2), and so on.
Each value from 0 to n is computed only once.
So total computations = n.
Time Complexity = O(n)

Space Complexity: O(n)
Justification:

Recursion stack depth = n
Storage list size = n + 1
Both grow linearly with n.
Space Complexity = O(n)

3️⃣ Fibonacci (Simple Recursion)
Time Complexity: O(2^n)
Justification:

Each call makes two recursive calls:

fib(n) = fib(n-1) + fib(n-2)

This creates a binary recursion tree.

Many values are recomputed multiple times.

Example: fib(5) calculates fib(3) twice, fib(2) three times, etc.

Total number of calls grows exponentially.

Time Complexity = O(2^n)

Space Complexity: O(n)
Justification:

Even though total calls are exponential,
Maximum recursion depth is still n.
So stack space = n.
Space Complexity = O(n)

4️⃣ Fibonacci (Using Stored Values)
Time Complexity: O(n)
Justification:

Each Fibonacci value from 0 to n is computed only once.
After storing, it is directly returned without recalculating.
So total computations = n.
➡ Time Complexity = O(n)

Space Complexity: O(n)
Justification:

Recursion stack depth = n
Storage list size = n + 1
Both grow linearly.
Space Complexity = O(n)