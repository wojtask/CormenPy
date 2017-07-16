import random
from unittest import TestCase

from chapter08.pr8_5 import average_sort
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Problem8_5Test(TestCase):
    def test_average_sort(self):
        array, data = random_int_array(min_size=2)
        k = random.randint(1, array.length - 1)
        average_sort(array, k, 1, array.length)
        actual_sorted_array = Array(sorted(array.data))
        expected_sorted_array = Array(sorted(data))
        self.assertEqual(actual_sorted_array, expected_sorted_array)
        self._assert_average_sorted(array.data, k)

    def _assert_average_sorted(self, data, k):
        for i in range(len(data) - k):
            self.assertTrue(data[i] <= data[i + k])
