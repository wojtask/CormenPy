import random

from hamcrest import *

from datastructures.array import Array
from datastructures.heap import Heap
from util import between, ceildiv


def assert_max_heap(heap, arity=2):
    for i in between(2, heap.heap_size):
        parent_idx = ceildiv(i - 1, arity)
        assert_that(heap[parent_idx], is_(greater_than_or_equal_to(heap[i])))


def assert_min_heap(heap, arity=2):
    for i in between(2, heap.heap_size):
        parent_idx = ceildiv(i - 1, arity)
        assert_that(heap[parent_idx], is_(less_than_or_equal_to(heap[i])))


def get_random_max_heap(arity=2):
    size = random.randint(1, 20)
    array = Array.indexed(1, size)
    fill_max_subheap(array, 1, size, 999, arity)
    return Heap(array, heap_size=size)


def fill_max_subheap(array, i, size, upper_bound, arity):
    if i > size:
        return
    max_diff = 100
    array[i] = random.randint(upper_bound - max_diff, upper_bound)
    for k in between(1, arity):
        child_idx = arity * (i - 1) + k + 1
        fill_max_subheap(array, child_idx, size, array[i], arity)


def get_random_min_heap(arity=2):
    size = random.randint(1, 20)
    array = Array.indexed(1, size)
    fill_min_subheap(array, 1, size, 0, arity)
    return Heap(array, heap_size=size)


def fill_min_subheap(array, i, size, lower_bound, arity):
    if i > size:
        return
    max_diff = 100
    array[i] = random.randint(lower_bound, lower_bound + max_diff)
    for k in between(1, arity):
        child_idx = arity * (i - 1) + k + 1
        fill_min_subheap(array, child_idx, size, array[i], arity)
