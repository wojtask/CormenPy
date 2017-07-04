import unittest

from chapter05.pr5_2 import random_search
from datastructures.array import Array


class RandomSearchTest(unittest.TestCase):
    def setUp(self):
        self.array = Array([5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8])

    def test_random_search_positive(self):
        index = random_search(self.array, 3)
        self.assertEqual(9, index)

    def test_random_search_negative(self):
        index = random_search(self.array, 4)
        self.assertIsNone(index)
