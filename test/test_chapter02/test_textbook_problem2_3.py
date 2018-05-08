import random
from unittest import TestCase

import numpy
from hamcrest import *

from chapter02.textbook_problem2_3 import horner
from datastructures.array import Array


class TestTextbookProblem2_3(TestCase):

    def test_horner(self):
        n = random.randint(1, 20)
        elements = [random.uniform(-2.0, 2.0) for _ in range(n + 1)]
        coefficients = Array(elements, start=0)
        x = random.uniform(-2.0, 2.0)

        actual_result = horner(coefficients, x)

        expected_result = numpy.polyval(list(reversed(elements)), x)
        assert_that(actual_result, is_(close_to(expected_result, 1e-7)))
