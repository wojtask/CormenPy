import random
from unittest import TestCase

from chapter14.ex14_1_7 import os_count_inversions
from datastructures.array import Array


def _count_inversions_bruteforce(a):
    inversions = 0
    for i, x in enumerate(a):
        inversions += len([y for y in a[i + 1:] if y < x])
    return inversions


class Ex14_1_7Test(TestCase):
    def test_os_count_inversions(self):
        array = Array(random.sample(range(1000), 10))
        expected_inversions = _count_inversions_bruteforce(array.data)
        inversions = os_count_inversions(array)
        self.assertEqual(inversions, expected_inversions)
