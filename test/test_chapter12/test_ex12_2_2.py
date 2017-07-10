from unittest import TestCase

from chapter12.ex12_2_2 import recursive_tree_minimum, recursive_tree_maximum
from datastructures.binary_tree import BinaryTree, Node


class Ex12_2_2Test(TestCase):
    def setUp(self):
        self.tree = BinaryTree(Node(10, data='ten',
                               left=Node(4, data='four',
                                         left=Node(1, data='one')),
                               right=Node(14, data='fourteen',
                                          left=Node(11, data='eleven'),
                                          right=Node(19, data='nineteen',
                                                     right=Node(20, data='twenty')))))

    def test_recursive_tree_minimum(self):
        x = recursive_tree_minimum(self.tree.root)
        self.assertEqual(1, x.key)

    def test_recursive_tree_maximum(self):
        x = recursive_tree_maximum(self.tree.root)
        self.assertEqual(20, x.key)
