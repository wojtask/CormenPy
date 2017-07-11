from unittest import TestCase

from datastructures.red_black_tree import Color

tc = TestCase()


def binary_tree_to_list(tree, sentinel=None):
    return _binary_tree_to_list(tree.root, sentinel)


def _binary_tree_to_list(node, sentinel):
    if node is sentinel:
        return []
    return [node.key] + _binary_tree_to_list(node.left, sentinel) + _binary_tree_to_list(node.right, sentinel)


def assert_binary_search_tree(tree, sentinel=None):
    if tree.root is not sentinel:
        tc.assertIs(sentinel, tree.root.p)
        _assert_parent_pointers_consistent(tree.root, sentinel)
        _assert_binary_search_tree_subtree(tree.root, sentinel)


def _assert_parent_pointers_consistent(x, sentinel):
    if x.left is not sentinel:
        tc.assertIs(x, x.left.p)
        _assert_parent_pointers_consistent(x.left, sentinel)
    if x.right is not sentinel:
        tc.assertIs(x, x.right.p)
        _assert_parent_pointers_consistent(x.right, sentinel)


def _assert_binary_search_tree_subtree(x, sentinel):
    if x.left is not sentinel:
        left_keys = _binary_tree_to_list(x.left, sentinel)
        for key in left_keys:
            tc.assertTrue(key <= x.key)
        _assert_binary_search_tree_subtree(x.left, sentinel)
    if x.right is not sentinel:
        right_keys = _binary_tree_to_list(x.right, sentinel)
        for key in right_keys:
            tc.assertTrue(key >= x.key)
        _assert_binary_search_tree_subtree(x.right, sentinel)


def assert_red_black_tree(tree):
    tc.assertEqual(Color.BLACK, tree.root.color)
    tc.assertEqual(Color.BLACK, tree.nil.color)
    if tree.root is not tree.nil:
        assert_binary_search_tree(tree, sentinel=tree.nil)
        _assert_red_black_property_4(tree.root, tree.nil)
        _assert_red_black_property_5(tree.root, tree.nil)


def _assert_red_black_property_4(x, nil):
    if x.color == Color.RED:
        tc.assertEqual(Color.BLACK, x.left.color)
        tc.assertEqual(Color.BLACK, x.right.color)
    if x.left is not nil:
        _assert_red_black_property_4(x.left, nil)
    if x.right is not nil:
        _assert_red_black_property_4(x.right, nil)


def _assert_red_black_property_5(x, nil):
    left_bh, right_bh = 0, 0
    if x.left is not nil:
        left_bh = _assert_red_black_property_5(x.left, nil) + x.left.color
    if x.right is not nil:
        right_bh = _assert_red_black_property_5(x.right, nil) + x.right.color
    tc.assertEqual(left_bh, right_bh)
    return left_bh
