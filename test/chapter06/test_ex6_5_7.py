import unittest

from chapter06.ex6_5_7 import max_heap_delete
from datastructures.heap import Heap


class MaxHeapDelete(unittest.TestCase):
    def test_max_heap_delete_with_heapify(self):
        heap = Heap([27, 7, 20, 4, 6, 13, 17, 0, 3, 2, 1, 5, 11, 10])
        max_heap_delete(heap, 1)
        self.assertEqual([20, 7, 17, 4, 6, 13, 10, 0, 3, 2, 1, 5, 11], heap.data[0:-1])
        self.assertEqual(13, heap.heap_size)

    def test_max_heap_delete_with_traversing_up(self):
        heap = Heap([27, 7, 20, 4, 6, 13, 17, 0, 3, 2, 1, 5, 11, 10])
        max_heap_delete(heap, 9)
        self.assertEqual([27, 10, 20, 7, 6, 13, 17, 0, 4, 2, 1, 5, 11], heap.data[0:-1])
        self.assertEqual(13, heap.heap_size)
