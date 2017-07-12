from unittest import TestCase

from chapter09.textbook import *
from datastructures.array import Array


class Chapter09Test(TestCase):
    def test_minimum(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        min = minimum(array)
        self.assertEqual(min, 1)

    def test_minimum_maximum_even_size(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        min, max = minimum_maximum(array)
        self.assertEqual(min, 1)
        self.assertEqual(max, 9)

    def test_minimum_maximum_odd_size(self):
        data = [3, 5, 2, 6, 6, 5, 1, 8, 9, 4, 7, 4, 2]
        array = Array(data)
        min, max = minimum_maximum(array)
        self.assertEqual(min, 1)
        self.assertEqual(max, 9)

    def test_randomized_select(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        x = randomized_select(array, 1, array.length, 5)
        self.assertEqual(x, 6)

    def test_select(self):
        data = [5, 9, 7, 9, 2, 8, 10, 6, 8, 6, 15, 12, 6, 3, 1, 7, 7, 8]
        array = Array(data)
        x = select(array, 1, array.length, 5)
        self.assertEqual(x, 6)

    def test_partition_around(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        pivot = partition_around(array, 1, array.length, 3)
        self.assertEqual(pivot, 3)
        expected_array = Array([2, 1, 3, 5, 6, 8, 6, 6, 8, 7, 7, 9])
        self.assertEqual(array, expected_array)
