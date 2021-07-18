import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_5 import circular_list_insert, circular_list_delete, circular_list_search
from datastructures.array import Array
from datastructures.list import SNode
from list_util import get_random_circular_list, get_circular_list_keys


class TestExercise10_2_5(TestCase):

    def test_circular_list_insert(self):
        list_, nodes, keys = get_random_circular_list(min_size=0, max_size=5)
        new_key = random.randint(0, 999)
        new_node = SNode(new_key)

        circular_list_insert(list_, new_node)

        actual_keys = get_circular_list_keys(list_)
        if nodes:
            expected_keys = Array([keys[1], new_key]) + keys[2:]
        else:
            expected_keys = Array([new_key])
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_circular_list_delete(self):
        list_, nodes, keys = get_random_circular_list(min_size=1, max_size=5)
        node_idx = random.randint(1, nodes.length)
        node_to_delete = nodes[node_idx]

        circular_list_delete(list_, node_to_delete)

        actual_keys = get_circular_list_keys(list_)
        expected_keys = keys[:node_idx - 1] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_circular_list_search(self):
        list_, nodes, keys = get_random_circular_list(min_size=10, max_size=20, max_value=20)
        k = random.randint(1, 20)

        actual_node = circular_list_search(list_, k)

        if k in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(none()))
