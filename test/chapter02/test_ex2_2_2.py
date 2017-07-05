import unittest

from chapter02.ex2_2_2 import selection_sort
from datastructures.array import Array


class SelectionSortTest(unittest.TestCase):
    def test_selection_sort_singleton(self):
        array = Array([3])
        selection_sort(array)
        self.assertEqual([3], array.data)

    def test_selection_sort_array(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        selection_sort(array)
        self.assertEqual(sorted(data), array.data)

