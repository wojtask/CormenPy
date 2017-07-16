from unittest import TestCase

from chapter06.textbook import parent

tc = TestCase()


def assert_max_heap(heap):
    for i in range(2, heap.heap_size + 1):
        tc.assertTrue(heap[parent(i)] >= heap[i])


def assert_min_heap(heap):
    for i in range(2, heap.heap_size + 1):
        tc.assertTrue(heap[parent(i)] <= heap[i])
