import random
from unittest import TestCase

from hamcrest import *

from chapter13.exercise13_3_6 import parentless_rb_insert
from datastructures.red_black_tree import RedBlackTree, Node
from tree_util import assert_red_black_tree, get_binary_tree_keys


class TestExercise13_3_6(TestCase):

    def test_rb_parentless_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = RedBlackTree()

        for key in keys:

            parentless_rb_insert(tree, Node(key))

            assert_red_black_tree(tree, sentinel=tree.nil)

        actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
        assert_that(actual_keys, contains_inanyorder(*keys))
