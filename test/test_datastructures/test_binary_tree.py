from unittest import TestCase

from datastructures.binary_tree import BinaryTree, Node


class BinaryTreeTest(TestCase):
    def test_create_empty_binary_tree(self):
        tree = BinaryTree()
        self.assertIsNone(tree.root)

    def test_create_binary_tree(self):
        left = Node(3)
        right = Node(20)
        root = Node(17, left=left, right=right)
        tree = BinaryTree(root)
        self.assertEqual(tree.root, root)
        self.assertIsNone(root.p)
        self.assertEqual(left, root.left)
        self.assertEqual(root, left.p)
        self.assertEqual(right, root.right)
        self.assertEqual(root, right.p)
        self.assertIsNone(left.left)
        self.assertIsNone(left.right)
        self.assertIsNone(right.left)
        self.assertIsNone(right.right)
