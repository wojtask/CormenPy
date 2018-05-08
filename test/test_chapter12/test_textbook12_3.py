import random
from unittest import TestCase

from hamcrest import *

from chapter12.textbook12_3 import tree_insert, tree_delete
from datastructures.binary_tree import BinaryTree, Node
from tree_util import assert_binary_search_tree, assert_parent_pointers_consistent, get_binary_tree_keys, \
    get_random_binary_search_tree, get_binary_tree_nodes


class TestTextbook12_3(TestCase):

    def test_tree_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = BinaryTree()

        for key in keys:

            tree_insert(tree, Node(key))

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_tree_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_tree_delete(self):
        tree, _, keys = get_random_binary_search_tree()
        nodes = get_binary_tree_nodes(tree)

        while nodes:
            node = random.choice(nodes)
            keys.remove(node.key)

            tree_delete(tree, node)

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_tree_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*keys))
            nodes = get_binary_tree_nodes(tree)
