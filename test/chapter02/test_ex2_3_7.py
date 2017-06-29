import unittest

from chapter02.ex2_3_7 import *
from datastructures.array import Array


class SumSearchTest(unittest.TestCase):
    def setUp(self):
        self.array = Array([5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8])

    def test_sum_search_positive(self):
        self.assertTrue(sum_search(self.array, 17))

    def test_sum_search_negative(self):
        self.assertFalse(sum_search(self.array, 18))
