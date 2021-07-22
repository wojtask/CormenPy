import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter18.exercise18_2_5 import b_tree_capacious_leaves_insert, b_tree_capacious_leaves_create
from chapter18.textbook18_2 import b_tree_create
from datastructures.array import Array
from datastructures.b_tree import BTree
from util import between


def assert_b_tree_with_capacious_leaves(tree, t):
    assert_b_subtree_with_capacious_leaves(tree.root, t, min_keys=0)


def assert_b_subtree_with_capacious_leaves(node, t, min_keys):
    assert_that(node.key[:node.n], is_(equal_to(node.key[:node.n].sort())))
    assert_that(node.n, is_(greater_than_or_equal_to(min_keys)))
    if node.leaf:
        assert_that(node.n, is_(less_than_or_equal_to(4 * t - 1)))
        return
    assert_that(node.n, is_(less_than_or_equal_to(2 * t - 1)))
    for i in between(1, node.n):
        left_child = node.c[i]
        right_child = node.c[i + 1]
        assert_that(node.key[i], is_(greater_than_or_equal_to(left_child.key[left_child.n])))
        assert_that(node.key[i], is_(less_than_or_equal_to(right_child.key[1])))
    for i in between(1, node.n + 1):
        assert_b_subtree_with_capacious_leaves(node.c[i], t, min_keys=1)


def get_b_tree_with_capacious_leaves_keys(tree):
    return get_b_subtree_with_capacious_leaves_keys(tree.root)


def get_b_subtree_with_capacious_leaves_keys(node):
    if node.leaf:
        return node.key[:node.n]
    elements = Array()
    for i in between(1, node.n):
        elements += get_b_subtree_with_capacious_leaves_keys(node.c[i])
        elements.append(node.key[i])
    elements += get_b_subtree_with_capacious_leaves_keys(node.c[node.n + 1])
    return elements


class TestExercise18_2_5(TestCase):

    def test_b_tree_capacious_leaves_insert(self):
        """
        Create an empty B-tree. Keep adding new keys to the tree that supports capacious leaves. After each operation
        assert that the actual tree is a valid B-tree with capacious leaves and that it has all expected keys.
        """
        tree = BTree()
        t = random.randint(2, 10)
        b_tree_capacious_leaves_create(tree, t)
        assert_b_tree_with_capacious_leaves(tree, t)

        max_key_value = 10000
        keys = get_random_array(size=1000, max_value=max_key_value, unique=True)
        keys_in_tree = Array()
        for key in keys:
            b_tree_capacious_leaves_insert(tree, key, t)
            keys_in_tree.append(key)
            assert_b_tree_with_capacious_leaves(tree, t)
            actual_tree_keys = get_b_tree_with_capacious_leaves_keys(tree)
            assert_that(actual_tree_keys, is_(equal_to(keys_in_tree.sort())))
