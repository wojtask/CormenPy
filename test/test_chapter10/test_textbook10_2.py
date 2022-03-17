import random
from unittest import TestCase

from hamcrest import *

from chapter10.textbook10_2 import list_search, list_insert, list_delete, list_delete_, list_search_, list_insert_
from datastructures.array import Array
from datastructures.list import DoublyLinkedNode
from list_util import get_random_doubly_linked_list, assert_doubly_linked_list_structure_consistent, \
    get_random_doubly_linked_list_with_sentinel, \
    assert_doubly_linked_list_with_sentinel_structure_consistent


class TestTextbook10_2(TestCase):

    def test_list_search(self):
        linked_list = get_random_doubly_linked_list(min_size=10, max_size=20, max_value=20)
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()
        k = random.randint(1, 20)

        actual_node = list_search(linked_list, k)

        if k in original_keys:
            assert_that(actual_node, is_in(original_nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(none()))
        actual_keys = linked_list.as_keys_array()
        assert_that(actual_keys, is_(equal_to(original_keys)))
        assert_doubly_linked_list_structure_consistent(linked_list)

    def test_list_insert(self):
        linked_list = get_random_doubly_linked_list()
        original_keys = linked_list.as_keys_array()
        new_key = random.randint(0, 999)
        new_node = DoublyLinkedNode(new_key)

        list_insert(linked_list, new_node)

        actual_keys = linked_list.as_keys_array()
        expected_keys = Array(new_key, original_keys)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_doubly_linked_list_structure_consistent(linked_list)

    def test_list_delete(self):
        linked_list = get_random_doubly_linked_list(max_size=5)
        original_keys = linked_list.as_keys_array()
        original_nodes = linked_list.as_nodes_array()
        node_to_delete = original_nodes.random_choice()

        list_delete(linked_list, node_to_delete)

        actual_keys = linked_list.as_keys_array()
        original_keys.remove(node_to_delete.key)
        assert_that(actual_keys, is_(equal_to(original_keys)))
        assert_doubly_linked_list_structure_consistent(linked_list)

    def test_list_delete_(self):
        linked_list = get_random_doubly_linked_list_with_sentinel(max_size=5)
        original_keys = linked_list.as_keys_array()
        original_nodes = linked_list.as_nodes_array()
        node_to_delete = original_nodes.random_choice()

        list_delete_(linked_list, node_to_delete)

        actual_keys = linked_list.as_keys_array()
        original_keys.remove(node_to_delete.key)
        assert_that(actual_keys, is_(equal_to(original_keys)))
        assert_doubly_linked_list_with_sentinel_structure_consistent(linked_list)

    def test_list_search_(self):
        linked_list = get_random_doubly_linked_list_with_sentinel(min_size=10, max_size=20, max_value=20)
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()
        k = random.randint(1, 20)

        actual_node = list_search_(linked_list, k)

        if k in original_keys:
            assert_that(actual_node, is_in(original_nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(linked_list.nil))
        actual_keys = linked_list.as_keys_array()
        assert_that(actual_keys, is_(equal_to(original_keys)))
        assert_doubly_linked_list_with_sentinel_structure_consistent(linked_list)

    def test_list_insert_(self):
        linked_list = get_random_doubly_linked_list_with_sentinel()
        original_keys = linked_list.as_keys_array()
        new_key = random.randint(0, 999)
        new_node = DoublyLinkedNode(new_key)

        list_insert_(linked_list, new_node)

        actual_keys = linked_list.as_keys_array()
        expected_keys = Array(new_key) + original_keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_doubly_linked_list_with_sentinel_structure_consistent(linked_list)
