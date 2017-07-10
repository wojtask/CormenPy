from unittest import TestCase

from chapter02.ex2_3_5 import recursive_binary_search, iterative_binary_search
from datastructures.array import Array


class Ex2_3_5Test(TestCase):
    def setUp(self):
        self.array = Array([1, 2, 3, 5, 6, 6, 6, 7, 7, 8, 8, 9])

    def test_recursive_binary_search_positive(self):
        index = recursive_binary_search(self.array, 3, 1, self.array.length)
        self.assertEqual(3, index)

    def test_recursive_binary_search_negative(self):
        index = recursive_binary_search(self.array, 4, 1, self.array.length)
        self.assertIsNone(index)

    def test_iterative_binary_search_positive(self):
        index = iterative_binary_search(self.array, 3)
        self.assertEqual(3, index)

    def test_iterative_binary_search_negative(self):
        index = iterative_binary_search(self.array, 4)
        self.assertIsNone(index)
