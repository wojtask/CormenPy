import random
from unittest import TestCase

from hamcrest import *

from chapter12.exercise12_3_1 import recursive_tree_insert_wrapper
from datastructures.binary_tree import BinaryTree, Node
from tree_util import assert_binary_search_tree, assert_parent_pointers_consistent, get_binary_tree_keys


class TestExercise12_3_1(TestCase):

    def test_recursive_tree_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = BinaryTree()

        for key in keys:
            recursive_tree_insert_wrapper(tree, Node(key))

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_tree_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))
