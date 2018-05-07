import io
import itertools
import math
import random
import re
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.problem15_1 import bitonic_tsp, print_bitonic_path
from datastructures.array import Array
from datastructures.point_2d import Point2D
from util import between, rbetween


def get_shortest_bitonic_path_length_bruteforce(points):
    n = points.length
    min_length = math.inf
    for k in between(0, n - 2):
        for right_path in itertools.combinations(between(2, n - 1), k):
            left_path = [x for x in rbetween(n - 1, 2) if x not in right_path]
            path_length = get_path_length(points, [1] + list(right_path) + [n] + left_path + [1])
            min_length = min(min_length, path_length)
    return min_length


def get_path_length(points, path):
    return sum([euclidean_distance(points[path[i - 1]], points[path[i]]) for i in range(1, len(path))])


def get_path_length_from_bitonic_path(path):
    return sum([euclidean_distance(path[i], path[i + 1]) for i in range(-1, len(path) - 1)])


def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


class TestProblem15_1(TestCase):

    def test_bitonic_tsp(self):
        n = random.randint(3, 12)
        xcoords, _ = get_random_array(min_size=n, max_size=n)
        ycoords, _ = get_random_array(min_size=n, max_size=n)
        points = Array([Point2D(x, y) for x, y in zip(xcoords, ycoords)])
        captured_output = io.StringIO()

        actual_path_lengths, optimal_paths = bitonic_tsp(points)
        with redirect_stdout(captured_output):
            print_bitonic_path(points, optimal_paths)

        expected_bitonic_path_length = get_shortest_bitonic_path_length_bruteforce(points)
        assert_that(actual_path_lengths[n, n], is_(close_to(expected_bitonic_path_length, 1e-7)))
        pattern = re.compile('\((\d+), (\d+)\)')
        actual_bitonic_path = [Point2D(int(pattern.match(point).group(1)), int(pattern.match(point).group(2)))
                               for point in captured_output.getvalue().splitlines()]
        assert_that(actual_bitonic_path, has_length(n))
        path_length_from_bitonic_path = get_path_length_from_bitonic_path(actual_bitonic_path)
        assert_that(path_length_from_bitonic_path, is_(close_to(expected_bitonic_path_length, 1e-7)))
