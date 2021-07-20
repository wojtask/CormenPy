import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.exercise8_2_4 import counting_in_range
from datastructures.array import Array


class TestExercise8_2_4(TestCase):

    def test_counting_in_range(self):
        k = 20
        array = get_random_array(max_value=k)
        original = copy.deepcopy(array)
        a, b = random.randint(-10, 30), random.randint(-10, 30)
        if a > b:
            a, b = b, a

        actual_count = counting_in_range(array, k, a, b)

        expected_count = Array(x for x in original if a <= x <= b).length
        assert_that(actual_count, is_(equal_to(expected_count)))
        assert_that(array, is_(equal_to(original)))
