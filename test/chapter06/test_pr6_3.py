import unittest

from chapter06.pr6_3 import *
from datastructures.array import Array


class Problem6_3Test(unittest.TestCase):
    def test_young_extract_min(self):
        young = Array([
            Array([2, 3, 14, 16]),
            Array([4, 8, math.inf, math.inf]),
            Array([5, 12, math.inf, math.inf]),
            Array([9, math.inf, math.inf, math.inf])
        ])
        min = young_extract_min(young, 4, 4, 1, 1)
        expected_young = Array([
            Array([3, 8, 14, 16]),
            Array([4, 12, math.inf, math.inf]),
            Array([5, math.inf, math.inf, math.inf]),
            Array([9, math.inf, math.inf, math.inf])
        ])
        self.assertEqual(2, min)
        self.assertEqual(expected_young, young)

    def test_youngify(self):
        young = Array([
            Array([2, 3, 14, 16]),
            Array([4, 8, math.inf, math.inf]),
            Array([5, 1, math.inf, math.inf]),
            Array([9, math.inf, math.inf, math.inf])
        ])
        youngify(young, 3, 2)
        expected_young = Array([
            Array([1, 3, 14, 16]),
            Array([2, 4, math.inf, math.inf]),
            Array([5, 8, math.inf, math.inf]),
            Array([9, math.inf, math.inf, math.inf])
        ])
        self.assertEqual(expected_young, young)

    def test_young_insert(self):
        young = Array([
            Array([2, 3, 14, 16]),
            Array([4, 8, math.inf, math.inf]),
            Array([5, 12, math.inf, math.inf]),
            Array([9, math.inf, math.inf, math.inf])
        ])
        young_insert(young, 4, 4, 7)
        expected_young = Array([
            Array([2, 3, 7, 16]),
            Array([4, 8, 14, math.inf]),
            Array([5, 12, math.inf, math.inf]),
            Array([9, math.inf, math.inf, math.inf])
        ])
        self.assertEqual(expected_young, young)

    def test_young_sort(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8, 6, 3, 7, 8]
        array = Array(data)
        young_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(expected_array, array)

    def test_young_search_positive(self):
        young = Array([
            Array([2, 3, 14, 16]),
            Array([4, 8, math.inf, math.inf]),
            Array([5, 12, math.inf, math.inf]),
            Array([9, math.inf, math.inf, math.inf])
        ])
        self.assertTrue(young_search(young, 4, 4, 5))

    def test_young_search_negative(self):
        young = Array([
            Array([2, 3, 14, 16]),
            Array([4, 8, math.inf, math.inf]),
            Array([5, 12, math.inf, math.inf]),
            Array([9, math.inf, math.inf, math.inf])
        ])
        self.assertFalse(young_search(young, 4, 4, 7))
