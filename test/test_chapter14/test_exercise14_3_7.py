import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_3_7 import rectangles_overlap
from chapter14.textbook14_3 import overlap
from datastructures.array import Array
from datastructures.essential import Interval
from util import between


class TestExercise14_3_7(TestCase):

    def test_rectangles_overlap(self):
        n = random.randint(1, 30)
        rectangles = Array()
        for _ in between(1, n):
            low_endpoint_x = random.randint(0, 899)
            low_endpoint_y = random.randint(0, 899)
            high_endpoint_x = low_endpoint_x + random.randint(1, 100)
            high_endpoint_y = low_endpoint_y + random.randint(1, 100)
            rectangles.append((Interval(low_endpoint_x, high_endpoint_x), Interval(low_endpoint_y, high_endpoint_y)))
        rectangles.save_state()

        actual_overlap = rectangles_overlap(rectangles)

        expected_overlap = False
        for i in between(1, n - 1):
            for j in between(i + 1, n):
                if overlap(rectangles[i][0], rectangles[j][0]) and overlap(rectangles[i][1], rectangles[j][1]):
                    expected_overlap = True
        assert_that(actual_overlap, is_(expected_overlap))
        assert_that(rectangles.is_modified(), is_(False))
