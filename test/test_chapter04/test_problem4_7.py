import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter04.problem4_7 import monge_minimums
from datastructures.array import Array
from datastructures.matrix import Matrix


def random_monge_array(m, n):
    elements = [[random.randrange(1000) for _ in range(n)]]  # the first row
    for i in range(1, m):
        row = [random.randrange(1000)]  # the first element in the next row can be anything
        for j in range(1, n):
            upper_bound = row[j - 1] + elements[i - 1][j] - elements[i - 1][j - 1]  # but later ones should be bounded
            row.append(random.randrange(upper_bound - 100, upper_bound + 1))
        elements.append(row)
    return Matrix(elements)


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
