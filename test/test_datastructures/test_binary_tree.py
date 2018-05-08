from unittest import TestCase

from hamcrest import *

from datastructures.binary_tree import BinaryTree, Node, ParentlessNode
from tree_util import assert_parent_pointers_consistent


class TestBinaryTree(TestCase):

    def test_create_empty_binary_tree(self):
        tree = BinaryTree()
        assert_that(tree.root, is_(none()))

    def test_create_binary_tree(self):
        left = Node(3)
        right = Node(20)
        root = Node(17, left=left, right=right)
        tree = BinaryTree(root)

        assert_that(tree.root, is_(root))
        assert_that(root.left, is_(left))
        assert_that(root.right, is_(right))
        assert_that(left.left, is_(none()))
        assert_that(left.right, is_(none()))
        assert_that(right.left, is_(none()))
        assert_that(right.right, is_(none()))
        assert_parent_pointers_consistent(tree)

    def test_create_parentless_binary_tree(self):
        left = ParentlessNode(3)
        right = ParentlessNode(20)
        root = ParentlessNode(17, left=left, right=right)
        tree = BinaryTree(root)

        assert_that(tree.root, is_(root))
        assert_that(root.left, is_(left))
        assert_that(root.right, is_(right))
        assert_that(left.left, is_(none()))
        assert_that(left.right, is_(none()))
        assert_that(right.left, is_(none()))
        assert_that(right.right, is_(none()))
