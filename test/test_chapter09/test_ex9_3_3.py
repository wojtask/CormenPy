from unittest import TestCase

from chapter09.ex9_3_3 import best_case_quicksort
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Ex9_3_3Test(TestCase):
    def test_best_case_quicksort(self):
        array, data = random_int_array()
        best_case_quicksort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)
