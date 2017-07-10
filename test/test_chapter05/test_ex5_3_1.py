from unittest import TestCase

from chapter05.ex5_3_1 import randomize_in_place_
from datastructures.array import Array


class Ex5_3_1Test(TestCase):
    def test_randomize_in_place_(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        randomize_in_place_(array)
        expected_sorted_array = Array(sorted(data))
        actual_sorted_array = Array(sorted(array.data))
        self.assertEqual(expected_sorted_array, actual_sorted_array)
