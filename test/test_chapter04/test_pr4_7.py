from unittest import TestCase

from chapter04.pr4_7 import monge_minimums
from datastructures.array import Array


class Problem4_7Test(TestCase):
    def test_monge_minimums(self):
        monge = Array([
            Array([10, 17, 13, 28, 23]),
            Array([17, 22, 16, 29, 23]),
            Array([24, 28, 22, 34, 24]),
            Array([11, 13, 6, 17, 7]),
            Array([45, 44, 32, 37, 23]),
            Array([36, 33, 19, 21, 6]),
            Array([75, 66, 51, 53, 34])
        ])
        actual_minimums = monge_minimums(monge)
        expected_minimums = Array([10, 16, 22, 6, 23, 6, 34])
        self.assertEqual(actual_minimums, expected_minimums)
