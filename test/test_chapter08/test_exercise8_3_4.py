import random
from unittest import TestCase

from hamcrest import *

from chapter08.exercise8_3_4 import below_square_sort
from datastructures.array import Array


class TestExercise8_3_4(TestCase):

    def test_below_square_sort(self):
        n = random.randint(1, 20)
        elements = [random.randint(0, n ** 2 - 1) for _ in range(n)]
        array = Array(elements)

        below_square_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
