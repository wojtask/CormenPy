import random
from unittest import TestCase

from hamcrest import *

from chapter12.textbook12_2 import tree_search, iterative_tree_search, tree_minimum, tree_maximum, tree_successor
from tree_util import get_random_binary_search_tree, get_binary_search_tree_inorder_keys, \
    get_binary_search_tree_inorder_nodes


class TestTextbook12_2(TestCase):

    def test_tree_search(self):
        tree = get_random_binary_search_tree(min_size=10, max_size=20, max_value=20)
        original_nodes = get_binary_search_tree_inorder_nodes(tree)
        original_keys = get_binary_search_tree_inorder_keys(tree)
        key_to_find = random.randint(0, 20)

        actual_node = tree_search(tree.root, key_to_find)

        if key_to_find in original_keys:
            assert_that(actual_node, is_in(original_nodes))
            assert_that(key_to_find, is_(equal_to(actual_node.key)))
        else:
            assert_that(actual_node, is_(none()))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))

    def test_iterative_tree_search(self):
        tree = get_random_binary_search_tree(min_size=10, max_size=20, max_value=20)
        original_nodes = get_binary_search_tree_inorder_nodes(tree)
        original_keys = get_binary_search_tree_inorder_keys(tree)
        key_to_find = random.randint(0, 20)

        actual_node = iterative_tree_search(tree.root, key_to_find)

        if key_to_find in original_keys:
            assert_that(actual_node, is_in(original_nodes))
            assert_that(key_to_find, is_(equal_to(actual_node.key)))
        else:
            assert_that(actual_node, is_(none()))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))

    def test_tree_minimum(self):
        tree = get_random_binary_search_tree()
        original_nodes = get_binary_search_tree_inorder_nodes(tree)
        original_keys = get_binary_search_tree_inorder_keys(tree)

        actual_minimum = tree_minimum(tree.root)

        assert_that(actual_minimum, is_in(original_nodes))
        assert_that(actual_minimum.key, is_(equal_to(min(original_keys))))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))

    def test_tree_maximum(self):
        tree = get_random_binary_search_tree()
        original_nodes = get_binary_search_tree_inorder_nodes(tree)
        original_keys = get_binary_search_tree_inorder_keys(tree)

        actual_maximum = tree_maximum(tree.root)

        assert_that(actual_maximum, is_in(original_nodes))
        assert_that(actual_maximum.key, is_(equal_to(max(original_keys))))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))

    def test_tree_successor(self):
        tree = get_random_binary_search_tree()
        original_nodes = get_binary_search_tree_inorder_nodes(tree)
        original_keys = get_binary_search_tree_inorder_keys(tree)
        given_node = original_nodes.random_choice()

        actual_successor = tree_successor(given_node)

        if actual_successor is None:
            assert_that(given_node.key, is_(equal_to(max(original_keys))))
        else:
            assert_that(actual_successor, is_in(original_nodes))
            assert_that(actual_successor.key, is_(greater_than_or_equal_to(given_node.key)))
            for node in original_nodes:
                assert_that(node.key, is_not(all_of(greater_than(given_node.key), less_than(actual_successor.key))))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))
