import math
import random

from hamcrest import *

from datastructures.heap import Heap
from util import between


def assert_max_heap(heap, arity=2):
    for i in between(2, heap.heap_size):
        parent_idx = math.ceil((i - 1) / arity)
        assert_that(heap[parent_idx], is_(greater_than_or_equal_to(heap[i])))


def assert_min_heap(heap, arity=2):
    for i in between(2, heap.heap_size):
        parent_idx = math.ceil((i - 1) / arity)
        assert_that(heap[parent_idx], is_(less_than_or_equal_to(heap[i])))


def get_random_max_heap(arity=2, min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value)]
    for i in between(2, size):
        bound = keys[(i - 2) // arity]
        keys.append(random.randint(0, bound))
    return Heap(keys)


def get_random_min_heap(arity=2, min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value)]
    for i in between(2, size):
        bound = keys[(i - 2) // arity]
        keys.append(random.randint(bound, max_value))
    return Heap(keys)
