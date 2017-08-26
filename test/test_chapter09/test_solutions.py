import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array, get_random_unique_array
from chapter09.ex9_2_3 import iterative_randomized_select
from chapter09.ex9_3_3 import best_case_quicksort
from chapter09.ex9_3_5 import randomized_blackbox_select
from chapter09.ex9_3_6 import quantiles
from chapter09.ex9_3_7 import median_neighbors, median_nearest
from chapter09.ex9_3_8 import two_arrays_median
from chapter09.pr9_2 import weighted_median_using_sorting, weighted_median, post_office_manhattan
from chapter09.pr9_3 import small_order_select
from datastructures.array import Array
from datastructures.point_2d import Point2D


def assert_quantiles(actual_quantiles, elements):
    quantiles_count = len(actual_quantiles)
    sorted_elements = sorted(elements)
    quantiles_indexes = sorted([sorted_elements.index(quantile) for quantile in actual_quantiles])
    subarray_lengths = {quantiles_indexes[0]}
    for i in range(1, quantiles_count):
        subarray_lengths.add(quantiles_indexes[i] - quantiles_indexes[i - 1] - 1)
    # the subarrays can differ at most 1 so their lengths can be one of 2 possible values
    assert_that(subarray_lengths, has_length(less_than_or_equal_to(2)))


def get_expected_neighbors(elements, k):
    n = len(elements)
    median_index = (n - 1) // 2
    left_from_median_index = median_index - (k - 1) // 2
    right_from_median_index = median_index + k // 2
    expected_neighbors = set(sorted(elements)[left_from_median_index:right_from_median_index + 1])
    return expected_neighbors


def assert_weighted_median(actual_weighted_median, elements, weights):
    left_sum = sum([weights[i] for i, x in enumerate(elements) if x < actual_weighted_median])
    right_sum = sum([weights[i] for i, x in enumerate(elements) if x > actual_weighted_median])
    assert_that(left_sum, is_(less_than(.5)))
    assert_that(right_sum, is_(less_than_or_equal_to(.5)))


def get_weighted_distance_sum(origin, locations, weights):
    return sum(w * (abs(origin.x - loc.x) + abs(origin.y - loc.y)) for loc, w in zip(locations, weights))


class Solutions09Test(TestCase):

    def test_iterative_randomized_select(self):
        array, elements = get_random_array()
        i = random.randint(1, array.length)

        actual_order_statistic = iterative_randomized_select(array, 1, array.length, i)

        expected_order_statistic = sorted(elements)[i - 1]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))

    def test_best_case_quicksort(self):
        array, elements = get_random_array()

        best_case_quicksort(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_randomized_blackbox_select(self):
        array, elements = get_random_array()
        k = random.randint(1, array.length)

        actual_order_statistic = randomized_blackbox_select(array, 1, array.length, k)

        expected_order_statistic = sorted(elements)[k - 1]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))

    def test_quantiles(self):
        array, elements = get_random_unique_array()
        k = random.randint(1, array.length + 1)

        actual_quantiles = quantiles(array, 1, array.length, k)

        assert_that(actual_quantiles, has_length(k - 1))
        if k > 1:
            assert_quantiles(actual_quantiles, elements)

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

    def test_two_arrays_median(self):
        n = random.randint(1, 20)
        elements1 = sorted([random.randrange(1000) for _ in range(n)])
        elements2 = sorted([random.randrange(1000) for _ in range(n)])
        array1 = Array(elements1)
        array2 = Array(elements2)

        actual_median = two_arrays_median(array1, 1, n, array2, 1, n)

        expected_median = sorted(elements1 + elements2)[n - 1]
        assert_that(actual_median, is_(equal_to(expected_median)))

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

    def test_small_order_select(self):
        array, elements = get_random_unique_array(max_size=50)
        i = random.randint(1, array.length // 5 + 1)  # pick small i

        actual_order_statistic = small_order_select(array, i)

        expected_order_statistic = sorted(elements)[i - 1]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))
