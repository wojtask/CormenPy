from unittest import TestCase

from chapter09.ex9_3_6 import quantiles
from datastructures.array import Array


class Ex9_3_6Test(TestCase):
    def setUp(self):
        self.data = [5, 0, 7, 9, 4, 2, 6, 8, 3, 1]
        self.array = Array(self.data)

    def test_quantiles_1st_order(self):
        q = quantiles(self.array, 1, self.array.length, 1)
        self.assertEqual(q, set())

    def test_quantiles_2nd_order(self):
        q = quantiles(self.array, 1, self.array.length, 2)
        self.assertIn(q, [{4}, {5}])

    def test_quantiles_5th_order(self):
        q = quantiles(self.array, 1, self.array.length, 5)
        self.assertIn(q, [{1, 3, 5, 7}, {2, 4, 6, 8}])

    def test_quantiles_maximum_order(self):
        q = quantiles(self.array, 1, self.array.length, self.array.length + 1)
        self.assertEqual(q, set(self.data))
