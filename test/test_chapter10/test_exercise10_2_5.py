import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_5 import circular_list_insert, circular_list_delete, circular_list_search
from datastructures.array import Array
from datastructures.list import SinglyLinkedNode
from list_util import get_random_circular_singly_linked_list


class TestExercise10_2_5(TestCase):

    def test_circular_list_insert(self):
        linked_list = get_random_circular_singly_linked_list(min_size=0, max_size=5)
        original_keys = linked_list.as_keys_array()
        new_key = random.randint(0, 999)
        new_node = SinglyLinkedNode(new_key)

        circular_list_insert(linked_list, new_node)

        actual_keys = linked_list.as_keys_array()
        if original_keys.length > 0:
            expected_keys = Array.of(original_keys[1], new_key) + original_keys[2:]
        else:
            expected_keys = Array.of(new_key)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_circular_list_delete(self):
        linked_list = get_random_circular_singly_linked_list(min_size=1, max_size=5)
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()
        node_to_delete = original_nodes.random_choice()

        circular_list_delete(linked_list, node_to_delete)

        actual_keys = linked_list.as_keys_array()
        original_keys.remove(node_to_delete.key)
        assert_that(actual_keys, is_(equal_to(original_keys)))

    def test_circular_list_search(self):
        linked_list = get_random_circular_singly_linked_list(min_size=10, max_size=20, max_value=20)
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()
        k = random.randint(1, 20)

        actual_node = circular_list_search(linked_list, k)

        if k in original_keys:
            assert_that(actual_node, is_in(original_nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(none()))
        actual_keys = linked_list.as_keys_array()
        assert_that(actual_keys, is_(equal_to(original_keys)))
