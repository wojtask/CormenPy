import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_8 import xor_linked_list_search, xor_linked_list_insert, xor_linked_list_delete, \
    xor_linked_list_reverse
from datastructures.list import XORNode
from list_util import get_random_xor_linked_list, get_xor_linked_list_keys


class TestExercise10_2_8(TestCase):

    def test_xor_linked_list_search(self):
        list_, nodes, keys = get_random_xor_linked_list(min_size=10, max_size=20, max_value=20)
        k = random.randint(1, 20)

        actual_node = xor_linked_list_search(list_, k)

        if k in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(none()))

    def test_xor_linked_list_insert(self):
        list_, nodes, keys = get_random_xor_linked_list(min_size=0, max_size=5)
        new_key = random.randint(0, 999)
        new_node = XORNode(new_key, list_)

        xor_linked_list_insert(list_, new_node)

        actual_keys = get_xor_linked_list_keys(list_)
        expected_keys = [new_key] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_xor_linked_list_delete(self):
        list_, nodes, keys = get_random_xor_linked_list(min_size=1, max_size=5)
        node_idx = random.randrange(len(nodes))
        node_to_delete = nodes[node_idx]

        xor_linked_list_delete(list_, node_to_delete)

        actual_keys = get_xor_linked_list_keys(list_)
        expected_keys = keys[:node_idx] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_xor_linked_list_reverse(self):
        list_, nodes, keys = get_random_xor_linked_list(min_size=0, max_size=5)

        xor_linked_list_reverse(list_)

        actual_keys = get_xor_linked_list_keys(list_)
        expected_keys = list(reversed(keys))
        assert_that(actual_keys, is_(equal_to(expected_keys)))
