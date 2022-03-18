from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.textbook13_3 import rb_insert
from datastructures.red_black_tree import RedBlackTree, Node
from tree_util import assert_red_black_tree, assert_parent_pointers_consistent, get_binary_search_tree_inorder_keys


class TestTextbook13_3(TestCase):

    def test_rb_insert(self):
        keys = get_random_array()
        tree = RedBlackTree()

        for key in keys:
            rb_insert(tree, Node(key), sentinel=tree.nil)

            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))
