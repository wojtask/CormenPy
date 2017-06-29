import unittest

from chapter02.pr2_3 import *
from datastructures.standard_array import StandardArray


class PolynomialEvaluationTest(unittest.TestCase):
    def test_evaluate_polynomial_naively(self):
        coefficients = StandardArray([-1.5, 3.2, 1.6, 3.4, -5.0, 0.0, -1.0, 1.0])
        x = -2.0
        result = naive_polynomial_evaluation(coefficients, x)
        self.assertAlmostEqual(-300.7, result, places=7)
