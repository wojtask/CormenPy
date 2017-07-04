import unittest

from chapter05.ex5_3_1 import randomize_in_place_
from datastructures.array import Array


class RandomizeInPlaceTest(unittest.TestCase):
    def test_randomize_in_place_(self):
        array = Array([5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8])
        randomize_in_place_(array)
        self.assertEqual([1, 2, 3, 5, 6, 6, 6, 7, 7, 8, 8, 9], sorted(array.data))
