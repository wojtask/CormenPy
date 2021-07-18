import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_1 import singly_linked_list_insert, singly_linked_list_delete
from datastructures.array import Array
from datastructures.list import SNode
from list_util import get_random_singly_linked_list, get_linked_list_keys


class TestExercise10_2_1(TestCase):

    def test_singly_linked_list_insert(self):
        list_, nodes, keys = get_random_singly_linked_list()
        new_key = random.randint(0, 999)
        new_node = SNode(new_key)

        singly_linked_list_insert(list_, new_node)

        actual_keys = get_linked_list_keys(list_)
        expected_keys = Array([new_key]) + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_delete(self):
        list_, nodes, keys = get_random_singly_linked_list(max_size=5)
        node_idx = random.randint(1, nodes.length)
        node_to_delete = nodes[node_idx]

        singly_linked_list_delete(list_, node_to_delete)

        actual_keys = get_linked_list_keys(list_)
        expected_keys = keys[:node_idx - 1] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))
