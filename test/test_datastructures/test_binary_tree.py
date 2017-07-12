from unittest import TestCase

from datastructures.binary_tree import BinaryTree, Node, ParentlessNode
from test.test_datastructures.tree_util import assert_parent_pointers_consistent


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
        self.assertEqual(root.left, left)
        self.assertEqual(root.right, right)
        self.assertIsNone(left.left)
        self.assertIsNone(left.right)
        self.assertIsNone(right.left)
        self.assertIsNone(right.right)
        assert_parent_pointers_consistent(tree)

    def test_create_parentless_binary_tree(self):
        left = ParentlessNode(3)
        right = ParentlessNode(20)
        root = ParentlessNode(17, left=left, right=right)
        tree = BinaryTree(root)
        self.assertEqual(tree.root, root)
        self.assertEqual(root.left, left)
        self.assertEqual(root.right, right)
        self.assertIsNone(left.left)
        self.assertIsNone(left.right)
        self.assertIsNone(right.left)
        self.assertIsNone(right.right)
