import random
from unittest import TestCase

from hamcrest import *

from chapter14.textbook14_1 import os_select, os_rank, os_insert, os_delete
from datastructures.red_black_tree import RedBlackTree, OSNode
from tree_util import get_random_os_tree, assert_os_tree, assert_parent_pointers_consistent, get_binary_tree_keys, \
    get_binary_tree_nodes


class TestTextbook14_1(TestCase):

    def test_os_select(self):
        tree, nodes, keys = get_random_os_tree()
        i = random.randint(1, len(keys))

        actual_order_statistic = os_select(tree.root, i)

        assert_that(actual_order_statistic, is_in(nodes))
        expected_order_statistic = sorted(keys)[i - 1]
        assert_that(actual_order_statistic.key, is_(equal_to(expected_order_statistic)))

    def test_os_rank(self):
        tree, nodes, keys = get_random_os_tree()
        node_to_find = random.choice(nodes)

        actual_rank = os_rank(tree, node_to_find)

        sorted_keys = sorted(keys)
        expected_ranks = [i + 1 for i, key in enumerate(sorted_keys) if key == node_to_find.key]
        assert_that(actual_rank, is_in(expected_ranks))

    def test_os_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = RedBlackTree(sentinel=OSNode(None))

        for i, key in enumerate(keys):

            os_insert(tree, OSNode(key))

            assert_os_tree(tree)
            assert_that(tree.root.size, is_(equal_to(i + 1)))
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)

        actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_os_delete(self):
        tree, _, keys = get_random_os_tree()
        nodes = get_binary_tree_nodes(tree, sentinel=tree.nil)

        while nodes:
            node = random.choice(nodes)
            keys.remove(node.key)

            os_delete(tree, node)

            assert_os_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            assert_that(tree.root.size, is_(equal_to(len(nodes) - 1)))
            actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
            assert_that(actual_keys, contains_inanyorder(*keys))
            nodes = get_binary_tree_nodes(tree, sentinel=tree.nil)
