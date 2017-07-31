import cmath
import math
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.ex8_2_4 import counting_in_range
from chapter08.ex8_3_4 import below_square_sort
from chapter08.ex8_4_4 import unit_circle_sort
from chapter08.pr8_2 import bitwise_sort, counting_sort_in_place
from chapter08.pr8_4 import jugs_group, jugs_match
from chapter08.pr8_5 import average_sort
from datastructures.array import Array
from datastructures.point_2d import Point2D


def assert_average_sorted(data, k):
    for i in range(len(data) - k):
        assert_that(data[i], is_(less_than_or_equal_to(data[i + k])))


class Solutions08Test(TestCase):

    def test_counting_in_range(self):
        k = 20
        array, data = get_random_array(max_value=k)
        a, b = sorted([random.randint(-10, 30), random.randint(-10, 30)])

        actual_count = counting_in_range(array, k, a, b)

        expected_count = len([x for x in data if a <= x <= b])
        assert_that(actual_count, is_(equal_to(expected_count)))

    def test_below_square_sort(self):
        n = random.randint(1, 20)
        data = [random.randint(0, n ** 2 - 1) for _ in range(n)]
        array = Array(data)

        below_square_sort(array)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))

    def test_unit_circle_sort(self):
        n = random.randint(1, 20)
        coords = [cmath.rect(random.random(), random.uniform(-math.pi, math.pi)) for _ in range(n)]
        data = [Point2D(coord.real, coord.imag) for coord in coords]
        array = Array(data)

        unit_circle_sort(array)

        expected_array = Array(sorted(data, key=lambda p: p.x ** 2 + p.y ** 2))
        assert_that(array, is_(equal_to(expected_array)))

    def test_bitwise_sort(self):
        array, data = get_random_array(max_value=1)

        bitwise_sort(array)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))

    def test_counting_sort_in_place(self):
        n = random.randint(1, 20)
        k = 20
        data = [random.randint(1, k) for _ in range(n)]
        array = Array(data)

        counting_sort_in_place(array, k)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))

    def test_jugs_group(self):
        n = random.randint(1, 20)
        reds_data = [random.randrange(1000) for _ in range(n)]
        blues_data = random.sample(reds_data, n)
        reds_array = Array(reds_data)
        blues_array = Array(blues_data)

        jugs_group(reds_array, blues_array)

        assert_that(reds_array.data, contains_inanyorder(*reds_data))
        assert_that(reds_array, is_(equal_to(blues_array)))

    def test_jugs_match(self):
        n = random.randint(1, 20)
        reds_data = [random.randrange(1000) for _ in range(n)]
        blues_data = random.sample(reds_data, n)
        reds_array = Array(reds_data)
        blues_array = Array(blues_data)

        jugs_match(reds_array, blues_array, 1, n)

        assert_that(reds_array.data, contains_inanyorder(*reds_data))
        assert_that(reds_array, is_(equal_to(blues_array)))

    def test_average_sort(self):
        array, data = get_random_array(min_size=2)
        k = random.randint(1, array.length - 1)

        average_sort(array, k, 1, array.length)

        assert_that(array.data, contains_inanyorder(*data))
        assert_average_sorted(array.data, k)
