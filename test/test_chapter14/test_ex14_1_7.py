from unittest import TestCase

from chapter14.ex14_1_7 import os_count_inversions
from test.test_datastructures.array_util import random_int_array


def _count_inversions_bruteforce(data):
    inversions = 0
    for i, x in enumerate(data):
        inversions += len([y for y in data[i + 1:] if y < x])
    return inversions


class Ex14_1_7Test(TestCase):
    def test_os_count_inversions(self):
        array, data = random_int_array()
        inversions = os_count_inversions(array)
        expected_inversions = _count_inversions_bruteforce(data)
        self.assertEqual(inversions, expected_inversions)
