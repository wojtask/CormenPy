import unittest

from chapter02.ex2_1_2 import nonincreasing_insertion_sort
from datastructures.array import Array


class NonincreasingInsertionSortTest(unittest.TestCase):
    def test_nonincreasing_insertion_sort_singleton(self):
        array = Array([3])
        nonincreasing_insertion_sort(array)
        self.assertEqual([3], array.data)

    def test_nonincreasing_insertion_sort_array(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        nonincreasing_insertion_sort(array)
        self.assertEqual(sorted(data, reverse=True), array.data)
