import io
import math
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.problem15_2 import break_lines, print_lines


def get_lines_break_minimum_cost_bruteforce(word_lengths, line_capacity, division=None, word_id=2):
    if division is None:
        division = [1]
    n = len(word_lengths)
    min_cost = get_cost_of_lines_break(division, word_lengths, line_capacity)
    while word_id <= n:
        min_cost = min(min_cost, get_lines_break_minimum_cost_bruteforce(
            word_lengths, line_capacity, division + [word_id], word_id + 1))
        word_id += 1
    return min_cost


def get_cost_of_lines_break(division, word_lengths, line_capacity):
    cost = 0
    for i in range(1, len(division)):
        line_length = get_line_length(division[i - 1], division[i] - 1, word_lengths)
        if line_length > line_capacity:
            return math.inf
        cost += (line_capacity - line_length) ** 3
    line_length = get_line_length(division[-1], len(word_lengths), word_lengths)
    if line_length > line_capacity:
        return math.inf
    return cost


def get_line_length(first_word_id, last_word_id, word_lengths):
    return sum([word_lengths[j - 1] for j in range(first_word_id, last_word_id + 1)]) + last_word_id - first_word_id


class TestProblem15_2(TestCase):

    def test_break_lines(self):
        n = random.randint(1, 15)
        line_capacity = random.randint(5, 100)
        word_lengths, _ = get_random_array(min_size=n, max_size=n, min_value=1, max_value=line_capacity)
        captured_output = io.StringIO()

        actual_costs, words_division = break_lines(word_lengths, line_capacity)
        with redirect_stdout(captured_output):
            print_lines(words_division, n)

        expected_cost = get_lines_break_minimum_cost_bruteforce(word_lengths.elements, line_capacity)
        assert_that(actual_costs[n], is_(equal_to(expected_cost)))
        actual_lines_break = [int(first_word) for first_word in captured_output.getvalue().splitlines()]
        actual_cost_of_lines_break = get_cost_of_lines_break(actual_lines_break, word_lengths.elements, line_capacity)
        assert_that(actual_cost_of_lines_break, is_(equal_to(expected_cost)))
