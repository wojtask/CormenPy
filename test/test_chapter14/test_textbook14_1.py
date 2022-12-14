import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.textbook14_1 import os_select, os_rank, os_insert, os_delete
from datastructures.array import Array
from datastructures.red_black_tree import RedBlackTree, OSNode
from tree_util import get_random_os_tree, assert_os_tree, get_binary_search_tree_inorder_keys, \
    get_binary_search_tree_inorder_nodes


class TestTextbook14_1(TestCase):

    def test_os_select(self):
        tree = get_random_os_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)
        i = random.randint(1, inorder_keys.length)

        actual_order_statistic = os_select(tree.root, i)

        assert_that(actual_order_statistic, is_in(inorder_nodes))
        expected_order_statistic = inorder_keys[i]
        assert_that(actual_order_statistic.key, is_(equal_to(expected_order_statistic)))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(inorder_keys)))

    def test_os_rank(self):
        tree = get_random_os_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)
        node_to_find = inorder_nodes.random_choice()

        actual_rank = os_rank(tree, node_to_find)

        expected_ranks = Array(i for i, key in enumerate(inorder_keys, start=1) if key == node_to_find.key)
        assert_that(actual_rank, is_in(expected_ranks))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(inorder_keys)))

    def test_os_insert(self):
        keys = get_random_array(size=20)
        tree = RedBlackTree(sentinel=OSNode(None))

        for i, key in enumerate(keys, start=1):
            os_insert(tree, OSNode(key))

            assert_os_tree(tree)
            assert_that(tree.root.size, is_(equal_to(i)))

        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_os_delete(self):
        tree = get_random_os_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)

        while inorder_nodes:
            node = inorder_nodes.random_choice()
            inorder_keys.remove(node.key)

            os_delete(tree, node)

            assert_os_tree(tree)
            assert_that(tree.root.size, is_(equal_to(inorder_nodes.length - 1)))
            actual_keys = get_binary_search_tree_inorder_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*inorder_keys))
            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
