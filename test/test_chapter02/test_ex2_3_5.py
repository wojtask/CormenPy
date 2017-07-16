import random
from unittest import TestCase

from chapter02.ex2_3_5 import recursive_binary_search, iterative_binary_search
from datastructures.array import Array


class Ex2_3_5Test(TestCase):
    def test_recursive_binary_search(self):
        n = random.randint(1, 20)
        data = sorted([random.randrange(20) for _ in range(n)])
        array = Array(data)
        v = random.randint(1, 20)
        actual_index = recursive_binary_search(array, v, 1, n)
        expected_indexes = [i + 1 for i, x in enumerate(data) if x == v]
        if expected_indexes:
            self.assertIn(actual_index, expected_indexes)
        else:
            self.assertIsNone(actual_index)

    def test_iterative_binary_search(self):
        n = random.randint(1, 20)
        data = sorted([random.randrange(20) for _ in range(n)])
        array = Array(data)
        v = random.randint(1, 20)
        actual_index = iterative_binary_search(array, v)
        expected_indexes = [i + 1 for i, x in enumerate(data) if x == v]
        if expected_indexes:
            self.assertIn(actual_index, expected_indexes)
        else:
            self.assertIsNone(actual_index)
