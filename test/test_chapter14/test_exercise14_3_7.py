import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_3_7 import rectangles_overlap
from chapter14.textbook14_3 import overlap
from datastructures.array import Array
from datastructures.interval import Interval


class TestExercise14_3_7(TestCase):

    def test_rectangles_overlap(self):
        n = random.randint(1, 30)
        rectangles = []
        for _ in range(n):
            low_endpoint_x = random.randint(0, 899)
            low_endpoint_y = random.randint(0, 899)
            high_endpoint_x = low_endpoint_x + random.randint(1, 100)
            high_endpoint_y = low_endpoint_y + random.randint(1, 100)
            rectangles.append((Interval(low_endpoint_x, high_endpoint_x), Interval(low_endpoint_y, high_endpoint_y)))
        rectangles_array = Array(rectangles)

        actual_overlap = rectangles_overlap(rectangles_array)

        expected_overlap = False
        for i in range(n):
            for j in range(i + 1, n):
                if overlap(rectangles[i][0], rectangles[j][0]) and overlap(rectangles[i][1], rectangles[j][1]):
                    expected_overlap = True
        assert_that(actual_overlap, is_(expected_overlap))
