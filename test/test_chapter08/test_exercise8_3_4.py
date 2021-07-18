import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.exercise8_3_4 import below_square_sort


class TestExercise8_3_4(TestCase):

    def test_below_square_sort(self):
        n = random.randint(1, 20)
        array = get_random_array(size=n, max_value=n ** 2 - 1)
        original = copy.deepcopy(array)

        below_square_sort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
