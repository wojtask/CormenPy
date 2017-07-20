import random
from unittest import TestCase

import math

from datastructures.array import Array

tc = TestCase()


def assert_max_heap(heap, ary=2):
    for i in range(2, heap.heap_size + 1):
        parent_idx = math.ceil((i - 1) / ary)
        tc.assertTrue(heap[parent_idx] >= heap[i])


def assert_min_heap(heap, ary=2):
    for i in range(2, heap.heap_size + 1):
        parent_idx = math.ceil((i - 1) / ary)
        tc.assertTrue(heap[parent_idx] <= heap[i])


def random_max_heap(ary=2, min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value)]
    for i in range(1, size):
        bound = keys[(i - 1) // ary]
        keys.append(random.randint(0, bound))
    heap = Array(keys)
    heap.heap_size = size
    return heap, keys


def random_min_heap(ary=2, min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value)]
    for i in range(1, size):
        bound = keys[(i - 1) // ary]
        keys.append(random.randint(bound, max_value))
    heap = Array(keys)
    heap.heap_size = size
    return heap, keys
