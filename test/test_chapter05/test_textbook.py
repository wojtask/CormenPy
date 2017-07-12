from unittest import TestCase

from chapter05.textbook import permute_by_sorting, randomize_in_place
from datastructures.array import Array


class Chapter05Test(TestCase):
    def setUp(self):
        self.data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        self.array = Array(self.data)

    def test_permute_by_sorting(self):
        self.array = permute_by_sorting(self.array)
        expected_sorted_array = Array(sorted(self.data))
        actual_sorted_array = Array(sorted(self.array.data))
        self.assertEqual(actual_sorted_array, expected_sorted_array)

    def test_randomize_in_place(self):
        randomize_in_place(self.array)
        expected_sorted_array = Array(sorted(self.data))
        actual_sorted_array = Array(sorted(self.array.data))
        self.assertEqual(actual_sorted_array, expected_sorted_array)
