import random
from unittest import TestCase

from hamcrest import *
from numpy.polynomial import polynomial

from chapter02.textbook_problem2_3 import horner
from datastructures.array import Array
from util import between


class TestTextbookProblem2_3(TestCase):

    def test_horner(self):
        n = random.randint(1, 20)
        coefficients = Array((random.uniform(-2.0, 2.0) for _ in between(1, n)), start=0)
        x = random.uniform(-2.0, 2.0)

        actual_result = horner(coefficients, x)

        expected_result = float(polynomial.polyval(x, coefficients))
        assert_that(actual_result, is_(close_to(expected_result, 1e-7)))
        assert_that(coefficients.is_modified(), is_(False))
