import random
from unittest import TestCase

import numpy
from hamcrest import *

from array_util import get_random_array
from chapter02.textbook import insertion_sort, merge_sort, bubble_sort, horner
from datastructures.array import Array


class Textbook02Test(TestCase):

    def test_insertion_sort(self):
        array, elements = get_random_array()

        insertion_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_merge_sort(self):
        array, elements = get_random_array()

        merge_sort(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_bubble_sort(self):
        array, elements = get_random_array()

        bubble_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_horner(self):
        n = random.randint(1, 20)
        elements = [random.uniform(-2.0, 2.0) for _ in range(n + 1)]
        coefficients = Array(elements, start=0)
        x = random.uniform(-2.0, 2.0)

        actual_result = horner(coefficients, x)

        expected_result = numpy.polyval(list(reversed(elements)), x)
        assert_that(actual_result, is_(close_to(expected_result, 1e-7)))
