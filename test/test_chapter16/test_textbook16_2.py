import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.textbook16_2 import fractional_knapsack
from datastructures.array import Array
from util import between


def part_item_value(item_partial_weight, item_total_weight, item_value):
    return item_partial_weight / item_total_weight * item_value


def fractional_knapsack_heuristic(w, v, W, i=1):
    if i == w.length:
        return part_item_value(min(w[i], W), w[i], v[i])
    value_no_item = fractional_knapsack_heuristic(w, v, W, i + 1)
    value_half_item = part_item_value(min(w[i] // 2, W), w[i], v[i]) + \
        fractional_knapsack_heuristic(w, v, W - min(w[i] // 2, W), i + 1)
    value_full_item = part_item_value(min(w[i], W), w[i], v[i]) + \
        fractional_knapsack_heuristic(w, v, W - min(w[i], W), i + 1)
    return max(value_no_item, value_half_item, value_full_item)


class TestTextbook16_2(TestCase):

    def test_fractional_knapsack(self):
        n = random.randint(1, 10)
        weights, weights_list = get_random_array(min_size=n, max_size=n)
        values, values_list = get_random_array(min_size=n, max_size=n)
        max_weight = random.randint(1, n * 1000)

        actual_knapsack = fractional_knapsack(weights, values, max_weight)

        assert_that(sum(actual_knapsack), is_(less_than_or_equal_to(max_weight)))
        actual_knapsack_value = sum([part_item_value(actual_knapsack[i], weights[i], values[i]) for i in between(1, n)])
        knapsack_value_bound = fractional_knapsack_heuristic(Array(weights_list), Array(values_list), max_weight)
        assert_that(actual_knapsack_value, is_(greater_than_or_equal_to(knapsack_value_bound)))
