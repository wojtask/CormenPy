import random
from unittest import TestCase

from chapter08.ex8_3_4 import below_square_sort
from datastructures.array import Array


class Ex8_3_4Test(TestCase):
    def test_below_square_sort(self):
        n = random.randint(1, 20)
        data = [random.randint(0, n ** 2 - 1) for _ in range(n)]
        array = Array(data)
        below_square_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)
