import unittest

from chapter02.ex2_1_3 import linear_search
from datastructures.array import Array


class LinearSearchTest(unittest.TestCase):
    def setUp(self):
        self.array = Array([5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8])

    def test_linear_search_positive(self):
        index = linear_search(self.array, 3)
        self.assertEqual(9, index)

    def test_linear_search_negative(self):
        index = linear_search(self.array, 4)
        self.assertIsNone(index)
