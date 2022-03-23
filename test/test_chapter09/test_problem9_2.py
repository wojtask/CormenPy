import copy
import numpy as np
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.problem9_2 import weighted_median_using_sorting, weighted_median, post_office_manhattan
from datastructures.array import Array
from datastructures.essential import Point2D
from util import between


def assert_weighted_median(tested_element, elements, weights):
    left_sum = sum(weights[i] for i, x in enumerate(elements, start=1) if x < tested_element)
    right_sum = sum(weights[i] for i, x in enumerate(elements, start=1) if x > tested_element)
    assert_that(left_sum, is_(less_than(.5)))
    assert_that(right_sum, is_(less_than_or_equal_to(.5)))


def get_weighted_distance_sum(origin, locations, weights):
    return sum(w * (abs(origin.x - loc.x) + abs(origin.y - loc.y)) for loc, w in zip(locations, weights))


class TestProblem9_2(TestCase):

    def test_weighted_median_using_sorting(self):
        array = get_random_array()
        original_array = copy.deepcopy(array)
        weights_unnormalized = get_random_array(size=array.length)
        sum_of_weights = sum(weights_unnormalized)
        weights = Array(w / sum_of_weights for w in weights_unnormalized)
        original_weights = copy.deepcopy(weights)

        actual_weighted_median = weighted_median_using_sorting(array, weights)

        assert_weighted_median(actual_weighted_median, original_array, original_weights)

    def test_weighted_median(self):
        array = get_random_array()
        original_array = copy.deepcopy(array)
        weights_unnormalized = get_random_array(size=array.length)
        sum_of_weights = sum(weights_unnormalized)
        weights = Array(w / sum_of_weights for w in weights_unnormalized)
        original_weights = copy.deepcopy(weights)

        actual_weighted_median = weighted_median(array, weights, 1, array.length)

        assert_weighted_median(actual_weighted_median, original_array, original_weights)

    def test_post_office_manhattan(self):
        n = random.randint(1, 20)
        array = Array(Point2D(random.uniform(-5.0, 5.0), random.uniform(-5.0, 5.0)) for _ in between(1, n))
        original_array = copy.deepcopy(array)
        weights_unnormalized = get_random_array(size=array.length)
        sum_of_weights = sum(weights_unnormalized)
        weights = Array(w / sum_of_weights for w in weights_unnormalized)
        original_weights = copy.deepcopy(weights)

        actual_post_office = post_office_manhattan(array, weights)

        actual_post_office_distance_sum = get_weighted_distance_sum(actual_post_office, array, weights)
        for x in np.arange(-5.0, 5.0, 0.1):
            for y in np.arange(-5.0, 5.0, 0.1):
                point = Point2D(x, y)
                point_distance_sum = get_weighted_distance_sum(point, original_array, original_weights)
                assert_that(actual_post_office_distance_sum, is_(less_than_or_equal_to(point_distance_sum)))
