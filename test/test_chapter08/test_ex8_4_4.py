import cmath
import math
import random
from unittest import TestCase

from chapter08.ex8_4_4 import unit_circle_sort
from datastructures.array import Array
from datastructures.point_2d import Point2D


class Ex8_4_4Test(TestCase):
    def test_unit_circle_sort(self):
        n = random.randint(0, 20)
        coords = [cmath.rect(random.random(), random.uniform(-math.pi, math.pi)) for _ in range(n)]
        data = [Point2D(coord.real, coord.imag) for coord in coords]
        array = Array(data)
        unit_circle_sort(array)
        expected_sorted_array = Array(sorted(data, key=lambda p: p.x ** 2 + p.y ** 2))
        self.assertEqual(array, expected_sorted_array)
