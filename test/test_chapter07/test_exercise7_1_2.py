import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.exercise7_1_2 import fair_partition


class TestExercise7_1_2(TestCase):

    def test_fair_partition_all_elements_equal(self):
        array = get_random_array(min_value=4, max_value=4)
        original = copy.deepcopy(array)

        pivot = fair_partition(array, 1, array.length)

        expected_pivot = (1 + array.length) // 2
        assert_that(pivot, is_(equal_to(expected_pivot)))
        assert_that(array, is_(equal_to(original)))

    def test_fair_partition_any_array(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        pivot = fair_partition(array, 1, array.length)

        for x in array[:pivot]:
            assert_that(x, is_(less_than_or_equal_to(array[pivot])))
        for x in array[pivot + 1:]:
            assert_that(x, is_(greater_than_or_equal_to(array[pivot])))
        assert_that(array, contains_inanyorder(*original))
