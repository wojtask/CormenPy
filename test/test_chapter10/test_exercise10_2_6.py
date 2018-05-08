from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_6 import circular_lists_union
from list_util import get_random_circular_list, get_circular_list_keys


class TestExercise10_2_6(TestCase):

    def test_circular_lists_union(self):
        list1, _, keys1 = get_random_circular_list()
        list2, _, keys2 = get_random_circular_list()

        actual_union = circular_lists_union(list1, list2)

        actual_keys = get_circular_list_keys(actual_union)
        expected_keys = keys1 + keys2
        assert_that(actual_keys, contains_inanyorder(*expected_keys))
