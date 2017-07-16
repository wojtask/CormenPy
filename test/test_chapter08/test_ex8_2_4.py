import random
from unittest import TestCase

from chapter08.ex8_2_4 import counting_in_range
from test.test_datastructures.array_util import random_int_array


def _count_in_range_bruteforce(data, a, b):
    return len([x for x in data if a <= x <= b])


class Ex8_2_4Test(TestCase):
    def test_counting_in_range(self):
        k = 20
        array, data = random_int_array(max_value=k)
        a, b = sorted([random.randint(-10, 30), random.randint(-10, 30)])
        actual_count = counting_in_range(array, k, a, b)
        expected_count = _count_in_range_bruteforce(data, a, b)
        self.assertEqual(actual_count, expected_count)
