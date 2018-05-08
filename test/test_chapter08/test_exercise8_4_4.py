import cmath
import math
import random
from unittest import TestCase

from hamcrest import *

from chapter08.exercise8_4_4 import unit_circle_sort
from datastructures.array import Array
from datastructures.point_2d import Point2D


class TestExercise8_4_4(TestCase):

    def test_unit_circle_sort(self):
        n = random.randint(1, 20)
        coords = [cmath.rect(random.random(), random.uniform(-math.pi, math.pi)) for _ in range(n)]
        points = [Point2D(coord.real, coord.imag) for coord in coords]
        array = Array(points)

        unit_circle_sort(array)

        expected_array = Array(sorted(points, key=lambda p: p.x ** 2 + p.y ** 2))
        assert_that(array, is_(equal_to(expected_array)))
