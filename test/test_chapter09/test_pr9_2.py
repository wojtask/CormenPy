import random
from unittest import TestCase

from chapter09.pr9_2 import weighted_median_using_sorting, weighted_median, post_office_manhattan
from datastructures.array import Array
from datastructures.point_2d import Point2D
from test.test_datastructures.array_util import random_int_array


def _get_weighted_distance_sum(origin, locations, weights):
    return sum(w * (abs(origin.x - loc.x) + abs(origin.y - loc.y)) for loc, w in zip(locations, weights))


class Problem9_2Test(TestCase):
    def test_weighted_median_using_sorting(self):
        array, data = random_int_array()
        weights_not_normalized = [random.randrange(1000) for _ in range(array.length)]
        weights = [w / sum(weights_not_normalized) for w in weights_not_normalized]
        weights_array = Array(weights)

        actual_weighted_median = weighted_median_using_sorting(array, weights_array)

        self.assert_weighted_median(actual_weighted_median, data, weights)

    def assert_weighted_median(self, wm, data, weights):
        left_sum = sum([weights[i] for i, x in enumerate(data) if x < wm])
        right_sum = sum([weights[i] for i, x in enumerate(data) if x > wm])
        self.assertTrue(left_sum < .5)
        self.assertTrue(right_sum <= .5)

    def test_weighted_median(self):
        array, data = random_int_array()
        weights_not_normalized = [random.randrange(1000) for _ in range(array.length)]
        weights = [w / sum(weights_not_normalized) for w in weights_not_normalized]
        weights_array = Array(weights)

        actual_weighted_median = weighted_median(array, weights_array, 1, array.length)

        self.assert_weighted_median(actual_weighted_median, data, weights)

    def test_post_office_manhattan(self):
        n = random.randint(1, 20)
        data = [Point2D(random.uniform(-5.0, 5.0), random.uniform(-5.0, 5.0)) for _ in range(n)]
        array = Array(data)

        weights_not_normalized = [random.randrange(1000) for _ in range(n)]
        weights = [w / sum(weights_not_normalized) for w in weights_not_normalized]
        weights_array = Array(weights)

        actual_post_office = post_office_manhattan(array, weights_array)

        post_office_distance_sum = _get_weighted_distance_sum(actual_post_office, data, weights)
        for point in data:
            point_distance_sum = _get_weighted_distance_sum(point, data, weights)
            self.assertTrue(post_office_distance_sum <= point_distance_sum)
