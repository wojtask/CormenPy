import cmath
import math
import random
import string
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.ex8_2_4 import counting_in_range
from chapter08.ex8_3_4 import below_square_sort
from chapter08.ex8_4_4 import unit_circle_sort
from chapter08.pr8_2 import bitwise_sort, counting_sort_in_place
from chapter08.pr8_3 import integers_sort, strings_sort
from chapter08.pr8_4 import jugs_group, jugs_match
from chapter08.pr8_5 import average_sort
from datastructures.array import Array
from datastructures.point_2d import Point2D


def assert_average_sorted(elements, k):
    for i in range(len(elements) - k):
        assert_that(elements[i], is_(less_than_or_equal_to(elements[i + k])))


class Solutions08Test(TestCase):

    def test_counting_in_range(self):
        k = 20
        array, elements = get_random_array(max_value=k)
        a, b = sorted([random.randint(-10, 30), random.randint(-10, 30)])

        actual_count = counting_in_range(array, k, a, b)

        expected_count = len([x for x in elements if a <= x <= b])
        assert_that(actual_count, is_(equal_to(expected_count)))

    def test_below_square_sort(self):
        n = random.randint(1, 20)
        elements = [random.randint(0, n ** 2 - 1) for _ in range(n)]
        array = Array(elements)

        below_square_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_unit_circle_sort(self):
        n = random.randint(1, 20)
        coords = [cmath.rect(random.random(), random.uniform(-math.pi, math.pi)) for _ in range(n)]
        points = [Point2D(coord.real, coord.imag) for coord in coords]
        array = Array(points)

        unit_circle_sort(array)

        expected_array = Array(sorted(points, key=lambda p: p.x ** 2 + p.y ** 2))
        assert_that(array, is_(equal_to(expected_array)))

    def test_bitwise_sort(self):
        array, elements = get_random_array(max_value=1)

        bitwise_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_counting_sort_in_place(self):
        n = random.randint(1, 20)
        k = 20
        elements = [random.randint(1, k) for _ in range(n)]
        array = Array(elements)

        counting_sort_in_place(array, k)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_integers_sort(self):
        size = random.randint(1, 20)
        elements = []
        for _ in range(size):
            sign = random.choice([-1, +1])
            exponent = random.randint(1, 20)
            elements.append(sign * random.randint(10 ** (exponent - 1), 10 ** exponent - 1))
        array = Array(elements)

        integers_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_strings_sort(self):
        size = random.randint(1, 50)
        elements = []
        for _ in range(size):
            string_length = random.randint(0, 10)
            elements.append(''.join(random.choice(string.ascii_lowercase) for _ in range(string_length)))
        array = Array(elements)

        strings_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_jugs_group(self):
        n = random.randint(1, 20)
        red_elements = [random.randrange(1000) for _ in range(n)]
        blue_elements = random.sample(red_elements, n)
        reds_array = Array(red_elements)
        blues_array = Array(blue_elements)

        jugs_group(reds_array, blues_array)

        assert_that(reds_array.elements, contains_inanyorder(*red_elements))
        assert_that(reds_array, is_(equal_to(blues_array)))

    def test_jugs_match(self):
        n = random.randint(1, 20)
        red_elements = [random.randrange(1000) for _ in range(n)]
        blue_elements = random.sample(red_elements, n)
        reds_array = Array(red_elements)
        blues_array = Array(blue_elements)

        jugs_match(reds_array, blues_array, 1, n)

        assert_that(reds_array.elements, contains_inanyorder(*red_elements))
        assert_that(reds_array, is_(equal_to(blues_array)))

    def test_average_sort(self):
        array, elements = get_random_array(min_size=2)
        k = random.randint(1, array.length - 1)

        average_sort(array, k, 1, array.length)

        assert_that(array.elements, contains_inanyorder(*elements))
        assert_average_sorted(array.elements, k)
