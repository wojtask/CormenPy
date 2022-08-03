import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.problem9_2 import weighted_median_using_sorting, weighted_median
from datastructures.array import Array


def assert_weighted_median(tested_element, elements, weights):
    left_sum = sum(weights[i] for i, x in enumerate(elements, start=1) if x < tested_element)
    right_sum = sum(weights[i] for i, x in enumerate(elements, start=1) if x > tested_element)
    assert_that(left_sum, is_(less_than(.5)))
    assert_that(right_sum, is_(less_than_or_equal_to(.5)))


class TestProblem9_2(TestCase):

    def test_weighted_median_using_sorting(self):
        array = get_random_array(unique=True)
        original_array = copy.deepcopy(array)
        weights_unnormalized = get_random_array(size=array.length)
        sum_of_weights = sum(weights_unnormalized)
        weights = Array(w / sum_of_weights for w in weights_unnormalized)
        original_weights = copy.deepcopy(weights)

        actual_weighted_median = weighted_median_using_sorting(array, weights)

        assert_weighted_median(actual_weighted_median, original_array, original_weights)

    def test_weighted_median(self):
        array = get_random_array(unique=True)
        original_array = copy.deepcopy(array)
        weights_unnormalized = get_random_array(size=array.length)
        sum_of_weights = sum(weights_unnormalized)
        weights = Array(w / sum_of_weights for w in weights_unnormalized)
        original_weights = copy.deepcopy(weights)

        actual_weighted_median = weighted_median(array, weights, 1, array.length)

        assert_weighted_median(actual_weighted_median, original_array, original_weights)
