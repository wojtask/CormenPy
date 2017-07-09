import unittest

from chapter12.ex12_2_3 import tree_predecessor
from datastructures.binary_tree import BinaryTree, Node


class Ex12_2_3Test(unittest.TestCase):
    def test_tree_predecessor(self):
        tree = BinaryTree(Node(10,
                               left=Node(4,
                                         left=Node(1)),
                               right=Node(14,
                                          left=Node(11),
                                          right=Node(19,
                                                     right=Node(20)))))
        self.assertEqual(4, tree_predecessor(tree.root).key)
        self.assertEqual(1, tree_predecessor(tree.root.left).key)
        self.assertIsNone(tree_predecessor(tree.root.left.left))
        self.assertEqual(11, tree_predecessor(tree.root.right).key)
        self.assertEqual(10, tree_predecessor(tree.root.right.left).key)
        self.assertEqual(14, tree_predecessor(tree.root.right.right).key)
        self.assertEqual(19, tree_predecessor(tree.root.right.right.right).key)
