from unittest import TestCase

from chapter09.ex9_3_3 import best_case_quicksort
from datastructures.array import Array


class Ex9_3_3Test(TestCase):
    def test_best_case_quicksort(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        best_case_quicksort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)
