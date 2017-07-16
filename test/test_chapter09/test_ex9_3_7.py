import random
from unittest import TestCase

from chapter09.ex9_3_7 import median_neighbors, median_nearest
from test.test_datastructures.array_util import random_int_array, random_unique_int_array


def get_expected_neighbors(data, k):
    n = len(data)
    median_index = (n - 1) // 2
    left_from_median_index = median_index - (k - 1) // 2
    right_from_median_index = median_index + k // 2
    expected_neighbors = set(sorted(data)[left_from_median_index:right_from_median_index + 1])
    return expected_neighbors


class Ex9_3_7Test(TestCase):
    def test_median_neighbors(self):
        array, data = random_unique_int_array()
        k = random.randint(1, array.length)
        actual_neighbors = median_neighbors(array, k)
        expected_neighbors = get_expected_neighbors(data, k)
        self.assertEqual(expected_neighbors, actual_neighbors)

    def test_median_nearest(self):
        array, data = random_int_array()
        k = random.randint(1, array.length)
        actual_nearest = median_nearest(array, k)
        median_index = (len(data) - 1) // 2
        median = sorted(data)[median_index]
        differences = [(x, abs(x - median)) for x in data]
        expected_nearest = {p[0] for p in sorted(differences, key=lambda p: p[1])[:k]}
        self.assertTrue(actual_nearest, expected_nearest)
