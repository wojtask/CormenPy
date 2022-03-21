import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter04.problem4_7 import monge_minimums
from datastructures.array import Array
from util import between


def random_monge_array(m, n):
    monge = Array.of(get_random_array(size=n, max_value=999))  # the first row
    for i in between(2, m):
        row = Array.of(random.randint(0, 999))  # the first element in the next row can be anything
        for j in between(2, n):
            upper_bound = row[j - 1] + monge[i - 1, j] - monge[i - 1, j - 1]  # but later ones should be bounded
            row.append(random.randint(upper_bound - 100, upper_bound))
        monge.append(row)
    return monge


class TestProblem4_7(TestCase):

    def test_monge_minimums(self):
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        monge_array = random_monge_array(m, n)
        original = copy.deepcopy(monge_array)

        actual_minimums = monge_minimums(monge_array)

        expected_minimums = Array(min(row) for row in monge_array)
        assert_that(actual_minimums, is_(equal_to(expected_minimums)))
        assert_that(monge_array, is_(equal_to(original)))
