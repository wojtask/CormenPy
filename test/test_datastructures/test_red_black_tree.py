from unittest import TestCase

from hamcrest import *

from datastructures.red_black_tree import RedBlackTree, Node, Color
from tree_util import assert_parent_pointers_consistent


class TestRedBlackTree(TestCase):

    def test_create_empty_red_black_tree(self):
        tree = RedBlackTree()

        assert_that(tree.root, is_(tree.nil))
        assert_that(tree.nil.color, is_(Color.BLACK))

    def test_create_empty_red_black_tree_without_sentinel(self):
        tree = RedBlackTree(sentinel=None)

        assert_that(tree.root, is_(none()))
        assert_that(hasattr(tree, 'nil'), is_(False))

    def test_create_red_black_tree(self):
        sentinel = Node(None)
        left = Node(3, left=sentinel, right=sentinel)
        right = Node(20, left=sentinel, right=sentinel)
        root = Node(17, left=left, right=right)
        tree = RedBlackTree(root, sentinel)

        assert_that(tree.root, is_(root))
        assert_that(tree.nil, is_(sentinel))
        assert_that(root.left, is_(left))
        assert_that(root.right, is_(right))
        assert_parent_pointers_consistent(tree)
