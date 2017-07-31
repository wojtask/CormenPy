import random

from datastructures.array import Array


def get_random_array(min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    elements = [random.randint(0, max_value) for _ in range(size)]
    return Array(elements), elements


def get_random_unique_array(min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    elements = random.sample(range(0, max_value + 1), size)
    return Array(elements), elements
