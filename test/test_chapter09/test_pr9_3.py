import random
from unittest import TestCase

from chapter09.pr9_3 import small_order_select
from datastructures.array import Array
from test.test_datastructures.array_util import random_unique_int_array


class Problem9_3Test(TestCase):
    def test_small_order_select(self):
        array, data = random_unique_int_array()
        k = random.randint(1, array.length // 5 + 1)  # pick small k
        array = Array(data)

        actual_order_statistic = small_order_select(array, k)

        self.assertEqual(actual_order_statistic, sorted(data)[k - 1])
