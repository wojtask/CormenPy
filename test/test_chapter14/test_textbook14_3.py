import random
from unittest import TestCase

from hamcrest import *

from chapter14.textbook14_3 import interval_search, overlap, interval_insert, interval_delete
from datastructures.interval import Interval
from datastructures.red_black_tree import RedBlackTree, IntervalNode
from tree_util import assert_parent_pointers_consistent, get_binary_tree_keys, get_binary_tree_nodes, \
    get_random_interval_tree, assert_interval_tree


class TestTextbook14_3(TestCase):

    def test_interval_insert(self):
        keys = [random.randrange(949) for _ in range(20)]
        tree = RedBlackTree(sentinel=IntervalNode(None, None))

        for key in keys:

            interval_insert(tree, IntervalNode(key, Interval(key, key + random.randint(0, 50))))

            assert_interval_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)

        actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_interval_delete(self):
        tree, _, keys = get_random_interval_tree()
        nodes = get_binary_tree_nodes(tree, sentinel=tree.nil)

        while nodes:
            node = random.choice(nodes)
            keys.remove(node.key)

            interval_delete(tree, node)

            assert_interval_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
            assert_that(actual_keys, contains_inanyorder(*keys))
            nodes = get_binary_tree_nodes(tree, sentinel=tree.nil)

    def test_interval_search(self):
        tree, nodes, keys = get_random_interval_tree()
        low_endpoint = random.randint(0, 949)
        high_endpoint = low_endpoint + random.randint(0, 50)
        interval = Interval(low_endpoint, high_endpoint)

        actual_found = interval_search(tree, interval)

        if actual_found is not tree.nil:
            assert_that(overlap(actual_found.int, interval))
        else:
            for node in nodes:
                assert_that(not_(overlap(node.int, interval)))
