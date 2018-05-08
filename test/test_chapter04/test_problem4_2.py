import random
from unittest import TestCase

from hamcrest import *

from chapter04.problem4_2 import missing_integer
from datastructures.array import Array


class TestProblem4_2(TestCase):

    def test_missing_integer(self):
        n = random.randint(1, 20)
        elements = random.sample(range(n), n - 1)
        array = Array(elements)

        actual_missing = missing_integer(array)

        expected_missing = [x for x in range(n) if x not in elements][0]
        assert_that(actual_missing, is_(equal_to(expected_missing)))
