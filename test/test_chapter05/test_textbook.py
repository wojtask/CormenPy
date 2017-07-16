from unittest import TestCase

from chapter05.textbook import permute_by_sorting, randomize_in_place
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Chapter05Test(TestCase):
    def test_permute_by_sorting(self):
        array, data = random_int_array()
        array = permute_by_sorting(array)
        sorted_expected_array = Array(sorted(data))
        sorted_actual_array = Array(sorted(array.data))
        self.assertEqual(sorted_actual_array, sorted_expected_array)

    def test_randomize_in_place(self):
        array, data = random_int_array()
        randomize_in_place(array)
        sorted_expected_array = Array(sorted(data))
        sorted_actual_array = Array(sorted(array.data))
        self.assertEqual(sorted_actual_array, sorted_expected_array)
