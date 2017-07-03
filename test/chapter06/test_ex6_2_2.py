import unittest

from chapter06.ex6_2_2 import min_heapify
from datastructures.heap import Heap


class MinHeapifyTest(unittest.TestCase):
    def test_min_heapify(self):
        heap = Heap([0, 1, 16, 3, 4, 7, 17, 12, 10, 5, 13, 9, 8, 27])
        min_heapify(heap, 3)
        self.assertEqual([0, 1, 7, 3, 4, 8, 17, 12, 10, 5, 13, 9, 16, 27], heap.data)
        self.assertEqual(14, heap.heap_size)
