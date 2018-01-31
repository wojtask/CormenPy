import random

from datastructures.array import Array
from datastructures.matrix import Matrix


def get_random_array(min_size=1, max_size=20, min_value=0, max_value=999):
    size = random.randint(min_size, max_size)
    elements = [random.randint(min_value, max_value) for _ in range(size)]
    return Array(elements), elements


def get_random_unique_array(min_size=1, max_size=20, min_value=0, max_value=999):
    size = random.randint(min_size, max_size)
    elements = random.sample(range(min_value, max_value + 1), size)
    return Array(elements), elements


def get_random_matrix(rows, columns, min_value=0, max_value=999):
    elements = [[random.randint(min_value, max_value) for _ in range(columns)] for _ in range(rows)]
    return Matrix(elements), elements
