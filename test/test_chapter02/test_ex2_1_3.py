import random
from unittest import TestCase

from chapter02.ex2_1_3 import linear_search
from test.test_datastructures.array_util import random_int_array


class Ex2_1_3Test(TestCase):
    def test_linear_search(self):
        array, data = random_int_array(min_size=10, max_size=20, max_value=20)
        v = random.randint(0, 20)
        actual_index = linear_search(array, v)
        try:
            expected_index = data.index(v) + 1
            self.assertEqual(actual_index, expected_index)
        except ValueError:
            self.assertIsNone(actual_index)
