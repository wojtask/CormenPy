from unittest import TestCase

from chapter12.ex12_3_4 import safe_tree_delete
from datastructures.binary_tree import BinaryTree, Node
from test.test_datastructures.tree_util import binary_tree_to_list, assert_binary_search_tree, \
    assert_parent_pointers_consistent


class Ex12_3_4Test(TestCase):
    def setUp(self):
        self.tree = BinaryTree(Node(10,
                               left=Node(4,
                                         left=Node(1)),
                               right=Node(14,
                                          left=Node(11),
                                          right=Node(19,
                                                     right=Node(20)))))

    def test_safe_tree_delete_leaf(self):
        node = self.tree.root.right.left  # a leaf
        safe_tree_delete(self.tree, node)
        keys = binary_tree_to_list(self.tree)
        self.assertEqual(sorted(keys), [1, 4, 10, 14, 19, 20])
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)

    def test_safe_tree_delete_node_with_one_child(self):
        node = self.tree.root.left  # a node with one child
        safe_tree_delete(self.tree, node)
        keys = binary_tree_to_list(self.tree)
        self.assertEqual(sorted(keys), [1, 10, 11, 14, 19, 20])
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)

    def test_safe_tree_delete_node_with_two_children(self):
        node = self.tree.root.right  # a node with two children
        safe_tree_delete(self.tree, node)
        keys = binary_tree_to_list(self.tree)
        self.assertEqual(sorted(keys), [1, 4, 10, 11, 19, 20])
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)
