from unittest import TestCase

from chapter09.pr9_3 import small_order_select
from datastructures.array import Array


class Problem9_3Test(TestCase):
    def test_small_order_select(self):
        data = [5, 12, 1, 0, 13, 12, 0, 10, 9, 1, 4, 3, 16, 15, 19, 6, 11, 20, 2]
        array = Array(data)
        x = small_order_select(array, 3)
        self.assertEqual(x, 1)
