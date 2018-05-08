import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.problem9_2 import weighted_median_using_sorting, weighted_median, post_office_manhattan
from datastructures.array import Array
from datastructures.point_2d import Point2D


def assert_weighted_median(actual_weighted_median, elements, weights):
    left_sum = sum([weights[i] for i, x in enumerate(elements) if x < actual_weighted_median])
    right_sum = sum([weights[i] for i, x in enumerate(elements) if x > actual_weighted_median])
    assert_that(left_sum, is_(less_than(.5)))
    assert_that(right_sum, is_(less_than_or_equal_to(.5)))


def get_weighted_distance_sum(origin, locations, weights):
    return sum(w * (abs(origin.x - loc.x) + abs(origin.y - loc.y)) for loc, w in zip(locations, weights))


class TestProblem9_2(TestCase):

    def test_weighted_median_using_sorting(self):
        array, elements = get_random_array()
        weights_not_normalized = [random.randrange(1000) for _ in range(array.length)]
        weights = [w / sum(weights_not_normalized) for w in weights_not_normalized]
        weights_array = Array(weights)

        actual_weighted_median = weighted_median_using_sorting(array, weights_array)

        assert_weighted_median(actual_weighted_median, elements, weights)

    def test_weighted_median(self):
        array, elements = get_random_array()
        weights_not_normalized = [random.randrange(1000) for _ in range(array.length)]
        weights = [w / sum(weights_not_normalized) for w in weights_not_normalized]
        weights_array = Array(weights)

        actual_weighted_median = weighted_median(array, weights_array, 1, array.length)

        assert_weighted_median(actual_weighted_median, elements, weights)

    def test_post_office_manhattan(self):
        n = random.randint(1, 20)
        elements = [Point2D(random.uniform(-5.0, 5.0), random.uniform(-5.0, 5.0)) for _ in range(n)]
        array = Array(elements)
        weights_not_normalized = [random.randrange(1000) for _ in range(n)]
        weights = [w / sum(weights_not_normalized) for w in weights_not_normalized]
        weights_array = Array(weights)

        actual_post_office = post_office_manhattan(array, weights_array)

        post_office_distance_sum = get_weighted_distance_sum(actual_post_office, elements, weights)
        for point in elements:
            point_distance_sum = get_weighted_distance_sum(point, elements, weights)
            assert_that(post_office_distance_sum, is_(less_than_or_equal_to(point_distance_sum)))
