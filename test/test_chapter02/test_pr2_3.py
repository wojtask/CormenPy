import random
from unittest import TestCase

import numpy

from chapter02.pr2_3 import polynomial_evaluate
from datastructures.standard_array import StandardArray


class Problem2_3Test(TestCase):
    def test_naive_polynomial_evaluation(self):
        n = random.randint(1, 20)
        data = [random.uniform(-2.0, 2.0) for _ in range(n + 1)]
        coefficients = StandardArray(data)
        x = random.uniform(-2.0, 2.0)
        expected_result = numpy.polyval(list(reversed(data)), x)
        actual_result = polynomial_evaluate(coefficients, x)
        self.assertAlmostEqual(actual_result, expected_result)
