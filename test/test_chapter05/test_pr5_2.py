import random
from unittest import TestCase

from chapter05.pr5_2 import random_search
from test.test_datastructures.array_util import random_int_array


class Problem5_2Test(TestCase):
    def test_random_search(self):
        array, data = random_int_array(min_size=10, max_size=20, max_value=20)
        v = random.randint(0, 20)
        actual_index = random_search(array, v)
        expected_indexes = [i + 1 for i, x in enumerate(data) if x == v]
        if expected_indexes:
            self.assertIn(actual_index, expected_indexes)
        else:
            self.assertIsNone(actual_index)
