import copy
import random
from unittest import TestCase

from hamcrest import *
from numpy.polynomial import polynomial

from chapter02.problem2_3 import polynomial_evaluate
from datastructures.array import Array
from util import between


class TestProblem2_3(TestCase):

    def test_polynomial_evaluate(self):
        n = random.randint(1, 20)
        coefficients = Array((random.uniform(-2.0, 2.0) for _ in between(1, n)), start=0)
        original = copy.deepcopy(coefficients)
        x = random.uniform(-2.0, 2.0)

        actual_result = polynomial_evaluate(coefficients, x)

        expected_result = float(polynomial.polyval(x, coefficients))
        assert_that(actual_result, is_(close_to(expected_result, 1e-7)))
        assert_that(coefficients, is_(equal_to(original)))
