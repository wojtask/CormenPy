from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.exercise13_3_6 import parentless_rb_insert
from datastructures.red_black_tree import RedBlackTree, Node
from tree_util import assert_red_black_tree, get_binary_search_tree_inorder_keys


class TestExercise13_3_6(TestCase):

    def test_rb_parentless_insert(self):
        keys = get_random_array()
        tree = RedBlackTree()

        for key in keys:
            parentless_rb_insert(tree, Node(key))

            assert_red_black_tree(tree)

        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))
