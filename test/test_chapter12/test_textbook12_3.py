from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter12.textbook12_3 import tree_insert, tree_delete
from datastructures.binary_tree import BinaryTree, Node
from tree_util import assert_binary_search_tree, assert_parent_pointers_consistent, \
    get_binary_search_tree_inorder_keys, get_random_binary_search_tree, get_binary_search_tree_inorder_nodes


class TestTextbook12_3(TestCase):

    def test_tree_insert(self):
        keys = get_random_array()
        tree = BinaryTree()

        for key in keys:
            tree_insert(tree, Node(key))

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_tree_delete(self):
        tree = get_random_binary_search_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)

        while inorder_nodes:
            node = inorder_nodes.random_choice()
            inorder_keys.remove(node.key)

            tree_delete(tree, node)

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_search_tree_inorder_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*inorder_keys))
            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
