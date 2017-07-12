from unittest import TestCase

from chapter04.pr4_2 import find_missing_integer
from datastructures.array import Array


class Problem4_2Test(TestCase):
    def test_find_missing_integer(self):
        array = Array([12, 1, 6, 11, 4, 3, 0, 10, 13, 7, 5, 2, 8])
        missing = find_missing_integer(array)
        self.assertEqual(missing, 9)
