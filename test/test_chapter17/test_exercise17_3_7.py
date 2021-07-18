import random
from unittest import TestCase

from hamcrest import *

from chapter17.exercise17_3_7 import dlh_insert, delete_larger_half
from datastructures.list import Node
from list_util import get_random_doubly_linked_list, get_linked_list_keys, assert_prev_next_pointers_consistent


class TestExercise17_3_7(TestCase):

    def test_dlh_insert(self):
        S, _, keys = get_random_doubly_linked_list()
        new_key = random.randint(0, 999)
        new_node = Node(new_key)

        dlh_insert(S, new_node)

        actual_keys = get_linked_list_keys(S)
        assert_that(actual_keys, contains_exactly(new_key, *keys))
        assert_prev_next_pointers_consistent(S)

    def test_delete_larger_half(self):
        S, _, keys = get_random_doubly_linked_list(max_value=10)

        delete_larger_half(S)

        actual_keys = get_linked_list_keys(S)
        expected_keys = keys.sort()[:keys.length // 2]
        assert_that(actual_keys, contains_inanyorder(*expected_keys))
        assert_prev_next_pointers_consistent(S)
