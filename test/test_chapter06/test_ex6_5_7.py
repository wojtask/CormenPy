from unittest import TestCase

from chapter06.ex6_5_7 import max_heap_delete
from datastructures.heap import Heap


class Ex6_5_7Test(TestCase):
    def setUp(self):
        self.heap = Heap([27, 7, 20, 4, 6, 13, 17, 0, 3, 2, 1, 5, 11, 10])

    def test_max_heap_delete_with_heapify(self):
        max_heap_delete(self.heap, 1)
        expected_heap = Heap([20, 7, 17, 4, 6, 13, 10, 0, 3, 2, 1, 5, 11])
        actual_heap = Heap(self.heap.data[0:-1])
        self.assertEqual(expected_heap, actual_heap)

    def test_max_heap_delete_with_traversing_up(self):
        max_heap_delete(self.heap, 9)
        expected_heap = Heap([27, 10, 20, 7, 6, 13, 17, 0, 4, 2, 1, 5, 11])
        actual_heap = Heap(self.heap.data[0:-1])
        self.assertEqual(expected_heap, actual_heap)
