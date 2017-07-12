from unittest import TestCase

from datastructures.red_black_tree import Color

tc = TestCase()


def binary_tree_to_list(tree, sentinel=None):
    return _binary_subtree_to_list(tree.root, sentinel)


def _binary_subtree_to_list(node, sentinel):
    if node is sentinel:
        return []
    return [node.key] + _binary_subtree_to_list(node.left, sentinel) + _binary_subtree_to_list(node.right, sentinel)


def assert_parent_pointers_consistent(tree, sentinel=None):
    if tree.root is not sentinel:
        tc.assertIs(sentinel, tree.root.p)
        _assert_parent_pointers_consistent(tree.root, sentinel)


def _assert_parent_pointers_consistent(node, sentinel):
    if node.left is not sentinel:
        tc.assertIs(node, node.left.p)
        _assert_parent_pointers_consistent(node.left, sentinel)
    if node.right is not sentinel:
        tc.assertIs(node, node.right.p)
        _assert_parent_pointers_consistent(node.right, sentinel)


def assert_binary_search_tree(tree, sentinel=None):
    if tree.root is not sentinel:
        _assert_binary_search_subtree(tree.root, sentinel)


def _assert_binary_search_subtree(node, sentinel):
    if node.left is not sentinel:
        left_keys = _binary_subtree_to_list(node.left, sentinel)
        for left_key in left_keys:
            tc.assertTrue(left_key <= node.key)
        _assert_binary_search_subtree(node.left, sentinel)
    if node.right is not sentinel:
        right_keys = _binary_subtree_to_list(node.right, sentinel)
        for right_key in right_keys:
            tc.assertTrue(right_key >= node.key)
        _assert_binary_search_subtree(node.right, sentinel)


def assert_red_black_tree(tree):
    tc.assertEqual(Color.BLACK, tree.root.color)
    tc.assertEqual(Color.BLACK, tree.nil.color)
    if tree.root is not tree.nil:
        assert_binary_search_tree(tree, sentinel=tree.nil)
        _assert_red_black_property_4(tree.root, tree.nil)
        _assert_red_black_property_5(tree.root, tree.nil)


def _assert_red_black_property_4(node, nil):
    if node.color == Color.RED:
        tc.assertEqual(Color.BLACK, node.left.color)
        tc.assertEqual(Color.BLACK, node.right.color)
    if node.left is not nil:
        _assert_red_black_property_4(node.left, nil)
    if node.right is not nil:
        _assert_red_black_property_4(node.right, nil)


def _assert_red_black_property_5(node, nil):
    left_bh = right_bh = 0
    if node.left is not nil:
        left_bh = _assert_red_black_property_5(node.left, nil) + node.left.color.value
    if node.right is not nil:
        right_bh = _assert_red_black_property_5(node.right, nil) + node.right.color.value
    tc.assertEqual(left_bh, right_bh)
    return left_bh


def assert_avl_tree(tree):
    assert_binary_search_tree(tree)
    _assert_avl_subtree(tree.root)


def _assert_avl_subtree(node):
    if node is None:
        return -1
    hl = _assert_avl_subtree(node.left)
    hr = _assert_avl_subtree(node.right)
    tc.assertEqual(node.h, max(hl, hr) + 1)
    tc.assertTrue(abs(hr - hl) <= 1)
    return node.h


def assert_treap(tree):
    assert_binary_search_tree(tree)
    if tree.root is not None:
        _assert_subtreap(tree.root)


def _assert_subtreap(node):
    if node.left is not None:
        tc.assertTrue(node.priority < node.left.priority)
        _assert_subtreap(node.left)
    if node.right is not None:
        tc.assertTrue(node.priority < node.right.priority)
        _assert_subtreap(node.right)


def assert_os_tree(tree):
    assert_red_black_tree(tree)
    if tree.root is not tree.nil:
        _assert_os_subtree(tree.root, tree.nil)


def _assert_os_subtree(node, nil):
    tc.assertEqual(node.size, node.left.size + node.right.size + 1)
    if node.left is not nil:
        _assert_os_subtree(node.left, nil)
    if node.right is not nil:
        _assert_os_subtree(node.right, nil)
