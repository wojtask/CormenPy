import copy
from unittest import TestCase

from hamcrest import *

from chapter12.exercise12_2_2 import recursive_tree_minimum, recursive_tree_maximum
from tree_util import get_random_binary_search_tree, get_binary_tree_inorder_keys


class TestExercise12_2_2(TestCase):

    def test_recursive_tree_minimum(self):
        tree, inorder_nodes, inorder_keys = get_random_binary_search_tree()
        original = copy.deepcopy(tree)

        actual_minimum = recursive_tree_minimum(tree.root)

        assert_that(actual_minimum, is_in(inorder_nodes))
        assert_that(actual_minimum.key, is_(equal_to(min(inorder_keys))))
        actual_keys = get_binary_tree_inorder_keys(tree)
        original_keys = get_binary_tree_inorder_keys(original)
        assert_that(actual_keys, is_(equal_to(original_keys)))

    def test_recursive_tree_maximum(self):
        tree, inorder_nodes, inorder_keys = get_random_binary_search_tree()
        original = copy.deepcopy(tree)

        actual_maximum = recursive_tree_maximum(tree.root)

        assert_that(actual_maximum, is_in(inorder_nodes))
        assert_that(actual_maximum.key, is_(equal_to(max(inorder_keys))))
        actual_keys = get_binary_tree_inorder_keys(tree)
        original_keys = get_binary_tree_inorder_keys(original)
        assert_that(actual_keys, is_(equal_to(original_keys)))
