import random

import math
from hamcrest import *

from array_util import get_random_unique_array, get_random_array
from datastructures import binary_tree as bt, red_black_tree as rb
from datastructures.binary_tree import BinaryTree
from datastructures.interval import Interval
from datastructures.red_black_tree import RedBlackTree, Red, Black


def get_binary_tree_keys(tree, sentinel=None):
    return _get_binary_subtree_keys(tree.root, sentinel)


def _get_binary_subtree_keys(node, sentinel):
    if node is sentinel:
        return []
    return _get_binary_subtree_keys(node.left, sentinel) + [node.key] + _get_binary_subtree_keys(node.right, sentinel)


def get_binary_tree_nodes(tree, sentinel=None):
    return _get_binary_subtree_nodes(tree.root, sentinel)


def _get_binary_subtree_nodes(node, sentinel):
    if node is sentinel:
        return []
    return _get_binary_subtree_nodes(node.left, sentinel) + [node] + _get_binary_subtree_nodes(node.right, sentinel)


def get_random_binary_search_tree(min_size=1, max_size=20, max_value=999):
    tree_size = random.randint(min_size, max_size)
    keys = sorted(random.sample(range(0, max_value + 1), tree_size))
    nodes = [bt.Node(key) for key in keys]
    tree = BinaryTree()
    tree.root = _get_random_binary_search_subtree(nodes)
    return tree, nodes, keys


def _get_random_binary_search_subtree(nodes):
    if not nodes:
        return None
    i = random.randrange(len(nodes))
    node = nodes[i]
    left_node = _get_random_binary_search_subtree(nodes[:i])
    if left_node is not None:
        node.left = left_node
        left_node.p = node
    right_node = _get_random_binary_search_subtree(nodes[i + 1:])
    if right_node is not None:
        node.right = right_node
        right_node.p = node
    return node


def assert_parent_pointers_consistent(tree, sentinel=None):
    if tree.root is not sentinel:
        assert_that(tree.root.p, is_(sentinel))
        _assert_parent_pointers_consistent(tree.root, sentinel)


def _assert_parent_pointers_consistent(node, sentinel):
    if node.left is not sentinel:
        assert_that(node.left.p, is_(node))
        _assert_parent_pointers_consistent(node.left, sentinel)
    if node.right is not sentinel:
        assert_that(node.right.p, is_(node))
        _assert_parent_pointers_consistent(node.right, sentinel)


def assert_binary_search_tree(tree, sentinel=None):
    if tree.root is not sentinel:
        _assert_binary_search_subtree(tree.root, sentinel)


def _assert_binary_search_subtree(node, sentinel):
    if node.left is not sentinel:
        left_keys = _get_binary_subtree_keys(node.left, sentinel)
        for left_key in left_keys:
            assert_that(left_key, is_(less_than_or_equal_to(node.key)))
        _assert_binary_search_subtree(node.left, sentinel)
    if node.right is not sentinel:
        right_keys = _get_binary_subtree_keys(node.right, sentinel)
        for right_key in right_keys:
            assert_that(right_key, is_(greater_than_or_equal_to(node.key)))
        _assert_binary_search_subtree(node.right, sentinel)


def get_random_red_black_tree(black_height=3, min_value=0, max_value=999, sentinel=rb.Node(None)):
    nodes = []
    tree = RedBlackTree(_get_random_red_black_subtree(black_height, nodes), sentinel=sentinel)
    tree_size = len(nodes)
    _, keys = get_random_unique_array(min_size=tree_size, max_size=tree_size, min_value=min_value, max_value=max_value)
    keys.sort()
    _fill_subtree_with_keys(tree.root, keys, tree.nil)
    return tree, nodes, keys


def _get_random_red_black_subtree(black_height, nodes):
    if black_height == 0:
        return None

    # at each level of the tree we try to create an extra red node in the left subtree
    if random.choice([Black, Red]) == Red:
        left_subtree_root = _create_red_node_in_subtree(black_height, nodes)
    else:
        left_subtree_root = _get_random_red_black_subtree(black_height - 1, nodes)

    # ...and we repeat the same for the right subtree
    if random.choice([Black, Red]) == Red:
        right_subtree_root = _create_red_node_in_subtree(black_height, nodes)
    else:
        right_subtree_root = _get_random_red_black_subtree(black_height - 1, nodes)

    root = rb.Node(None, left=left_subtree_root, right=right_subtree_root)
    nodes.append(root)
    return root


def _create_red_node_in_subtree(black_height, nodes):
    left_subtree_root = _get_random_red_black_subtree(black_height - 1, nodes)
    right_subtree_root = _get_random_red_black_subtree(black_height - 1, nodes)
    subtree_root = rb.Node(None, left=left_subtree_root, right=right_subtree_root, color=Red)
    nodes.append(subtree_root)
    return subtree_root


def _fill_subtree_with_keys(node, keys, sentinel):
    if node is sentinel:
        return
    left_subtree_size = _get_subtree_size(node.left, sentinel)
    node.key = keys[left_subtree_size]
    _fill_subtree_with_keys(node.left, keys[:left_subtree_size], sentinel)
    _fill_subtree_with_keys(node.right, keys[left_subtree_size + 1:], sentinel)


def _get_subtree_size(node, sentinel=None):
    if node is sentinel:
        return 0
    return 1 + _get_subtree_size(node.left, sentinel) + _get_subtree_size(node.right, sentinel)


