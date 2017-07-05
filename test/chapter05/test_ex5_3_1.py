import unittest

from chapter05.ex5_3_1 import randomize_in_place_
from datastructures.array import Array


class RandomizeInPlaceTest(unittest.TestCase):
    def test_randomize_in_place_(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        randomize_in_place_(array)
        self.assertEqual(sorted(data), sorted(array.data))
