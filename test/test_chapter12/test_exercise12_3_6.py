from unittest import TestCase

from hamcrest import *

from chapter12.exercise12_3_6 import fair_tree_delete
from tree_util import get_random_binary_search_tree, get_binary_search_tree_inorder_nodes, assert_binary_search_tree, \
    assert_parent_pointers_consistent, get_binary_search_tree_inorder_keys


class TestExercise12_3_6(TestCase):

    def test_fair_tree_delete(self):
        tree = get_random_binary_search_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)

        while inorder_nodes:
            node = inorder_nodes.random_choice()
            inorder_keys.remove(node.key)

            fair_tree_delete(tree, node)

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_search_tree_inorder_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*inorder_keys))
            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
