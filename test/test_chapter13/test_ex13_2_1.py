from unittest import TestCase

from chapter13.ex13_2_1 import right_rotate
from test.test_datastructures.tree_util import assert_binary_search_tree, assert_parent_pointers_consistent


class Ex13_2_1Test(TestCase):
    def test_right_rotate_binary_tree(self):
        from datastructures.binary_tree import BinaryTree, Node
        alpha, beta, gamma = Node(1), Node(3), Node(5)
        x = Node(2, left=alpha, right=beta)
        y = Node(4, left=x, right=gamma)
        z = Node(100, left=y)
        tree = BinaryTree(z)
        right_rotate(tree, y)
        self.assertIs(z.left, x)
        self.assertIs(x.right, y)
        self.assertIs(x.left, alpha)
        self.assertIs(y.left, beta)
        self.assertIs(y.right, gamma)
        assert_binary_search_tree(tree)
        assert_parent_pointers_consistent(tree)

    def test_left_rotate_red_black_tree(self):
        from datastructures.red_black_tree import RedBlackTree, Node
        alpha, beta, gamma = Node(1), Node(3), Node(5)
        x = Node(2, left=alpha, right=beta)
        y = Node(4, left=x, right=gamma)
        z = Node(100, left=y)
        tree = RedBlackTree(z)
        right_rotate(tree, y)
        self.assertIs(z.left, x)
        self.assertIs(x.right, y)
        self.assertIs(x.left, alpha)
        self.assertIs(y.left, beta)
        self.assertIs(y.right, gamma)
        assert_binary_search_tree(tree, sentinel=tree.nil)
        assert_parent_pointers_consistent(tree, sentinel=tree.nil)
