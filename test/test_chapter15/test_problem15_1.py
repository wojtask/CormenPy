import copy
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
from datastructures.essential import Point2D
from util import between, rbetween


def get_shortest_bitonic_path_length_bruteforce(points):
    points.sort(key=lambda p: p.x)
    n = points.length
    min_length = math.inf
    for k in between(0, n - 2):
        for combination in itertools.combinations(between(2, n - 1), k):
            right_path = Array(combination)
            left_path = Array(x for x in rbetween(n - 1, 2) if x not in right_path)
            path_length = get_path_length(points, Array.of(1) + right_path + Array.of(n) + left_path + Array.of(1))
            min_length = min(min_length, path_length)
    return min_length


def get_path_length(points, path):
    return sum(euclidean_distance(points[path[i]], points[path[i + 1]]) for i in between(1, path.length - 1))


def get_path_length_from_bitonic_path(path):
    return sum((euclidean_distance(path[i], path[i + 1]) for i in between(1, path.length - 1)),
               euclidean_distance(path[path.length], path[1]))


def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


class TestProblem15_1(TestCase):

    def test_bitonic_tsp(self):
        n = random.randint(3, 12)
        x_coordinates = get_random_array(size=n)
        y_coordinates = get_random_array(size=n)
        points = Array(Point2D(x, y) for x, y in zip(x_coordinates, y_coordinates))
        original_points = copy.deepcopy(points)
        captured_output = io.StringIO()

        actual_path_lengths, optimal_paths = bitonic_tsp(points)
        with redirect_stdout(captured_output):
            print_bitonic_path(points, optimal_paths)

        expected_bitonic_path_length = get_shortest_bitonic_path_length_bruteforce(original_points)
        assert_that(actual_path_lengths[n, n], is_(close_to(expected_bitonic_path_length, 1e-7)))
        pattern = re.compile(r'\(([+-]?(\d*\.)?\d+), ([+-]?(\d*\.)?\d+)\)')
        actual_bitonic_path = Array(Point2D(float(pattern.match(point).group(1)), float(pattern.match(point).group(3)))
                                    for point in captured_output.getvalue().splitlines())
        assert_that(actual_bitonic_path.length, is_(equal_to(n)))
        path_length_from_bitonic_path = get_path_length_from_bitonic_path(actual_bitonic_path)
        assert_that(path_length_from_bitonic_path, is_(close_to(expected_bitonic_path_length, 1e-7)))
