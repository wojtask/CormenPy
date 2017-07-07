import unittest

from chapter08.ex8_4_4 import unit_circle_sort
from datastructures.array import Array


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ex8_4_4Test(unittest.TestCase):
    def test_unit_circle_sort(self):
        data = [
            Point2D(.15, .79),
            Point2D(.92, .16),
            Point2D(.56, .06),
            Point2D(.25, .33),
            Point2D(.66, .15),
            Point2D(.23, .81),
            Point2D(.69, .72),
            Point2D(.2, .37),
            Point2D(.45, .88),
            Point2D(.7, .07),
            Point2D(.39, .55),
            Point2D(.99, .04),
            Point2D(.3, .49),
            Point2D(.01, .68),
            Point2D(.33, .08),
            Point2D(.91, .4)
        ]
        array = Array(data)
        unit_circle_sort(array)
        expected_sorted_array = Array(sorted(data, key=lambda p: p.x ** 2 + p.y ** 2))
        self.assertEqual(expected_sorted_array, array)
