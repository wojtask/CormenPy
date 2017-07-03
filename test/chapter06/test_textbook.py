import unittest

from chapter06.textbook import *
from datastructures.array import Array
from datastructures.heap import Heap


class HeapsortTest(unittest.TestCase):
    def test_parent_even(self):
        parent_index = parent(42)
        self.assertEqual(21, parent_index)

    def test_parent_odd(self):
        parent_index = parent(43)
        self.assertEqual(21, parent_index)

    def test_left(self):
        left_index = left(21)
        self.assertEqual(42, left_index)

    def test_right(self):
        right_index = right(21)
        self.assertEqual(43, right_index)

    def test_max_heapify(self):
        heap = Heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        max_heapify(heap, 2)
        self.assertEqual([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], heap.data)
        self.assertEqual(10, heap.heap_size)

    def test_build_max_heap(self):
        array = Array([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        build_max_heap(array)
        self.assertEqual([16, 14, 10, 8, 7, 9, 3, 2, 4, 1], array.data)
        self.assertEqual(10, array.heap_size)

    def test_build_max_heap_(self):
        array = Array([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        build_max_heap_(array)
        self.assertEqual([16, 14, 10, 8, 7, 3, 9, 1, 4, 2], array.data)
        self.assertEqual(10, array.heap_size)

    def test_heapsort_singleton(self):
        array = Array([3])
        heapsort(array)
        self.assertEqual([3], array.data)

    def test_heapsort_array(self):
        array = Array([5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8])
        heapsort(array)
        self.assertEqual([1, 2, 3, 5, 6, 6, 6, 7, 7, 8, 8, 9], array.data)


class MaxPriorityQueueTest(unittest.TestCase):
    def test_heap_maximum(self):
        heap = Heap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
        max = heap_maximum(heap)
        self.assertEqual(15, max)
        self.assertEqual([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1], heap.data)
        self.assertEqual(12, heap.heap_size)

    def test_extract_max(self):
        heap = Heap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
        max = heap_extract_max(heap)
        self.assertEqual(15, max)
        self.assertEqual([13, 12, 9, 5, 6, 8, 7, 4, 0, 1, 2], heap.data[0:-1])
        self.assertEqual(11, heap.heap_size)

    def test_increase_key(self):
        heap = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        heap_increase_key(heap, 9, 15)
        self.assertEqual([16, 15, 10, 14, 7, 9, 3, 2, 8, 1], heap.data)
        self.assertEqual(10, heap.heap_size)

    def test_max_heap_insert(self):
        heap = Heap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
        heap.data.append(None)  # to increase the heap's capacity for the new element
        max_heap_insert(heap, 10)
        self.assertEqual([15, 13, 10, 5, 12, 9, 7, 4, 0, 6, 2, 1, 8], heap.data)
        self.assertEqual(13, heap.heap_size)
