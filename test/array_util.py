import random

from datastructures.array import Array
from util import between


def get_random_array(size=None, min_size=1, max_size=20, min_value=0, max_value=999, start=1, unique=False):
    if size is None:
        size = random.randint(min_size, max_size)
    if unique:
        elements = random.sample(between(min_value, max_value), size)
    else:
        elements = [random.randint(min_value, max_value) for _ in between(1, size)]
    return Array(elements, start=start)
