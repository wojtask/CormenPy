import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_3_2 import open_interval_search, open_overlap
from datastructures.array import Array
from datastructures.essential import Interval
from tree_util import get_random_interval_tree, get_binary_search_tree_inorder_nodes


class TestExercise14_3_2(TestCase):

    def test_open_interval_search_random(self):
        tree = get_random_interval_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_intervals = Array(node.int for node in inorder_nodes)
        low_endpoint = random.randint(0, 949)
        high_endpoint = low_endpoint + random.randint(0, 50)
        interval = Interval(low_endpoint, high_endpoint)

        actual_found = open_interval_search(tree, interval)

        if actual_found is not tree.nil:
            assert_that(open_overlap(actual_found.int, interval))
        else:
            for node in inorder_nodes:
                assert_that(open_overlap(node.int, interval), is_(False))
        actual_nodes = get_binary_search_tree_inorder_nodes(tree)
        actual_intervals = Array(node.int for node in actual_nodes)
        assert_that(actual_intervals, is_(equal_to(inorder_intervals)))

    def test_open_interval_search_overlapping_with_no_intervals_in_left_subtree(self):
        tree = get_random_interval_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_intervals = Array(node.int for node in inorder_nodes)
        low_endpoint = tree.root.left.max
        high_endpoint = low_endpoint + random.randint(0, 50)
        interval = Interval(low_endpoint, high_endpoint)

        actual_found = open_interval_search(tree, interval)

        if actual_found is not tree.nil:
            assert_that(open_overlap(actual_found.int, interval))
        else:
            for node in inorder_nodes:
                assert_that(open_overlap(node.int, interval), is_(False))
        actual_nodes = get_binary_search_tree_inorder_nodes(tree)
        actual_intervals = Array(node.int for node in actual_nodes)
        assert_that(actual_intervals, is_(equal_to(inorder_intervals)))
