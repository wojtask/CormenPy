import random
from unittest import TestCase

from chapter08.pr8_2 import bitwise_sort, counting_sort_in_place
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Problem8_2Test(TestCase):
    def test_bitwise_sort(self):
        array, data = random_int_array(max_value=1)
        bitwise_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_counting_sort_in_place(self):
        n = random.randint(1, 20)
        k = 20
        data = [random.randint(1, k) for _ in range(n)]
        array = Array(data)
        counting_sort_in_place(array, k)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)
