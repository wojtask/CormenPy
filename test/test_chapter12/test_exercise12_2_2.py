from unittest import TestCase

from hamcrest import *

from chapter12.exercise12_2_2 import recursive_tree_minimum, recursive_tree_maximum
from tree_util import get_random_binary_search_tree, get_binary_search_tree_inorder_keys, \
    get_binary_search_tree_inorder_nodes


class TestExercise12_2_2(TestCase):

    def test_recursive_tree_minimum(self):
        tree = get_random_binary_search_tree()
        original_nodes = get_binary_search_tree_inorder_nodes(tree)
        original_keys = get_binary_search_tree_inorder_keys(tree)

        actual_minimum = recursive_tree_minimum(tree.root)

        assert_that(actual_minimum, is_in(original_nodes))
        assert_that(actual_minimum.key, is_(equal_to(min(original_keys))))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))

    def test_recursive_tree_maximum(self):
        tree = get_random_binary_search_tree()
        original_nodes = get_binary_search_tree_inorder_nodes(tree)
        original_keys = get_binary_search_tree_inorder_keys(tree)

        actual_maximum = recursive_tree_maximum(tree.root)

        assert_that(actual_maximum, is_in(original_nodes))
        assert_that(actual_maximum.key, is_(equal_to(max(original_keys))))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))
