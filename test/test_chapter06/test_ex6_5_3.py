from unittest import TestCase

from chapter06.ex6_5_3 import heap_minimum, heap_extract_min, heap_decrease_key, min_heap_insert
from datastructures.heap import Heap


class Ex6_5_3Test(TestCase):
    def setUp(self):
        self.heap = Heap([0, 1, 7, 3, 4, 8, 17, 12, 10, 5, 13, 9, 16, 27])

    def test_heap_minimum(self):
        min = heap_minimum(self.heap)
        self.assertEqual(0, min)
        expected_heap = Heap([0, 1, 7, 3, 4, 8, 17, 12, 10, 5, 13, 9, 16, 27])
        self.assertEqual(self.heap, expected_heap)

    def test_extract_min(self):
        min = heap_extract_min(self.heap)
        self.assertEqual(0, min)
        expected_heap = Heap([1, 3, 7, 10, 4, 8, 17, 12, 27, 5, 13, 9, 16])
        actual_heap = Heap(self.heap.data[0:-1])  # because the last element is not actually removed from the heap
        self.assertEqual(actual_heap, expected_heap)

    def test_decrease_key(self):
        heap_decrease_key(self.heap, 13, 2)
        expected_heap = Heap([0, 1, 2, 3, 4, 7, 17, 12, 10, 5, 13, 9, 8, 27])
        self.assertEqual(self.heap, expected_heap)

    def test_decrease_key_with_larger_value(self):
        with self.assertRaisesRegex(RuntimeError, 'new key is larger than current key'):
            heap_decrease_key(self.heap, 13, 20)

    def test_min_heap_insert(self):
        self.heap.data.append(None)  # to increase the heap's capacity for the new element
        self.heap.length += 1
        min_heap_insert(self.heap, 6)
        expected_heap = Heap([0, 1, 6, 3, 4, 8, 7, 12, 10, 5, 13, 9, 16, 27, 17])
        self.assertEqual(self.heap, expected_heap)
