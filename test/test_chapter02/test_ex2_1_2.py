from unittest import TestCase

from chapter02.ex2_1_2 import nonincreasing_insertion_sort
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Ex2_1_2Test(TestCase):
    def test_nonincreasing_insertion_sort(self):
        array, data = random_int_array()
        nonincreasing_insertion_sort(array)
        expected_array = Array(sorted(data, reverse=True))
        self.assertEqual(array, expected_array)
