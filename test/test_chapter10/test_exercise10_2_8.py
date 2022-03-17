import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_8 import xor_linked_list_search, xor_linked_list_insert, xor_linked_list_delete, \
    xor_linked_list_reverse
from datastructures.array import Array
from datastructures.list import XORNode
from list_util import get_random_xor_linked_list


class TestExercise10_2_8(TestCase):

    def test_xor_linked_list_search(self):
        linked_list = get_random_xor_linked_list(min_size=10, max_size=20, max_value=20)
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()

        k = random.randint(1, 20)

        actual_node = xor_linked_list_search(linked_list, k)

        if k in original_keys:
            assert_that(actual_node, is_in(original_nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(none()))
        actual_keys = linked_list.as_keys_array()
        assert_that(actual_keys, is_(equal_to(original_keys)))

    def test_xor_linked_list_insert(self):
        linked_list = get_random_xor_linked_list(min_size=0, max_size=5)
        original_keys = linked_list.as_keys_array()
        new_key = random.randint(0, 999)
        new_node = XORNode(new_key, linked_list)

        xor_linked_list_insert(linked_list, new_node)

        actual_keys = linked_list.as_keys_array()
        expected_keys = Array(new_key, original_keys)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_xor_linked_list_delete(self):
        linked_list = get_random_xor_linked_list(min_size=1, max_size=5)
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()
        node_to_delete = original_nodes.random_choice()

        xor_linked_list_delete(linked_list, node_to_delete)

        actual_keys = linked_list.as_keys_array()
        original_keys.remove(node_to_delete.key)
        assert_that(actual_keys, is_(equal_to(original_keys)))

    def test_xor_linked_list_reverse(self):
        linked_list = get_random_xor_linked_list(min_size=0, max_size=5)
        original_keys = linked_list.as_keys_array()

        xor_linked_list_reverse(linked_list)

        actual_keys = linked_list.as_keys_array()
        expected_keys = Array(reversed(original_keys))
        assert_that(actual_keys, is_(equal_to(expected_keys)))
