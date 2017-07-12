from unittest import TestCase

from datastructures.red_black_tree import RedBlackTree, Color, Node
from test.test_datastructures.test_binary_tree import BinaryTreeTest
from test.test_datastructures.tree_util import assert_parent_pointers_consistent


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
        self.assertEqual(root.left, left)
        self.assertEqual(root.right, right)
        assert_parent_pointers_consistent(tree, sentinel=tree.nil)
