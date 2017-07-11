import io
from contextlib import redirect_stdout
from unittest import TestCase

from chapter12.textbook import *
from datastructures.array import Array
from datastructures.binary_tree import BinaryTree, Node
from test.test_datastructures.tree_util import binary_tree_to_list, assert_binary_search_tree, \
    assert_parent_pointers_consistent


class Chapter12Test(TestCase):
    def setUp(self):
        self.tree = BinaryTree(Node(10,
                               left=Node(4,
                                         left=Node(1)),
                               right=Node(14,
                                          left=Node(11),
                                          right=Node(19,
                                                     right=Node(20)))))

    def test_inorder_tree_walk_empty_tree(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            inorder_tree_walk(None)
        self.assertEqual('', captured_output.getvalue())

    def test_inorder_tree_walk(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            inorder_tree_walk(self.tree.root)
        self.assertEqual(['1', '4', '10', '11', '14', '19', '20'], captured_output.getvalue().splitlines())

    def test_tree_search_positive(self):
        x = tree_search(self.tree.root, 11)
        self.assertEqual(11, x.key)

    def test_tree_search_negative(self):
        x = tree_search(self.tree.root, 17)
        self.assertIsNone(x)

    def test_iterative_tree_search_positive(self):
        x = iterative_tree_search(self.tree.root, 11)
        self.assertEqual(11, x.key)

    def test_iterative_tree_search_negative(self):
        x = iterative_tree_search(self.tree.root, 17)
        self.assertIsNone(x)

    def test_tree_minimum(self):
        x = tree_minimum(self.tree.root)
        self.assertEqual(1, x.key)

    def test_tree_maximum(self):
        x = tree_maximum(self.tree.root)
        self.assertEqual(20, x.key)

    def test_tree_successor(self):
        x = tree_successor(self.tree.root)
        self.assertEqual(11, x.key)

    def test_tree_successor_nonexistent(self):
        max_node = self.tree.root.right.right.right  # a node with maximum value in the tree
        x = tree_successor(max_node)
        self.assertIsNone(x)

    def test_inorder_tree_walk_(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            inorder_tree_walk_(self.tree)
        self.assertEqual(['1', '4', '10', '11', '14', '19', '20'], captured_output.getvalue().splitlines())

    def test_tree_insert_to_empty_tree(self):
        tree = BinaryTree()
        tree_insert(tree, Node(12))
        keys = binary_tree_to_list(tree)
        self.assertEqual([12], keys)
        assert_binary_search_tree(tree)
        assert_parent_pointers_consistent(tree)

    def test_tree_insert(self):
        tree_insert(self.tree, Node(12))
        keys = binary_tree_to_list(self.tree)
        self.assertEqual([1, 4, 10, 11, 12, 14, 19, 20], sorted(keys))
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)

    def test_tree_delete_leaf(self):
        node = self.tree.root.right.left  # a leaf
        y = tree_delete(self.tree, node)
        self.assertEqual(11, y.key)
        keys = binary_tree_to_list(self.tree)
        self.assertEqual([1, 4, 10, 14, 19, 20], sorted(keys))
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)

    def test_tree_delete_node_with_one_child(self):
        node = self.tree.root.left  # a node with one child
        y = tree_delete(self.tree, node)
        self.assertEqual(4, y.key)
        keys = binary_tree_to_list(self.tree)
        self.assertEqual([1, 10, 11, 14, 19, 20], sorted(keys))
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)

    def test_tree_delete_node_with_two_children(self):
        node = self.tree.root.right  # a node with two children (successor's key = 19)
        y = tree_delete(self.tree, node)
        self.assertEqual(19, y.key)
        keys = binary_tree_to_list(self.tree)
        self.assertEqual([1, 4, 10, 11, 19, 20], sorted(keys))
        assert_binary_search_tree(self.tree)
        assert_parent_pointers_consistent(self.tree)

    def test_tree_delete_from_single_node_tree(self):
        tree = BinaryTree(Node(10))
        y = tree_delete(tree, tree.root)
        self.assertEqual(10, y.key)
        self.assertIsNone(tree.root)

    def test_inorder_sort(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            inorder_sort(array)
        self.assertEqual(sorted([str(x) for x in data]), captured_output.getvalue().splitlines())
