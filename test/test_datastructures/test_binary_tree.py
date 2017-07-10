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

    def assert_binary_search_tree(self, x):
        if x.left is not None:
            left_keys = binary_tree_to_list(x.left)
            for key in left_keys:
                self.assertTrue(key <= x.key)
            self.assert_binary_search_tree(x.left)
        if x.right is not None:
            right_keys = binary_tree_to_list(x.right)
            for key in right_keys:
                self.assertTrue(key >= x.key)
            self.assert_binary_search_tree(x.right)


def binary_tree_to_list(node):
    if node is None:
        return []
    return [node.key] + binary_tree_to_list(node.left) + binary_tree_to_list(node.right)
