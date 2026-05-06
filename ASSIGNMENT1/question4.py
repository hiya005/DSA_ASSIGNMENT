# Function to search an element using recursive binary search
def search_number(data, key, left, right):
    # Base case: element not found
    if left > right:
        return -1

    middle = (left + right) // 2

    # If element is found
    if data[middle] == key:
        return middle

    # Search left side
    elif data[middle] > key:
        return search_number(data, key, left, middle - 1)

    # Search right side
    else:
        return search_number(data, key, middle + 1, right)

# Time: O(log n) → search space is divided into half each time
# Space: O(log n) → recursion depth depends on number of halvings

def run():
    numbers = [10, 20, 30, 40, 50]
    key = 30
    index = search_number(numbers, key, 0, len(numbers) - 1)
    print(f"Index of {key}: {index}")


if __name__ == "__main__":
    run()