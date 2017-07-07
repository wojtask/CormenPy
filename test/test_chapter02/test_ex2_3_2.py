import unittest

from chapter02.ex2_3_2 import merge_
from datastructures.array import Array


class Ex2_3_2Test(unittest.TestCase):
    def test_merge_(self):
        array = Array([3, 5, 6, 8, 8, 9] + [1, 2, 6, 6, 7, 7])
        merge_(array, 1, array.length // 2, array.length)
        expected_array = Array([1, 2, 3, 5, 6, 6, 6, 7, 7, 8, 8, 9])
        self.assertEqual(expected_array, array)
