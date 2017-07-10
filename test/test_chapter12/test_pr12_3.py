from unittest import TestCase

from chapter12.pr12_3 import randomly_built_tree_quicksort
from datastructures.array import Array


class Problem12_3Test(TestCase):
    def test_bit_strings_sort(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        randomly_built_tree_quicksort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(expected_array, array)
