from unittest import TestCase

from chapter08.pr8_2 import bitwise_sort, counting_sort_in_place
from datastructures.array import Array


class Problem8_2Test(TestCase):
    def test_bitwise_sort(self):
        data = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0]
        array = Array(data)
        bitwise_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_counting_sort_in_place(self):
        data = [7, 1, 3, 1, 2, 4, 5, 7, 2, 4, 3]
        array = Array(data)
        counting_sort_in_place(array, 7)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)
