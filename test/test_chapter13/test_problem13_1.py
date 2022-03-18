import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.problem13_1 import persistent_tree_insert, persistent_rb_insert, persistent_rb_delete
from datastructures.binary_tree import BinaryTree
from datastructures.red_black_tree import ParentlessNode, RedBlackTree
from tree_util import assert_binary_search_tree, get_binary_search_tree_inorder_keys, assert_red_black_tree, \
    get_random_red_black_tree, \
    get_binary_search_tree_inorder_nodes


def transform_tree_to_parentless_tree(tree):
    parentless_sentinel = ParentlessNode(None)
    tree.root = transform_nodes_to_parentless_nodes(tree.root, tree.nil, parentless_sentinel)
    tree.nil = parentless_sentinel


def transform_nodes_to_parentless_nodes(node, sentinel, parentless_sentinel):
    if node is sentinel:
        return parentless_sentinel
    return ParentlessNode(node.key, data=node.data, color=node.color,
                          left=transform_nodes_to_parentless_nodes(node.left, sentinel, parentless_sentinel),
                          right=transform_nodes_to_parentless_nodes(node.right, sentinel, parentless_sentinel))


class TestProblem13_1(TestCase):

    def test_persistent_tree_insert(self):
        keys = get_random_array(min_size=1, max_size=20)
        tree = BinaryTree()

        for i, key in enumerate(keys, start=1):
            new_tree = persistent_tree_insert(tree, key)

            assert_binary_search_tree(new_tree)
            actual_keys_before_insertion = get_binary_search_tree_inorder_keys(tree)
            actual_keys_after_insertion = get_binary_search_tree_inorder_keys(new_tree)
            assert_that(actual_keys_before_insertion, contains_inanyorder(*keys[:i - 1]))
            assert_that(actual_keys_after_insertion, contains_inanyorder(*keys[:i]))
            tree = new_tree

    def test_persistent_rb_insert(self):
        keys = get_random_array(min_size=1, max_size=20)
        tree = RedBlackTree()

        for i, key in enumerate(keys, start=1):
            new_tree = persistent_rb_insert(tree, ParentlessNode(key))

            assert_red_black_tree(new_tree)
            actual_keys_before_insertion = get_binary_search_tree_inorder_keys(tree)
            actual_keys_after_insertion = get_binary_search_tree_inorder_keys(new_tree)
            assert_that(actual_keys_before_insertion, contains_inanyorder(*keys[:i - 1]))
            assert_that(actual_keys_after_insertion, contains_inanyorder(*keys[:i]))
            tree = new_tree

    def test_persistent_rb_delete(self):
        tree, _, inorder_keys = get_random_red_black_tree()
        transform_tree_to_parentless_tree(tree)
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)

        while inorder_nodes:
            node = inorder_nodes.random_choice()

            new_tree = persistent_rb_delete(tree, node)

            assert_red_black_tree(new_tree)
            actual_keys_before_insertion = get_binary_search_tree_inorder_keys(tree)
            actual_keys_after_insertion = get_binary_search_tree_inorder_keys(new_tree)
            assert_that(actual_keys_before_insertion, contains_inanyorder(*inorder_keys))
            inorder_keys.remove(node.key)
            assert_that(actual_keys_after_insertion, contains_inanyorder(*inorder_keys))
            tree = new_tree
            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
