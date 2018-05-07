import io
import math
import random
import re
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter15.problem15_6 import checkerboard, print_moves
from datastructures.array import Array
from util import between


def checkerboard_profit(profit, x, y):
    if x[0] != y[0] - 1 or abs(x[1] - y[1]) > 1:
        raise ValueError('invalid argument')
    return profit[x][y[1] - x[1] + 1]


def get_optimal_checkerboard_path_bruteforce(n, p):
    max_profit = -math.inf
    for j in between(1, n):
        max_profit = max(max_profit, get_optimal_checkerboard_subpath_bruteforce((1, j), n, p))
    return max_profit


def get_optimal_checkerboard_subpath_bruteforce(x, n, p):
    if x[0] == n:
        return 0
    y = (x[0] + 1, x[1])
    result = p(x, y) + get_optimal_checkerboard_subpath_bruteforce(y, n, p)
    if x[1] > 1:
        y = (x[0] + 1, x[1] - 1)
        result = max(result, p(x, y) + get_optimal_checkerboard_subpath_bruteforce(y, n, p))
    if x[1] < n:
        y = (x[0] + 1, x[1] + 1)
        result = max(result, p(x, y) + get_optimal_checkerboard_subpath_bruteforce(y, n, p))
    return result


def assert_squares_path(n, lines, profit, max_profit):
    comp = re.compile('\((\d+), (\d+)\)')
    actual_squares_path = [(int(comp.search(line).group(1)), int(comp.search(line).group(2))) for line in lines]
    assert_that(actual_squares_path, has_length(n))
    assert_that(actual_squares_path[0][0], is_(equal_to(1)))
    profit_from_path = 0
    for k in range(1, n):
        profit_from_path += checkerboard_profit(profit, actual_squares_path[k - 1], actual_squares_path[k])
    assert_that(profit_from_path, is_(equal_to(max_profit)))


class TestProblem15_6(TestCase):

    def test_checkerboard(self):
        n = random.randint(1, 8)
        # profit[i, j] contains a triple (a, b, c), where the profit of moving from square of coords (i, j):
        # to square of coords (i+1, j-1) is a, to square of coords (i+1, j) is b, to square of coords (i+1, j+1) is c,
        # where (i, j) means i-th row from the bottom and j-th column from the left
        profit = Array([Array.indexed(1, n) for _ in between(1, n - 1)])
        for i in between(1, n - 1):
            profit[i, 1] = (None, random.randint(-100, 100), random.randint(-100, 100))
            for j in between(2, n - 1):
                profit[i, j] = (random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100))
            profit[i, n] = (random.randint(-100, 100), random.randint(-100, 100), None)
        captured_output = io.StringIO()

        actual_maximum_profit, squares, last_square = checkerboard(n, lambda x, y: checkerboard_profit(profit, x, y))
        with redirect_stdout(captured_output):
            print_moves(squares, n, last_square)

        expected_maximum_profit = \
            get_optimal_checkerboard_path_bruteforce(n, lambda x, y: checkerboard_profit(profit, x, y))
        assert_that(actual_maximum_profit, is_(equal_to(expected_maximum_profit)))
        assert_squares_path(n, captured_output.getvalue().splitlines(), profit, expected_maximum_profit)
