import io
import random
import re
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.exercise16_2_3 import greedy_knapsack
from datastructures.array import Array
from test_chapter16.test_exercise16_2_2 import knapsack_bruteforce, items_total_value


class TestExercise16_2_3(TestCase):

    def test_greedy_knapsack(self):
        n = random.randint(1, 15)
        weights = get_random_array(size=n).sort()
        values = get_random_array(size=n).sort(reverse=True)
        max_weight = random.randint(1, n * 200)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            actual_knapsack_value = greedy_knapsack(weights, values, max_weight)

        expected_knapsack_value = knapsack_bruteforce(weights, values, max_weight)
        assert_that(actual_knapsack_value, is_(equal_to(expected_knapsack_value)))
        actual_items = Array(
            int(re.search(r'a(\d+)', item).group(1)) for item in captured_output.getvalue().splitlines())
        actual_knapsack_value_from_items = items_total_value(actual_items, values)
        assert_that(actual_knapsack_value_from_items, is_(equal_to(expected_knapsack_value)))
