from unittest import TestCase

from chapter12.ex12_2_3 import tree_predecessor
from datastructures.binary_tree import BinaryTree, Node


class Ex12_2_3Test(TestCase):
    def test_tree_predecessor(self):
        tree = BinaryTree(Node(10,
                               left=Node(4,
                                         left=Node(1)),
                               right=Node(14,
                                          left=Node(11),
                                          right=Node(19,
                                                     right=Node(20)))))
        self.assertEqual(tree_predecessor(tree.root).key, 4)
        self.assertEqual(tree_predecessor(tree.root.left).key, 1)
        self.assertIsNone(tree_predecessor(tree.root.left.left))
        self.assertEqual(tree_predecessor(tree.root.right).key, 11)
        self.assertEqual(tree_predecessor(tree.root.right.left).key, 10)
        self.assertEqual(tree_predecessor(tree.root.right.right).key, 14)
        self.assertEqual(tree_predecessor(tree.root.right.right.right).key, 19)
