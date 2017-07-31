import random
from unittest import TestCase

from hamcrest import *

from chapter04.pr4_2 import missing_integer
from chapter04.pr4_7 import monge_minimums
from datastructures.array import Array
from datastructures.matrix import Matrix


def random_monge_array(m, n):
    elements = [[random.randrange(1000) for _ in range(n)]]  # the first row
    for i in range(1, m):
        row = [random.randrange(1000)]  # the first element in next row can be anything
        for j in range(1, n):
            upper_bound = row[j - 1] + elements[i - 1][j] - elements[i - 1][j - 1]  # but later ones should be bounded
            row.append(random.randrange(upper_bound - 100, upper_bound + 1))
        elements.append(row)
    return elements


class Solutions04Test(TestCase):

    def test_missing_integer(self):
        n = random.randint(1, 20)
        elements = random.sample(range(n), n - 1)
        array = Array(elements)

        actual_missing = missing_integer(array)

        expected_missing = [x for x in range(n) if x not in elements][0]
        assert_that(actual_missing, is_(equal_to(expected_missing)))

    def test_monge_minimums(self):
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        monge_elements = random_monge_array(m, n)
        monge_array = Matrix(monge_elements)

        actual_minimums = monge_minimums(monge_array)

        expected_minimums = Array([min(row) for row in monge_elements])
        assert_that(actual_minimums, is_(equal_to(expected_minimums)))
