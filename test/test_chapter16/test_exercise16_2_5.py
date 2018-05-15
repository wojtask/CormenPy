import random
from unittest import TestCase

from hamcrest import *

from chapter16.exercise16_2_5 import points_cover
from datastructures.array import Array


def all_points_covered(cover, points):
    for point in points:
        intervals_covering = [interval for interval in cover if interval.low <= point <= interval.high]
        if len(intervals_covering) == 0:
            return False
    return True


def remove_one_interval_heuristic(cover, points):
    for interval in cover:
        other_cover = set(cover)
        other_cover.remove(interval)
        assert_that(all_points_covered(other_cover, points), is_(False))


class TestExercise16_2_5(TestCase):

    def test_points_cover(self):
        n = random.randint(1, 20)
        points_elements = [random.random() * 20.0 - 10.0 for _ in range(n)]
        points = Array(points_elements)

        actual_intervals = points_cover(points)

        assert_that(all_points_covered(actual_intervals, points_elements), is_(True))
        remove_one_interval_heuristic(actual_intervals, points)
