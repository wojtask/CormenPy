import random
from unittest import TestCase

from hamcrest import *

from chapter13.problem13_3 import avl_insert_wrapper
from datastructures.avl_tree import AVLTree, Node
from tree_util import assert_avl_tree, assert_parent_pointers_consistent, get_binary_tree_keys


class TestProblem13_3(TestCase):

    def test_avl_insert(self):

        keys = [random.randrange(1000) for _ in range(20)]
        tree = AVLTree()

        for key in keys:

            avl_insert_wrapper(tree, Node(key))

            assert_avl_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_tree_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))
