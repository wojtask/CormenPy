from unittest import TestCase

from chapter06.textbook import *
from datastructures.array import Array
from datastructures.heap import Heap


class Chapter06Test(TestCase):
    def test_parent_even(self):
        parent_index = parent(42)
        self.assertEqual(parent_index, 21)

    def test_parent_odd(self):
        parent_index = parent(43)
        self.assertEqual(parent_index, 21)

    def test_left(self):
        left_index = left(21)
        self.assertEqual(left_index, 42)

    def test_right(self):
        right_index = right(21)
        self.assertEqual(right_index, 43)

    def test_max_heapify(self):
        heap = Heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        max_heapify(heap, 2)
        expected_heap = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        self.assertEqual(heap, expected_heap)

    def test_build_max_heap(self):
        array = Array([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        build_max_heap(array)
        expected_heap = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        self.assertEqual(array, expected_heap)

    def test_build_max_heap_(self):
        array = Array([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        build_max_heap_(array)
        expected_heap = Heap([16, 14, 10, 8, 7, 3, 9, 1, 4, 2])
        self.assertEqual(array, expected_heap)

    def test_heapsort_singleton(self):
        heap = Heap([3])
        heapsort(heap)
        expected_heap = Heap([3])
        self.assertEqual(heap, expected_heap)

    def test_heapsort_array(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        heap = Array(data)
        heapsort(heap)
        expected_heap = Heap(sorted(data))
        expected_heap.heap_size = 1
        self.assertEqual(heap, expected_heap)

    def test_heap_maximum(self):
        heap = Heap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
        max = heap_maximum(heap)
        self.assertEqual(15, max)
        expected_heap = Heap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
        self.assertEqual(heap, expected_heap)

    def test_extract_max(self):
        heap = Heap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
        max = heap_extract_max(heap)
        self.assertEqual(15, max)
        expected_heap = Heap([13, 12, 9, 5, 6, 8, 7, 4, 0, 1, 2])
        actual_heap = Heap(heap.data[0:-1])
        self.assertEqual(actual_heap, expected_heap)

    def test_increase_key(self):
        heap = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        heap_increase_key(heap, 9, 15)
        expected_heap = Heap([16, 15, 10, 14, 7, 9, 3, 2, 8, 1])
        self.assertEqual(heap, expected_heap)

    def test_increase_key_with_smaller_value(self):
        heap = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        with self.assertRaisesRegex(RuntimeError, "new key is smaller than current key"):
            heap_increase_key(heap, 9, 3)

    def test_max_heap_insert(self):
        heap = Heap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
        heap.data.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        max_heap_insert(heap, 10)
        expected_heap = Heap([15, 13, 10, 5, 12, 9, 7, 4, 0, 6, 2, 1, 8])
        self.assertEqual(heap, expected_heap)
