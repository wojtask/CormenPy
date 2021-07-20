import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.exercise9_3_7 import median_neighbors, median_nearest
from datastructures.array import Array


def get_expected_neighbors(elements, k):
    n = elements.length
    median_index = (n + 1) // 2
    left_from_median_index = median_index - (k - 1) // 2
    right_from_median_index = median_index + k // 2
    return set(elements.sort()[left_from_median_index:right_from_median_index])


class TestExercise9_3_7(TestCase):

    def test_median_neighbors(self):
        array = get_random_array(unique=True)
        original = copy.deepcopy(array)
        k = random.randint(1, array.length)

        actual_neighbors = median_neighbors(array, k)

        expected_neighbors = get_expected_neighbors(original, k)
        assert_that(expected_neighbors, is_(equal_to(actual_neighbors)))

    def test_median_nearest(self):
        array = get_random_array(max_value=30, unique=True)
        original = copy.deepcopy(array)
        n = array.length
        k = random.randint(1, n)

        actual_nearest = median_nearest(array, k)

        median = original.sort()[(n + 1) // 2]
        distances = Array((x, abs(x - median)) for x in original)
        sorted_distances = distances.sort(key=lambda p: p[1])
        expected_nearest = {p[0] for p in sorted_distances[:k]}
        # also add (k+1)-th number if its distance to the median is equal to one of the k elements already taken
        if k < n and sorted_distances[k + 1][1] == sorted_distances[k][1]:
            expected_nearest |= {sorted_distances[k + 1][0]}

        assert_that(actual_nearest, has_length(k))
        assert_that(actual_nearest.issubset(expected_nearest))
