import unittest

from chapter06.ex6_5_3 import heap_minimum, heap_extract_min, heap_decrease_key, min_heap_insert
from datastructures.heap import Heap


class MinPriorityQueueTest(unittest.TestCase):
    def setUp(self):
        self.heap = Heap([0, 1, 7, 3, 4, 8, 17, 12, 10, 5, 13, 9, 16, 27])

    def test_heap_minimum(self):
        min = heap_minimum(self.heap)
        self.assertEqual(0, min)
        self.assertEqual([0, 1, 7, 3, 4, 8, 17, 12, 10, 5, 13, 9, 16, 27], self.heap.data)
        self.assertEqual(14, self.heap.heap_size)

    def test_extract_min(self):
        min = heap_extract_min(self.heap)
        self.assertEqual(0, min)
        self.assertEqual([1, 3, 7, 10, 4, 8, 17, 12, 27, 5, 13, 9, 16], self.heap.data[0:-1])
        self.assertEqual(13, self.heap.heap_size)

    def test_decrease_key(self):
        heap_decrease_key(self.heap, 13, 2)
        self.assertEqual([0, 1, 2, 3, 4, 7, 17, 12, 10, 5, 13, 9, 8, 27], self.heap.data)
        self.assertEqual(14, self.heap.heap_size)

    def test_decrease_key_with_larger_value(self):
        with self.assertRaisesRegex(RuntimeError, "new key is larger than current key"):
            heap_decrease_key(self.heap, 13, 20)

    def test_min_heap_insert(self):
        self.heap.data.append(None)  # to increase the heap's capacity for the new element
        min_heap_insert(self.heap, 6)
        self.assertEqual([0, 1, 6, 3, 4, 8, 7, 12, 10, 5, 13, 9, 16, 27, 17], self.heap.data)
        self.assertEqual(15, self.heap.heap_size)

