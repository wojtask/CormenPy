from unittest import TestCase

from chapter12.ex12_3_6 import fair_tree_delete
from datastructures.binary_tree import BinaryTree, Node
from test.test_datastructures.tree_util import binary_tree_to_list, assert_binary_search_tree, \
    assert_parent_pointers_consistent


class Ex12_3_6Test(TestCase):
    def setUp(self):
        self.tree = BinaryTree(Node(10,
                                    left=Node(4,
                                              left=Node(1)),
                                    right=Node(14,
                                               left=Node(11),
                                               right=Node(19,
                                                          right=Node(20)))))

    def test_fair_tree_delete_leaf(self):
        y = fair_tree_delete(self.tree, self.tree.root.right.left)  # a leaf
        self.assertEqual(11, y.key)
        keys = binary_tree_to_list(self.tree)
        self.assertEqual([1, 4, 10, 14, 19, 20], sorted(keys))
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)

    def test_fair_tree_delete_node_with_one_child(self):
        node = self.tree.root.left  # a node with one child
        y = fair_tree_delete(self.tree, node)
        self.assertEqual(4, y.key)
        keys = binary_tree_to_list(self.tree)
        self.assertEqual([1, 10, 11, 14, 19, 20], sorted(keys))
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)

    def test_fair_tree_delete_node_with_two_children(self):
        node = self.tree.root.right  # a node with two children (predecessor's key = 11, successor's key = 19)
        y = fair_tree_delete(self.tree, node)
        self.assertIn(y.key, [11, 19])
        keys = binary_tree_to_list(self.tree)
        self.assertEqual([1, 4, 10, 11, 19, 20], sorted(keys))
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)
