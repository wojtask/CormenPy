import unittest

from chapter08.ex8_3_4 import below_square_sort
from datastructures.array import Array


class Ex8_3_4Test(unittest.TestCase):
    def test_below_square_sort(self):
        data = [15, 56, 25, 66, 23, 92, 2, 45, 7, 39]
        array = Array(data)
        below_square_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(expected_array, array)
