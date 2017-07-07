import unittest

from chapter06.ex6_2_2 import min_heapify
from datastructures.heap import Heap


class Ex6_2_2Test(unittest.TestCase):
    def test_min_heapify(self):
        heap = Heap([0, 1, 16, 3, 4, 7, 17, 12, 10, 5, 13, 9, 8, 27])
        min_heapify(heap, 3)
        expected_heap = Heap([0, 1, 7, 3, 4, 8, 17, 12, 10, 5, 13, 9, 16, 27])
        self.assertEqual(expected_heap, heap)
