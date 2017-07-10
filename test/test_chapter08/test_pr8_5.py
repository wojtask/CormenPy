from unittest import TestCase

from chapter08.pr8_5 import average_sort
from datastructures.array import Array
from util import between


class Problem8_5Test(TestCase):
    def test_average_sort(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        k = 6
        average_sort(array, k, 1, array.length)
        expected_sorted_array = Array(sorted(data))
        actual_sorted_array = Array(sorted(data))
        self.assertEqual(expected_sorted_array, actual_sorted_array)
        for i in between(1, array.length - k):
            self.assertTrue(array[i] <= array[i + k])
