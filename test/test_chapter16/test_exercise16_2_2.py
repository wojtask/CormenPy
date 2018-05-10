import io
import itertools
import random
import re
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.exercise16_2_2 import knapsack, print_knapsack
from util import between


def items_total_weight(item_ids, w):
    return sum([w[i] for i in item_ids])


def items_total_value(item_ids, v):
    return sum([v[i] for i in item_ids])


def knapsack_bruteforce(w, v, W):
    max_value = 0
    n = w.length
    for m in between(1, n):
        for item_ids in itertools.combinations(between(1, n), m):
            if items_total_weight(item_ids, w) <= W:
                max_value = max(max_value, items_total_value(item_ids, v))
    return max_value


class TestExercise16_2_2(TestCase):

    def test_knapsack(self):
        n = random.randint(1, 15)
        weights, _ = get_random_array(min_size=n, max_size=n)
        values, _ = get_random_array(min_size=n, max_size=n)
        max_weight = random.randint(1, n * 200)
        captured_output = io.StringIO()

        actual_knapsack = knapsack(weights, values, max_weight)
        with redirect_stdout(captured_output):
            print_knapsack(actual_knapsack, weights, n, max_weight)

        expected_knapsack_value = knapsack_bruteforce(weights, values, max_weight)
        assert_that(actual_knapsack[n, max_weight], is_(equal_to(expected_knapsack_value)))
        actual_items = [int(re.search('a(\d+)', item).group(1)) for item in captured_output.getvalue().splitlines()]
        actual_knapsack_value_from_items = items_total_value(actual_items, values)
        assert_that(actual_knapsack_value_from_items, is_(equal_to(expected_knapsack_value)))
