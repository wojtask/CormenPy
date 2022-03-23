import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter12.textbook12_1 import inorder_tree_walk
from datastructures.array import Array
from tree_util import get_random_binary_search_tree, get_binary_search_tree_inorder_keys


def assert_inorder_tree_keys(tree, keys):
    next_key_position = assert_inorder_subtree_keys(tree.root, keys, 1)
    assert_that(next_key_position, is_(equal_to(keys.length + 1)))


def assert_inorder_subtree_keys(subtree_root, keys, next_key_position):
    if subtree_root is None:
        return next_key_position
    next_key_position = assert_inorder_subtree_keys(subtree_root.left, keys, next_key_position)
    assert_that(subtree_root.key, is_(equal_to(keys[next_key_position])))
    next_key_position += 1
    return assert_inorder_subtree_keys(subtree_root.right, keys, next_key_position)


class TestTextbook12_1(TestCase):

    def test_inorder_tree_walk(self):
        tree = get_random_binary_search_tree()
        original_keys = get_binary_search_tree_inorder_keys(tree)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            inorder_tree_walk(tree.root)

        actual_output = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_inorder_tree_keys(tree, actual_output)
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))
