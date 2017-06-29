import unittest

from chapter02.ex2_2_2 import selection_sort
from datastructures.array import Array


class SelectionSortTest(unittest.TestCase):
    def test_selection_sort_singleton(self):
        array = Array([3])
        selection_sort(array)
        self.assertEqual([3], array.data)

    def test_selection_sort_array(self):
        array = Array([5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8])
        selection_sort(array)
        self.assertEqual([1, 2, 3, 5, 6, 6, 6, 7, 7, 8, 8, 9], array.data)

