import random
from unittest import TestCase

from hamcrest import *

from chapter10.textbook10_2 import list_search, list_insert, list_delete, list_delete_, list_search_, list_insert_
from datastructures.list import Node
from list_util import get_random_doubly_linked_list, get_linked_list_keys, assert_prev_next_pointers_consistent, \
    get_random_doubly_linked_list_with_sentinel, get_doubly_linked_list_with_sentinel_keys, \
    assert_prev_next_pointers_consistent_with_sentinel


class TestTextbook10_2(TestCase):

    def test_list_search(self):
        list_, nodes, keys = get_random_doubly_linked_list(min_size=10, max_size=20, max_value=20)
        k = random.randint(1, 20)

        actual_node = list_search(list_, k)

        if k in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(none()))

    def test_list_insert(self):
        list_, nodes, keys = get_random_doubly_linked_list()
        new_key = random.randint(0, 999)
        new_node = Node(new_key)

        list_insert(list_, new_node)

        actual_keys = get_linked_list_keys(list_)
        expected_keys = [new_key] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent(list_)

    def test_list_delete(self):
        list_, nodes, keys = get_random_doubly_linked_list(max_size=5)
        node_idx = random.randrange(len(nodes))
        node_to_delete = nodes[node_idx]

        list_delete(list_, node_to_delete)

        actual_keys = get_linked_list_keys(list_)
        expected_keys = keys[:node_idx] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent(list_)

    def test_list_delete_(self):
        list_, nodes, keys = get_random_doubly_linked_list_with_sentinel(max_size=5)
        node_idx = random.randrange(len(nodes))
        node_to_delete = nodes[node_idx]

        list_delete_(list_, node_to_delete)

        actual_keys = get_doubly_linked_list_with_sentinel_keys(list_)
        expected_keys = keys[:node_idx] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent_with_sentinel(list_)

    def test_list_search_(self):
        list_, nodes, keys = get_random_doubly_linked_list_with_sentinel(min_size=10, max_size=20, max_value=20)
        k = random.randint(1, 20)

        actual_node = list_search_(list_, k)

        if k in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(list_.nil))

    def test_list_insert_(self):
        list_, nodes, keys = get_random_doubly_linked_list_with_sentinel()
        new_key = random.randint(0, 999)
        new_node = Node(new_key)

        list_insert_(list_, new_node)

        actual_keys = get_doubly_linked_list_with_sentinel_keys(list_)
        expected_keys = [new_key] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent_with_sentinel(list_)
