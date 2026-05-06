import random

def quick_sort(arr):
    a = arr.copy()
    quick_sort_helper(a, 0, len(a) - 1)
    return a


def quick_sort_helper(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quick_sort_helper(a, low, pi - 1)
        quick_sort_helper(a, pi + 1, high)


def partition(a, low, high):
    # Step 1: pick a random pivot and move it to end
    pivot_index = random.randint(low, high)
    a[pivot_index], a[high] = a[high], a[pivot_index]

    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1