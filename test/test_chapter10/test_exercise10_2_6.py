from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_6 import list_union
from list_util import get_random_doubly_linked_list_with_sentinel


class TestExercise10_2_6(TestCase):

    def test_list_union(self):
        linked_list1 = get_random_doubly_linked_list_with_sentinel(min_size=0)
        original_keys1 = linked_list1.as_keys_array()
        linked_list2 = get_random_doubly_linked_list_with_sentinel(min_size=0)
        original_keys2 = linked_list2.as_keys_array()

        actual_union = list_union(linked_list1, linked_list2)

        actual_keys = actual_union.as_keys_array()
        expected_keys = original_keys1 + original_keys2
        assert_that(actual_keys, contains_inanyorder(*expected_keys))
