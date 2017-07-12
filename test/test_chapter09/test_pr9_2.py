from unittest import TestCase

from chapter09.pr9_2 import weighted_median_using_sorting, weighted_median, post_office_manhattan
from datastructures.array import Array
from datastructures.point_2d import Point2D


def get_distance_sum(origin, locations):
    return sum(abs(origin.x - loc.x) + abs(origin.y - loc.y) for loc in locations)


class Problem9_2Test(TestCase):
    def test_weighted_median_using_sorting(self):
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        array = Array(data)
        weights = [.05, .05, .1, .2, .02, .1, .03, .05, .3, .1]
        w = Array(weights)
        median = weighted_median_using_sorting(array, w)
        self.assertEqual(median, 5)

    def test_weighted_median(self):
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        array = Array(data)
        weights = [.05, .05, .1, .2, .02, .1, .03, .05, .3, .1]
        w = Array(weights)
        median = weighted_median(array, w, 1, array.length)
        self.assertEqual(median, 5)

    def test_post_office_manhattan(self):
        data = [
            Point2D(1.0, 1.0),
            Point2D(1.0, 3.0),
            Point2D(1.0, 5.0),
            Point2D(3.0, 1.0),
            Point2D(3.0, 5.0),
            Point2D(5.0, 1.0),
            Point2D(5.0, 3.0),
            Point2D(5.0, 5.0)
        ]
        array = Array(data)
        weights = [.1, .1, .2, .02, .2, .3, .05, .03]
        w = Array(weights)
        post_office = post_office_manhattan(array, w)
        post_office_distance_sum = get_distance_sum(post_office, data)
        for point in data:
            point_distance_sum = get_distance_sum(point, data)
            self.assertTrue(post_office_distance_sum <= point_distance_sum)
