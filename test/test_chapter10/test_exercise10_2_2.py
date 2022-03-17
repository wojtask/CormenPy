import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_2 import singly_linked_list_push, singly_linked_list_pop
from datastructures.array import Array
from list_util import get_random_singly_linked_list


class TestExercise10_2_2(TestCase):

    def test_singly_linked_list_push(self):
        linked_list = get_random_singly_linked_list()
        original_keys = linked_list.as_keys_array()
        x = random.randint(0, 999)

        singly_linked_list_push(linked_list, x)

        actual_keys = linked_list.as_keys_array()
        expected_keys = Array(x) + original_keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_pop(self):
        linked_list = get_random_singly_linked_list(max_size=5)
        original_keys = linked_list.as_keys_array()

        actual_deleted = singly_linked_list_pop(linked_list)

        assert_that(actual_deleted, is_(equal_to(original_keys[1])))
        original_keys.pop(1)
        actual_keys = linked_list.as_keys_array()
        assert_that(actual_keys, is_(equal_to(original_keys)))
