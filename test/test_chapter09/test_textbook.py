import unittest

from chapter09.textbook import *
from datastructures.array import Array


class Chapter09Test(unittest.TestCase):
    def test_minimum(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        min = minimum(array)
        self.assertEqual(1, min)

    def test_minimum_maximum_even_size(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        min, max = minimum_maximum(array)
        self.assertEqual(1, min)
        self.assertEqual(9, max)

    def test_minimum_maximum_odd_size(self):
        data = [3, 5, 2, 6, 6, 5, 1, 8, 9, 4, 7, 4, 2]
        array = Array(data)
        min, max = minimum_maximum(array)
        self.assertEqual(1, min)
        self.assertEqual(9, max)

    def test_randomized_select(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        x = randomized_select(array, 1, array.length, 5)
        self.assertEqual(6, x)

    def test_select(self):
        data = [5, 9, 7, 9, 2, 8, 10, 6, 8, 6, 15, 12, 6, 3, 1, 7, 7, 8]
        array = Array(data)
        x = select(array, 1, array.length, 5)
        self.assertEqual(6, x)

    def test_partition_around(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        pivot = partition_around(array, 1, array.length, 3)
        self.assertEqual(3, pivot)
        expected_array = Array([2, 1, 3, 5, 6, 8, 6, 6, 8, 7, 7, 9])
        self.assertEqual(expected_array, array)
