import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_unique_array
from chapter09.exercise9_3_6 import quantiles


def assert_quantiles(actual_quantiles, elements):
    quantiles_count = len(actual_quantiles)
    sorted_elements = sorted(elements)
    quantiles_indexes = sorted([sorted_elements.index(quantile) for quantile in actual_quantiles])
    subarray_lengths = {quantiles_indexes[0]}
    for i in range(1, quantiles_count):
        subarray_lengths.add(quantiles_indexes[i] - quantiles_indexes[i - 1] - 1)
    # the subarrays can differ at most 1 so their lengths can be one of 2 possible values
    assert_that(subarray_lengths, has_length(less_than_or_equal_to(2)))


class TestExercise9_3_6(TestCase):

    def test_quantiles(self):
        array, elements = get_random_unique_array()
        k = random.randint(1, array.length + 1)

        actual_quantiles = quantiles(array, 1, array.length, k)

        assert_that(actual_quantiles, has_length(k - 1))
        if k > 1:
            assert_quantiles(actual_quantiles, elements)
