import unittest

from chapter06.ex6_2_5 import iterative_max_heapify
from datastructures.heap import Heap


class Ex6_2_5Test(unittest.TestCase):
    def test_min_heapify(self):
        heap = Heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        iterative_max_heapify(heap, 2)
        expected_heap = Heap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        self.assertEqual(expected_heap, heap)
