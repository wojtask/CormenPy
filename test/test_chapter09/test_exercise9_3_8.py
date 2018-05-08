import random
from unittest import TestCase

from hamcrest import *

from chapter09.exercise9_3_8 import two_arrays_median
from datastructures.array import Array


class TestExercise9_3_8(TestCase):

    def test_two_arrays_median(self):
        n = random.randint(1, 20)
        elements1 = sorted([random.randrange(1000) for _ in range(n)])
        elements2 = sorted([random.randrange(1000) for _ in range(n)])
        array1 = Array(elements1)
        array2 = Array(elements2)

        actual_median = two_arrays_median(array1, 1, n, array2, 1, n)

        expected_median = sorted(elements1 + elements2)[n - 1]
        assert_that(actual_median, is_(equal_to(expected_median)))
