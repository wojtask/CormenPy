import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.exercise9_3_6 import quantiles
from datastructures.array import Array
from util import between, ceildiv


def assert_quantiles(a_set, k, elements):
    quantiles_count = len(a_set)
    sorted_elements = elements.sort()
    quantiles_indexes = Array(sorted_elements.index(quantile) for quantile in a_set).sort()
    assert_valid_subarray_length(elements.length, k, quantiles_indexes[1] - 1)
    for i in between(2, quantiles_count):
        assert_valid_subarray_length(elements.length, k, quantiles_indexes[i] - quantiles_indexes[i - 1] - 1)


def assert_valid_subarray_length(n, k, subarray_length):
    expected_low_subarray_length = (n - (k - 1)) // k
    expected_high_subarray_length = ceildiv(n - (k - 1), k)
    assert_that(subarray_length,
                any_of(equal_to(expected_low_subarray_length), equal_to(expected_high_subarray_length)))


class TestExercise9_3_6(TestCase):

    def test_quantiles(self):
        array = get_random_array(unique=True)
        original = copy.deepcopy(array)
        k = random.randint(1, array.length + 1)

        actual_quantiles = quantiles(array, 1, array.length, k)

        assert_that(actual_quantiles, has_length(k - 1))
        if k > 1:
            assert_quantiles(actual_quantiles, k, original)
