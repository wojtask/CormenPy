import random
from unittest import TestCase

from hamcrest import *

from chapter17.exercise17_3_7 import dlh_insert, delete_larger_half
from datastructures.list import DoublyLinkedNode
from list_util import get_random_doubly_linked_list, assert_doubly_linked_list_structure_consistent


class TestExercise17_3_7(TestCase):

    def test_dlh_insert(self):
        S = get_random_doubly_linked_list()
        original_keys = S.as_keys_array()
        new_key = random.randint(0, 999)
        new_node = DoublyLinkedNode(new_key)

        dlh_insert(S, new_node)

        actual_keys = S.as_keys_array()
        assert_that(actual_keys, contains_exactly(new_key, *original_keys))
        assert_doubly_linked_list_structure_consistent(S)

    def test_delete_larger_half(self):
        S = get_random_doubly_linked_list(max_value=10)
        original_keys = S.as_keys_array()

        delete_larger_half(S)

        actual_keys = S.as_keys_array()
        expected_keys = original_keys.sort()[:original_keys.length // 2]
        assert_that(actual_keys, contains_inanyorder(*expected_keys))
        assert_doubly_linked_list_structure_consistent(S)
