import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.textbook_problem7_5 import median_of_3_partition


class TestTextbookProblem7_5(TestCase):

    def test_median_of_3_partition(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        pivot = median_of_3_partition(array, 1, array.length)

        for x in array[1:pivot]:
            assert_that(x, is_(less_than_or_equal_to(array[pivot])))
        for x in array[pivot + 1:array.length]:
            assert_that(x, is_(greater_than_or_equal_to(array[pivot])))
        assert_that(array, contains_inanyorder(*original))
