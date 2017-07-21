import random
from unittest import TestCase

from chapter13.textbook import rb_insert
from datastructures import binary_tree as bt, red_black_tree as rb
from datastructures.binary_tree import BinaryTree
from datastructures.red_black_tree import Color, RedBlackTree

tc = TestCase()


def binary_tree_to_list(tree, sentinel=None):
    return _binary_subtree_to_list(tree.root, sentinel)


def _binary_subtree_to_list(node, sentinel):
    if node is sentinel:
        return []
    return [node.key] + _binary_subtree_to_list(node.left, sentinel) + _binary_subtree_to_list(node.right, sentinel)


def random_binary_search_tree(min_size=1, max_size=20, max_value=999):
    tree_size = random.randint(min_size, max_size)
    nodes = []
    tree = BinaryTree(_random_binary_search_subtree(tree_size, nodes, min_value=0, max_value=max_value))
    keys = [node.key for node in nodes]
    return tree, nodes, keys


def _random_binary_search_subtree(tree_size, nodes, min_value, max_value):
    root_key = random.randint(min_value, max_value)
    left_subtree_size = random.randint(0, tree_size - 1)
    right_subtree_size = tree_size - 1 - left_subtree_size
    left_subtree_root = right_subtree_root = None
    if left_subtree_size > 0:
        left_subtree_root = _random_binary_search_subtree(
            left_subtree_size, nodes, min_value=min_value, max_value=root_key
        )
    if right_subtree_size > 0:
        right_subtree_root = _random_binary_search_subtree(
            right_subtree_size, nodes, min_value=root_key, max_value=max_value
        )
    root = bt.Node(root_key, left=left_subtree_root, right=right_subtree_root)
    nodes.append(root)
    return root


def build_random_red_black_tree(min_size=1, max_size=20, max_value=999):
    tree_size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value) for _ in range(tree_size)]
    nodes = [rb.Node(key) for key in keys]
    tree = RedBlackTree()
    for node in nodes:
        rb_insert(tree, node)
    return tree, nodes, keys


def assert_parent_pointers_consistent(tree, sentinel=None):
    if tree.root is not sentinel:
        tc.assertIs(tree.root.p, sentinel)
        _assert_parent_pointers_consistent(tree.root, sentinel)


def _assert_parent_pointers_consistent(node, sentinel):
    if node.left is not sentinel:
        tc.assertIs(node.left.p, node)
        _assert_parent_pointers_consistent(node.left, sentinel)
    if node.right is not sentinel:
        tc.assertIs(node.right.p, node)
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
    tc.assertEqual(tree.root.color, Color.BLACK)
    tc.assertEqual(tree.nil.color, Color.BLACK)
    if tree.root is not tree.nil:
        assert_binary_search_tree(tree, sentinel=tree.nil)
        _assert_red_black_property_4(tree.root, tree.nil)
        _assert_red_black_property_5(tree.root, tree.nil)


def _assert_red_black_property_4(node, nil):
    if node.color == Color.RED:
        tc.assertEqual(node.left.color, Color.BLACK)
        tc.assertEqual(node.right.color, Color.BLACK)
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
