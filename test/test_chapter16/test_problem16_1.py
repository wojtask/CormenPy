import io
import math
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.problem16_1 import greedy_make_change, make_change, print_change
from datastructures.array import Array
from util import between


def get_min_change_size_bruteforce(n, d):
    if n == 0:
        return 0
    min_change = math.inf
    for denom in d:
        if denom <= n:
            min_change = min(min_change, 1 + get_min_change_size_bruteforce(n - denom, d))
    return min_change


class TestProblem16_1(TestCase):

    def test_greedy_make_change(self):
        n = random.randint(1, 20)
        d = Array(1, 2, 5, 10, 20, 50)

        actual_change = greedy_make_change(n)

        expected_change_size = get_min_change_size_bruteforce(n, d)
        actual_change_sum = sum(actual_change[i] * d[i] for i in between(1, d.length))
        assert_that(sum(actual_change), is_(equal_to(expected_change_size)))
        assert_that(actual_change_sum, is_(equal_to(n)))

    def test_make_change(self):
        n = random.randint(1, 20)
        k = random.randint(1, 5)
        d = get_random_array(max_size=k, min_value=2, max_value=20, unique=True)
        d[1] = 1
        captured_output = io.StringIO()

        actual_change, actual_denominators = make_change(n, d)
        with redirect_stdout(captured_output):
            print_change(n, actual_denominators)

        expected_change_size = get_min_change_size_bruteforce(n, d)
        assert_that(actual_change[n], is_(equal_to(expected_change_size)))
        actual_change_denoms = Array(int(d) for d in captured_output.getvalue().splitlines())
        assert_that(sum(actual_change_denoms), is_(equal_to(n)))
        assert_that(actual_change_denoms.length, is_(equal_to(expected_change_size)))
