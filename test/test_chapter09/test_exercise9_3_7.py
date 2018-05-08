import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_unique_array
from chapter09.exercise9_3_7 import median_neighbors, median_nearest


def get_expected_neighbors(elements, k):
    n = len(elements)
    median_index = (n - 1) // 2
    left_from_median_index = median_index - (k - 1) // 2
    right_from_median_index = median_index + k // 2
    expected_neighbors = set(sorted(elements)[left_from_median_index:right_from_median_index + 1])
    return expected_neighbors


class TestExercise9_3_7(TestCase):

    def test_median_neighbors(self):
        array, elements = get_random_unique_array()
        k = random.randint(1, array.length)

        actual_neighbors = median_neighbors(array, k)

        expected_neighbors = get_expected_neighbors(elements, k)
        assert_that(expected_neighbors, is_(equal_to(actual_neighbors)))

    def test_median_nearest(self):
        array, elements = get_random_unique_array(max_value=30)
        k = random.randint(1, array.length)

        actual_nearest = median_nearest(array, k)

        median_index = (len(elements) - 1) // 2
        median = sorted(elements)[median_index]
        distances = [(x, abs(x - median)) for x in elements]
        sorted_distances = sorted(distances, key=lambda p: p[1])
        expected_nearest = {p[0] for p in sorted_distances[:k]}
        # also add (k+1)-th number if its distance to median is equal to one of k elements already taken
        if k < len(elements) and sorted_distances[k][1] == sorted_distances[k - 1][1]:
            expected_nearest |= {sorted_distances[k][0]}

        assert_that(actual_nearest, has_length(k))
        assert_that(actual_nearest.issubset(expected_nearest))
