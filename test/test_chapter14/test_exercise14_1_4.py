from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_1_4 import os_key_rank
from datastructures.array import Array
from tree_util import get_random_os_tree, get_binary_search_tree_inorder_nodes, get_binary_search_tree_inorder_keys


class TestExercise14_1_4(TestCase):

    def test_os_key_rank(self):
        tree = get_random_os_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)
        key_to_find = inorder_keys.random_choice()

        actual_rank = os_key_rank(tree.root, key_to_find)

        expected_ranks = Array(i for i, key in enumerate(inorder_keys, start=1) if key == key_to_find)
        assert_that(actual_rank, is_in(expected_ranks))
        actual_nodes = get_binary_search_tree_inorder_nodes(tree)
        assert_that(actual_nodes, is_(equal_to(inorder_nodes)))
