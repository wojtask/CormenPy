from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.exercise14_2_2 import bh_rb_insert, bh_rb_delete
from datastructures.red_black_tree import RedBlackTree, Color, BHNode
from tree_util import get_binary_search_tree_inorder_nodes, assert_red_black_tree


def assert_bh_in_subtree(subtree_root, sentinel):
    left_bh = 1
    if subtree_root.left is not sentinel:
        left_bh = assert_bh_in_subtree(subtree_root.left, sentinel)
        if subtree_root.left.color == Color.BLACK:
            left_bh += 1
    assert_that(left_bh, is_(equal_to(subtree_root.bh)))
    if subtree_root.right is not sentinel:
        assert_bh_in_subtree(subtree_root.right, sentinel)
    return left_bh


def assert_bh_in_tree(tree):
    assert_that(tree.nil.bh, is_(equal_to(0)))
    if tree.root is not tree.nil:
        assert_bh_in_subtree(tree.root, tree.nil)


class TestExercise14_2_2(TestCase):

    def test_bh_rb_tree(self):
        keys = get_random_array()
        tree = RedBlackTree(sentinel=BHNode(None))

        for key in keys:
            bh_rb_insert(tree, BHNode(key), sentinel=tree.nil)

        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        expected_size = keys.length

        while expected_size > 0:
            assert_that(inorder_nodes.length, is_(equal_to(expected_size)))
            assert_red_black_tree(tree)
            assert_bh_in_tree(tree)

            node = inorder_nodes.random_choice()

            bh_rb_delete(tree, node, sentinel=tree.nil)

            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
            expected_size -= 1
