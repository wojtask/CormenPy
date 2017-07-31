import random
from unittest import TestCase

from hamcrest import *

from chapter14.textbook import os_insert, os_delete, os_select, os_rank
from datastructures.red_black_tree import RedBlackTree, OSNode
from tree_util import assert_parent_pointers_consistent, get_binary_tree_keys, assert_os_tree, \
    get_random_os_tree


class Textbook14Test(TestCase):

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
        tree = RedBlackTree(nil=OSNode(None))

        for key in keys:

            os_insert(tree, OSNode(key))

            assert_os_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)

        actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_os_delete(self):
        tree, nodes, keys = get_random_os_tree()
        random.shuffle(nodes)

        for i, node in enumerate(nodes):
            keys.remove(node.key)

            y = os_delete(tree, node)

            if y is not node:
                # this means that os_delete actually removed the node's successor so we need to swap them in nodes list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_os_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
            assert_that(actual_keys, contains_inanyorder(*keys))
