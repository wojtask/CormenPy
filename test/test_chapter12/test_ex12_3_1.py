from unittest import TestCase

from chapter12.ex12_3_1 import recursive_tree_insert_wrapper
from datastructures.binary_tree import Node, BinaryTree
from test.test_datastructures.test_binary_tree import binary_tree_to_list, BinaryTreeTest


class Ex12_3_1Test(TestCase):
    def setUp(self):
        self.btt = BinaryTreeTest()

    def test_recursive_tree_insert_to_empty_tree(self):
        tree = BinaryTree()
        recursive_tree_insert_wrapper(tree, Node(12))
        keys = binary_tree_to_list(tree.root)
        self.assertEqual([12], keys)
        self.btt.assert_binary_search_tree(tree.root)

    def test_recursive_tree_insert(self):
        tree = BinaryTree(Node(10,
                               left=Node(4,
                                         left=Node(1)),
                               right=Node(14,
                                          left=Node(11),
                                          right=Node(19,
                                                     right=Node(20)))))
        recursive_tree_insert_wrapper(tree, Node(12))
        keys = binary_tree_to_list(tree.root)
        self.assertEqual([1, 4, 10, 11, 12, 14, 19, 20], sorted(keys))
        self.btt.assert_binary_search_tree(tree.root)
