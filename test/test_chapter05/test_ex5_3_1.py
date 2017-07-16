from unittest import TestCase

from chapter05.ex5_3_1 import randomize_in_place_
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Ex5_3_1Test(TestCase):
    def test_randomize_in_place_(self):
        array, data = random_int_array()
        randomize_in_place_(array)
        expected_sorted_array = Array(sorted(data))
        actual_sorted_array = Array(sorted(array.data))
        self.assertEqual(actual_sorted_array, expected_sorted_array)
