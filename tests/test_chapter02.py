import unittest

from chapter02 import *
from data_structures import Array


class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort_singleton(self):
        array = Array([3])
        insertion_sort(array)
        self.assertEqual([3], array.data)

    def test_insertion_sort_array(self):
        array = Array([6, 1, 4, 2, 6, 7, 2])
        insertion_sort(array)
        self.assertEqual([1, 2, 2, 4, 6, 6, 7], array.data)

    def test_nonincreasing_insertion_sort_singleton(self):
        array = Array([3])
        nonincreasing_insertion_sort(array)
        self.assertEqual([3], array.data)

    def test_nonincreasing_insertion_sort_array(self):
        array = Array([6, 1, 4, 2, 6, 7, 2])
        nonincreasing_insertion_sort(array)
        self.assertEqual([7, 6, 6, 4, 2, 2, 1], array.data)