def assert_red_black_tree(tree, sentinel=None):
    if tree.root is not None:
        assert_that(tree.root.color, is_(Black))
    if sentinel is not None:
        assert_that(tree.nil.color, is_(Black))
    if tree.root is not sentinel:
        assert_binary_search_tree(tree, sentinel)
        _assert_red_black_property_4(tree.root, sentinel)
        _assert_red_black_property_5(tree.root, sentinel)


def _assert_red_black_property_4(node, sentinel):
    if node.color == Red:
        if node.left is not sentinel:
            assert_that(node.left.color, is_(Black))
        if node.right is not sentinel:
            assert_that(node.right.color, is_(Black))
    if node.left is not sentinel:
        _assert_red_black_property_4(node.left, sentinel)
    if node.right is not sentinel:
        _assert_red_black_property_4(node.right, sentinel)


def _assert_red_black_property_5(node, sentinel):
    left_bh = right_bh = 0
    if node.left is not sentinel:
        left_bh = _assert_red_black_property_5(node.left, sentinel) + node.left.color
    if node.right is not sentinel:
        right_bh = _assert_red_black_property_5(node.right, sentinel) + node.right.color
    assert_that(left_bh, is_(equal_to(right_bh)))
    return left_bh


def assert_avl_tree(tree):
    assert_binary_search_tree(tree)
    _assert_avl_subtree(tree.root)


def _assert_avl_subtree(node):
    if node is None:
        return -1
    hl = _assert_avl_subtree(node.left)
    hr = _assert_avl_subtree(node.right)
    assert_that(node.h, is_(equal_to(max(hl, hr) + 1)))
    assert_that(abs(hr - hl), is_(less_than_or_equal_to(1)))
    return node.h


def assert_treap(tree):
    assert_binary_search_tree(tree)
    if tree.root is not None:
        _assert_subtreap(tree.root)


def _assert_subtreap(node):
    if node.left is not None:
        assert_that(node.priority, is_(less_than(node.left.priority)))
        _assert_subtreap(node.left)
    if node.right is not None:
        assert_that(node.priority, is_(less_than(node.right.priority)))
        _assert_subtreap(node.right)


def get_random_os_tree(black_height=3, max_value=999):
    tree, nodes, keys = get_random_red_black_tree(black_height, max_value=max_value, sentinel=rb.OSNode(None))
    _augment_to_os_tree(tree)
    return tree, nodes, keys


def _augment_to_os_tree(tree):
    tree.nil.size = 0
    if tree.root is not tree.nil:
        _augment_to_os_subtree(tree.root, tree.nil)


def _augment_to_os_subtree(node, sentinel):
    left_size = right_size = 0
    if node.left is not sentinel:
        left_size = _augment_to_os_subtree(node.left, sentinel)
    if node.right is not sentinel:
        right_size = _augment_to_os_subtree(node.right, sentinel)
    node.size = left_size + right_size + 1
    return node.size


def assert_os_tree(tree):
    assert_red_black_tree(tree, sentinel=tree.nil)
    if tree.root is not tree.nil:
        _assert_os_subtree(tree.root, tree.nil)


def _assert_os_subtree(node, sentinel):
    assert_that(node.size, is_(equal_to(node.left.size + node.right.size + 1)))
    if node.left is not sentinel:
        _assert_os_subtree(node.left, sentinel)
    if node.right is not sentinel:
        _assert_os_subtree(node.right, sentinel)


def get_random_interval_tree(black_height=3, max_value=999):
    # we treat max_value as the upper bound for high endpoints
    # the procedure is generating intervals at most (.1 * max_value) units wide
    tree, nodes, keys = get_random_red_black_tree(black_height, max_value=int(.9 * max_value),
                                                  sentinel=rb.IntervalNode(None, None))
    # we will allow keys and intervals to be non unique
    tree_size = len(nodes)
    _, keys = get_random_array(min_size=tree_size, max_size=tree_size, max_value=max_value)
    keys.sort()
    _fill_subtree_with_intervals(tree.root, keys, max_value, sentinel=tree.nil)
    _augment_to_interval_tree(tree)
    return tree, nodes, keys


def _fill_subtree_with_intervals(node, keys, max_value, sentinel):
    if node is sentinel:
        return
    left_subtree_size = _get_subtree_size(node.left, sentinel)
    node.key = keys[left_subtree_size]
    high_endpoint = random.randint(node.key, node.key + int(.1 * max_value))
    node.int = Interval(node.key, high_endpoint)
    _fill_subtree_with_intervals(node.left, keys[:left_subtree_size], max_value, sentinel)
    _fill_subtree_with_intervals(node.right, keys[left_subtree_size + 1:], max_value, sentinel)


def _augment_to_interval_tree(tree):
    tree.nil.max = -math.inf
    if tree.root is not tree.nil:
        _augment_to_interval_subtree(tree.root, tree.nil)


def _augment_to_interval_subtree(node, sentinel):
    max_left = max_right = -math.inf
    if node.left is not sentinel:
        max_left = _augment_to_interval_subtree(node.left, sentinel)
    if node.right is not sentinel:
        max_right = _augment_to_interval_subtree(node.right, sentinel)
    node.max = max(node.int.high, max_left, max_right)
    return node.max


def assert_interval_tree(tree):
    assert_red_black_tree(tree, sentinel=tree.nil)
    if tree.root is not tree.nil:
        _assert_interval_subtree(tree.root, tree.nil)


def _assert_interval_subtree(node, sentinel):
    assert_that(node.max, is_(equal_to(max(node.int.high, node.left.max, node.right.max))))
    if node.left is not sentinel:
        _assert_interval_subtree(node.left, sentinel)
    if node.right is not sentinel:
        _assert_interval_subtree(node.right, sentinel)
