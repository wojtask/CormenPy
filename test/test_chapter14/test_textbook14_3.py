import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.textbook14_3 import interval_search, overlap, interval_insert, interval_delete
from datastructures.interval import Interval
from datastructures.red_black_tree import RedBlackTree, IntervalNode
from tree_util import get_binary_search_tree_inorder_keys, get_binary_search_tree_inorder_nodes, \
    get_random_interval_tree, assert_interval_tree


class TestTextbook14_3(TestCase):

    def test_interval_insert(self):
        keys = get_random_array(size=20, max_value=949)
        tree = RedBlackTree(sentinel=IntervalNode(None, None))

        for key in keys:
            interval_insert(tree, IntervalNode(key, Interval(key, key + random.randint(0, 50))))

            assert_interval_tree(tree)

        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_interval_delete(self):
        tree = get_random_interval_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)

        while inorder_nodes:
            node = inorder_nodes.random_choice()
            inorder_keys.remove(node.key)

            interval_delete(tree, node)

            assert_interval_tree(tree)
            actual_keys = get_binary_search_tree_inorder_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*inorder_keys))
            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)

    def test_interval_search(self):
        tree = get_random_interval_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        low_endpoint = random.randint(0, 949)
        high_endpoint = low_endpoint + random.randint(0, 50)
        interval = Interval(low_endpoint, high_endpoint)

        actual_found = interval_search(tree, interval)

        if actual_found is not tree.nil:
            assert_that(overlap(actual_found.int, interval))
        else:
            for node in inorder_nodes:
                assert_that(overlap(node.int, interval), is_(False))
        actual_nodes = get_binary_search_tree_inorder_nodes(tree)
        assert_that(actual_nodes, is_(equal_to(inorder_nodes)))
