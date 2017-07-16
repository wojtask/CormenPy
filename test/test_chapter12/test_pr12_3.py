from unittest import TestCase

from chapter12.pr12_3 import randomly_built_tree_quicksort
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Problem12_3Test(TestCase):
    def test_randomly_built_tree_quicksort(self):
        array, data = random_int_array()
        randomly_built_tree_quicksort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)
