from unittest import TestCase

from hamcrest import *

from datastructures.red_black_tree import RedBlackTree, Node, Black
from tree_util import assert_parent_pointers_consistent


class RedBlackTreeTest(TestCase):

    def test_create_empty_red_black_tree(self):
        tree = RedBlackTree()

        assert_that(tree.root, is_(tree.nil))
        assert_that(tree.nil.color, is_(Black))

    def test_create_binary_tree(self):
        left = Node(3)
        right = Node(20)
        root = Node(17, left=left, right=right)
        tree = RedBlackTree(root)

        assert_that(tree.root, is_(root))
        assert_that(root.left, is_(left))
        assert_that(root.right, is_(right))
        assert_parent_pointers_consistent(tree, sentinel=tree.nil)
