from unittest import TestCase

from datastructures.red_black_tree import RedBlackTree, Color, Node
from test.test_datastructures.test_binary_tree import BinaryTreeTest


class RedBlackTreeTest(TestCase):
    def setUp(self):
        self.btt = BinaryTreeTest()

    def test_create_empty_red_black_tree(self):
        tree = RedBlackTree()
        self.assertIs(tree.root, tree.nil)
        self.assertEqual(tree.nil.color, Color.BLACK)

    def test_create_binary_tree(self):
        left = Node(3)
        right = Node(20)
        root = Node(17, left=left, right=right)
        tree = RedBlackTree(root)
        self.assertEqual(tree.root, root)
        self.assertIs(tree.nil, root.p)
        self.assertEqual(left, root.left)
        self.assertEqual(root, left.p)
        self.assertEqual(right, root.right)
        self.assertEqual(root, right.p)
        self.assertIs(tree.nil, left.left)
        self.assertIs(tree.nil, left.right)
        self.assertIs(tree.nil, right.left)
        self.assertIs(tree.nil, right.right)
