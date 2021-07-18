import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.exercise16_2_6 import effective_fractional_knapsack
from test_chapter16.test_textbook16_2 import part_item_value, fractional_knapsack_heuristic
from util import between


class TestExercise16_2_6(TestCase):

    def test_effective_fractional_knapsack(self):
        n = random.randint(1, 10)
        weights = get_random_array(size=n)
        values = get_random_array(size=n)
        original_weights = copy.deepcopy(weights)
        original_values = copy.deepcopy(values)
        max_weight = random.randint(1, n * 1000)

        actual_knapsack = effective_fractional_knapsack(weights, values, max_weight)

        assert_that(sum(actual_knapsack), is_(less_than_or_equal_to(max_weight)))
        actual_knapsack_value = sum(part_item_value(actual_knapsack[i], weights[i], values[i]) for i in between(1, n))
        knapsack_value_bound = fractional_knapsack_heuristic(original_weights, original_values, max_weight)
        assert_that(actual_knapsack_value, is_(greater_than_or_equal_to(knapsack_value_bound)))
