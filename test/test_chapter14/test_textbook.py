import random
from unittest import TestCase

from hamcrest import *

from chapter14.textbook import os_insert, os_delete, os_select, os_rank, interval_search, overlap
from datastructures.interval import Interval
from datastructures.red_black_tree import RedBlackTree, OSNode
from tree_util import assert_parent_pointers_consistent, get_binary_tree_keys, assert_os_tree, get_random_os_tree, \
    get_binary_tree_nodes, get_random_interval_tree


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

    def test_interval_search(self):
        tree, nodes, keys = get_random_interval_tree()
        low_endpoint = random.randint(0, 949)
        high_endpoint = low_endpoint + random.randint(0, 50)
        endpoints = [low_endpoint, high_endpoint]
        interval = Interval(min(endpoints), max(endpoints))

        actual_found = interval_search(tree, interval)

        if actual_found is not tree.nil:
            assert_that(overlap(actual_found.int, interval))
        else:
            for node in nodes:
                assert_that(not_(overlap(node.int, interval)))
