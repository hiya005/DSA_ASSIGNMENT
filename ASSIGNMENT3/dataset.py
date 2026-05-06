import random

def generate_datasets(n):
    random_data = [random.randint(1, 10000) for _ in range(n)]
    sorted_data = sorted(random_data)
    reverse_data = sorted_data[::-1]

    return random_data, sorted_data, reverse_data