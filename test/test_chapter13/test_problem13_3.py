from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.problem13_3 import avl_insert_wrapper
from datastructures.binary_tree import AVLNode, BinaryTree
from tree_util import assert_avl_tree, assert_parent_pointers_consistent, get_binary_search_tree_inorder_keys


class TestProblem13_3(TestCase):

    def test_avl_insert(self):
        keys = get_random_array()
        tree = BinaryTree()

        for key in keys:
            avl_insert_wrapper(tree, AVLNode(key))

            assert_avl_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))
