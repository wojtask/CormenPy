import math
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.exercise14_3_6 import min_gap_insert, min_gap_search, min_gap_delete, min_gap
from datastructures.red_black_tree import RedBlackTree, MinGapNode
from tree_util import get_binary_search_tree_inorder_nodes


def get_expected_min_gap(keys):
    expected_min_gap = math.inf
    for key1 in keys:
        for key2 in keys:
            if key1 != key2:
                expected_min_gap = min(expected_min_gap, abs(key1 - key2))
    return expected_min_gap


class TestExercise14_3_6(TestCase):

    def test_min_gap_tree(self):
        keys = get_random_array(unique=True)
        tree = RedBlackTree(sentinel=MinGapNode(None))

        for key in keys:
            min_gap_insert(tree, MinGapNode(key))

        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)

        while inorder_nodes:
            node = inorder_nodes.random_choice()
            key = node.key
            keys.remove(key)

            actual_found = min_gap_search(tree, key)
            assert_that(actual_found.key, is_(equal_to(key)))

            min_gap_delete(tree, node)

            actual_found = min_gap_search(tree, key)
            assert_that(actual_found, is_(tree.nil))

            actual_min_gap = min_gap(tree)

            expected_min_gap = get_expected_min_gap(keys)
            assert_that(actual_min_gap, is_(equal_to(expected_min_gap)))
            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
