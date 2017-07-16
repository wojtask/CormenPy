import random
from unittest import TestCase

from chapter02.ex2_3_7 import sum_search
from test.test_datastructures.array_util import random_int_array


def _sum_search_bruteforce(data, sum):
    for i, x in enumerate(data):
        for y in data[i + 1:]:
            if x + y == sum:
                return True
    return False


class Ex2_3_7Test(TestCase):
    def test_sum_search(self):
        array, data = random_int_array(max_value=20)
        sum_to_find = random.randint(0, 40)
        actual_found = sum_search(array, sum_to_find)
        expected_found = _sum_search_bruteforce(data, sum_to_find)
        self.assertEqual(actual_found, expected_found)
