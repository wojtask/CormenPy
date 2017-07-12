from unittest import TestCase

from chapter12.ex12_2_2 import recursive_tree_minimum, recursive_tree_maximum
from datastructures.binary_tree import BinaryTree, Node


class Ex12_2_2Test(TestCase):
    def setUp(self):
        self.tree = BinaryTree(Node(10,
                               left=Node(4,
                                         left=Node(1)),
                               right=Node(14,
                                          left=Node(11),
                                          right=Node(19,
                                                     right=Node(20)))))

    def test_recursive_tree_minimum(self):
        x = recursive_tree_minimum(self.tree.root)
        self.assertEqual(x.key, 1)

    def test_recursive_tree_maximum(self):
        x = recursive_tree_maximum(self.tree.root)
        self.assertEqual(x.key, 20)
