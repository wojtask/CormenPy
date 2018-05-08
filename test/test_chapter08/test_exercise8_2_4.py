import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.exercise8_2_4 import counting_in_range


class TestExercise8_2_4(TestCase):

    def test_counting_in_range(self):
        k = 20
        array, elements = get_random_array(max_value=k)
        a, b = sorted([random.randint(-10, 30), random.randint(-10, 30)])

        actual_count = counting_in_range(array, k, a, b)

        expected_count = len([x for x in elements if a <= x <= b])
        assert_that(actual_count, is_(equal_to(expected_count)))
