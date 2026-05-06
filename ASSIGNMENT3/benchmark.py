import time
from dataset import generate_datasets

from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort


def benchmark():
    sizes = [1000, 5000, 10000]

    # Step 1: store output in a string
    output = "\n--- Timing Table (seconds) ---\n\n"
    output += "Size | Type | Insertion | Merge | Quick\n"
    output += "-" * 50 + "\n"

    for n in sizes:
        random_data, sorted_data, reverse_data = generate_datasets(n)

        for label, data in [
            ("Random", random_data),
            ("Sorted", sorted_data),
            ("Reverse", reverse_data),
        ]:
            start = time.time()
            insertion_sort(data)
            t1 = time.time() - start

            start = time.time()
            merge_sort(data)
            t2 = time.time() - start

            start = time.time()
            quick_sort(data)
            t3 = time.time() - start

            line = f"{n} | {label} | {t1:.4f} | {t2:.4f} | {t3:.4f}\n"

            output += line

    # Step 2: print to console
    print(output)

    # Step 3: write to file (THIS is where your line goes)
    with open("results/output.txt", "w") as f:
        f.write(output)