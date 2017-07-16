from unittest import TestCase

from chapter02.pr2_4 import count_inversions
from test.test_datastructures.array_util import random_int_array


def _count_inversions_bruteforce(data):
    inversions = 0
    for i, x in enumerate(data):
        inversions += len([y for y in data[i + 1:] if y < x])
    return inversions


class Problem4_2Test(TestCase):
    def test_count_inversions(self):
        array, data = random_int_array()
        expected_inversions = _count_inversions_bruteforce(array.data)
        inversions = count_inversions(array, 1, array.length)
        self.assertEqual(inversions, expected_inversions)
