# Unit 3 Assignment Report
## Data Structures (ETCCDS202)

---

## Objective

To implement and analyze sorting algorithms by comparing their execution time on different datasets.

---

## Algorithms Implemented

### 1. Insertion Sort
A comparison-based sorting algorithm efficient for small or nearly sorted datasets.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)

---

### 2. Merge Sort
A divide-and-conquer algorithm with consistent performance.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

---

### 3. Quick Sort
A highly efficient sorting algorithm based on partitioning.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)

---

## Dataset Types

- Random
- Sorted
- Reverse Sorted

Dataset Sizes:
- 1000
- 5000
- 10000

---

## Performance Analysis

### Insertion Sort
Performed efficiently on sorted datasets due to minimal shifting.

### Merge Sort
Showed stable and predictable performance across all inputs.

### Quick Sort
Fast for random datasets but degraded significantly on sorted input because of poor pivot selection.

---

## Stability Comparison

| Algorithm | Stable | In-place |
|----------|--------|---------|
| Insertion Sort | Yes | Yes |
| Merge Sort | Yes | No |
| Quick Sort | No | Yes |

---

## Conclusion

The benchmark demonstrates that algorithm efficiency depends heavily on input characteristics.

Insertion Sort is ideal for small/nearly sorted data.

Merge Sort provides reliable performance.

Quick Sort is efficient on average but vulnerable to worst-case inputs.