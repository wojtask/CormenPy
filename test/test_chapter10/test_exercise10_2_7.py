from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_7 import singly_linked_list_reverse
from datastructures.array import Array
from list_util import get_random_singly_linked_list


class TestExercise10_2_7(TestCase):

    def test_singly_linked_list_reverse(self):
        linked_list = get_random_singly_linked_list()
        original_keys = linked_list.as_keys_array()

        singly_linked_list_reverse(linked_list)

        actual_keys = linked_list.as_keys_array()
        expected_keys = Array(reversed(original_keys))
        assert_that(actual_keys, is_(equal_to(expected_keys)))
