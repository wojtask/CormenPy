from unittest import TestCase

from hamcrest import *

from chapter12.exercise12_2_3 import tree_predecessor
from tree_util import get_random_binary_search_tree, get_binary_search_tree_inorder_keys, \
    get_binary_search_tree_inorder_nodes


class TestExercise12_2_3(TestCase):

    def test_tree_predecessor(self):
        tree = get_random_binary_search_tree()
        original_nodes = get_binary_search_tree_inorder_nodes(tree)
        original_keys = get_binary_search_tree_inorder_keys(tree)
        given_node = original_nodes.random_choice()

        actual_predecessor = tree_predecessor(given_node)

        if actual_predecessor is None:
            assert_that(given_node.key, is_(equal_to(min(original_keys))))
        else:
            assert_that(actual_predecessor, is_in(original_nodes))
            assert_that(actual_predecessor.key, is_(less_than_or_equal_to(given_node.key)))
            for node in original_nodes:
                assert_that(node.key, is_not(all_of(greater_than(actual_predecessor.key), less_than(given_node.key))))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))
