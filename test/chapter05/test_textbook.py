import unittest

from chapter05.textbook import permute_by_sorting, randomize_in_place
from datastructures.array import Array


class ShufflingTest(unittest.TestCase):
    def setUp(self):
        self.array = Array([5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8])

    def test_permute_by_sorting(self):
        self.array = permute_by_sorting(self.array)
        self.assertEqual([1, 2, 3, 5, 6, 6, 6, 7, 7, 8, 8, 9], sorted(self.array.data))

    def test_randomize_in_place(self):
        randomize_in_place(self.array)
        self.assertEqual([1, 2, 3, 5, 6, 6, 6, 7, 7, 8, 8, 9], sorted(self.array.data))
