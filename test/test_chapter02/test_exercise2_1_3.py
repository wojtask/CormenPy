import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_1_3 import linear_search


class TestExercise2_1_3(TestCase):

    def test_linear_search(self):
        array = get_random_array(min_size=10, max_size=20, max_value=20)
        original = copy.deepcopy(array)
        v = random.randint(0, 20)

        actual_index = linear_search(array, v)

        if actual_index:
            assert_that(array[actual_index], is_(equal_to(v)))
        else:
            assert_that(v not in array)
        assert_that(array, is_(equal_to(original)))
