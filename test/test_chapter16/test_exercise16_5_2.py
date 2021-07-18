import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.exercise16_5_2 import tasks_independent
from datastructures.array import Array
from util import between


def tasks_independent_bruteforce(deadlines):
    n = deadlines.length
    N = Array(Array(d for d in deadlines if d <= t).length for t in between(1, n))
    for t in between(1, n):
        if N[t] > t:
            return False
    return True


class TestExercise16_5_2(TestCase):

    def test_tasks_independent(self):
        n = random.randint(1, 10)
        deadlines = get_random_array(max_size=n, min_value=1, max_value=n)

        actual_result = tasks_independent(deadlines, n)

        expected_result = tasks_independent_bruteforce(deadlines)
        assert_that(actual_result, is_(equal_to(expected_result)))
