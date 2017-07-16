import random

from datastructures.array import Array


def random_int_array(min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    data = [random.randint(0, max_value) for _ in range(size)]
    return Array(data), data


def random_unique_int_array(min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    data = random.sample(range(0, max_value + 1), size)
    return Array(data), data
