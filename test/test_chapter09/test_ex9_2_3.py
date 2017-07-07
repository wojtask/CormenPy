import unittest

from chapter09.ex9_2_3 import iterative_randomized_select
from datastructures.array import Array


class Ex9_2_3Test(unittest.TestCase):
    def test_iterative_randomized_select(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        x = iterative_randomized_select(array, 1, array.length, 5)
        self.assertEqual(6, x)
