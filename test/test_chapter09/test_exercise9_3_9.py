import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.exercise9_3_9 import optimal_pipeline_location
from datastructures.array import Array
from datastructures.essential import Point2D


class TestExercise9_3_9(TestCase):

    def test_optimal_pipeline_location(self):
        n = random.randint(1, 20)
        x_coordinates = get_random_array(size=n)
        y_coordinates = get_random_array(size=n, max_value=5)
        wells = Array(Point2D(x, y) for x, y in zip(x_coordinates, y_coordinates))
        original = copy.deepcopy(wells)

        actual_pipeline_location = optimal_pipeline_location(wells)

        expected_pipeline_location = Array(well.y for well in original).sort()[(n + 1) // 2]
        assert_that(actual_pipeline_location, is_(equal_to(expected_pipeline_location)))
