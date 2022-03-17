import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_1 import singly_linked_list_insert, singly_linked_list_delete
from datastructures.array import Array
from datastructures.list import SinglyLinkedNode
from list_util import get_random_singly_linked_list


class TestExercise10_2_1(TestCase):

    def test_singly_linked_list_insert(self):
        linked_list = get_random_singly_linked_list()
        original_keys = linked_list.as_keys_array()
        new_key = random.randint(0, 999)
        new_node = SinglyLinkedNode(new_key)

        singly_linked_list_insert(linked_list, new_node)

        actual_keys = linked_list.as_keys_array()
        expected_keys = Array(new_key) + original_keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_delete(self):
        linked_list = get_random_singly_linked_list(max_size=5)
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()
        node_to_delete = original_nodes.random_choice()

        singly_linked_list_delete(linked_list, node_to_delete)

        actual_keys = linked_list.as_keys_array()
        original_keys.remove(node_to_delete.key)
        assert_that(actual_keys, is_(equal_to(original_keys)))
