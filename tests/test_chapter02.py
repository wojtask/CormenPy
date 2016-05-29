import unittest

from chapter02 import insertion_sort
from data_structures import Array


class InsertionSortTest(unittest.TestCase):
    def test_sort_singleton(self):
        array = Array([3])
        insertion_sort(array)
        self.assertEqual([3], array.data)

    def test_sort_array(self):
        array = Array([6, 1, 4, 2, 6, 7, 2])
        insertion_sort(array)
        self.assertEqual([1, 2, 2, 4, 6, 6, 7], array.data)
