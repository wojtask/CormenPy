from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.problem13_3 import avl_insert_wrapper
from datastructures.avl_tree import AVLTree, Node
from tree_util import assert_avl_tree, assert_parent_pointers_consistent, get_binary_tree_inorder_keys


class TestProblem13_3(TestCase):

    def test_avl_insert(self):
        keys = get_random_array(min_size=1, max_size=20)
        tree = AVLTree()

        for key in keys:
            avl_insert_wrapper(tree, Node(key))

            assert_avl_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))
