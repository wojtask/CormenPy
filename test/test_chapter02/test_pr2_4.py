import unittest

from chapter02.pr2_4 import count_inversions
from datastructures.array import Array


class Problem2_4Test(unittest.TestCase):
    def test_count_inversions_singleton(self):
        array = Array([3])
        inversions = count_inversions(array, 1, array.length)
        self.assertEqual(0, inversions)

    def test_count_inversions(self):
        array = Array([5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8])
        inversions = count_inversions(array, 1, array.length)
        self.assertEqual(31, inversions)
