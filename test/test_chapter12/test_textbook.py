import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from chapter12.textbook import inorder_tree_walk, tree_search, iterative_tree_search, tree_minimum, tree_maximum, \
    tree_successor, inorder_tree_walk_, tree_insert, tree_delete, inorder_sort
from datastructures.binary_tree import BinaryTree, Node
from test.test_datastructures.array_util import random_int_array
from test.test_datastructures.tree_util import binary_tree_to_list, assert_binary_search_tree, \
    assert_parent_pointers_consistent, random_binary_search_tree


class Chapter12Test(TestCase):
    def setUp(self):
        self.tree = BinaryTree(Node(10,
                               left=Node(4,
                                         left=Node(1)),
                               right=Node(14,
                                          left=Node(11),
                                          right=Node(19,
                                                     right=Node(20)))))

    def test_inorder_tree_walk(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            inorder_tree_walk(self.tree.root)
        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        self.assertEqual(actual_output, [1, 4, 10, 11, 14, 19, 20])

    def test_tree_search(self):
        keys = binary_tree_to_list(self.tree)
        key = random.randint(0, 25)
        x = tree_search(self.tree.root, key)
        if key in keys:
            self.assertEqual(key, x.key)
        else:
            self.assertIsNone(x)

    def test_iterative_tree_search(self):
        keys = binary_tree_to_list(self.tree)
        key = random.randint(0, 25)
        x = iterative_tree_search(self.tree.root, key)
        if key in keys:
            self.assertEqual(key, x.key)
        else:
            self.assertIsNone(x)

    def test_tree_minimum(self):
        x = tree_minimum(self.tree.root)
        self.assertEqual(x.key, 1)

    def test_tree_maximum(self):
        x = tree_maximum(self.tree.root)
        self.assertEqual(x.key, 20)

    def test_tree_successor(self):
        self.assertEqual(tree_successor(self.tree.root).key, 11)
        self.assertEqual(tree_successor(self.tree.root.left).key, 10)
        self.assertEqual(tree_successor(self.tree.root.left.left).key, 4)
        self.assertEqual(tree_successor(self.tree.root.right).key, 19)
        self.assertEqual(tree_successor(self.tree.root.right.left).key, 14)
        self.assertEqual(tree_successor(self.tree.root.right.right).key, 20)
        self.assertIsNone(tree_successor(self.tree.root.right.right.right))

    def test_inorder_tree_walk_(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            inorder_tree_walk_(self.tree)
        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        self.assertEqual(actual_output, [1, 4, 10, 11, 14, 19, 20])

    def test_tree_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = BinaryTree()
        for key in keys:
            tree_insert(tree, Node(key))
            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
        actual_keys = binary_tree_to_list(tree)
        self.assertEqual(sorted(actual_keys), sorted(keys))

    def test_tree_delete(self):
        tree, nodes, keys = random_binary_search_tree()
        random.shuffle(nodes)
        for i, node in enumerate(nodes):
            keys.remove(node.key)
            y = tree_delete(tree, node)
            if y is not node:
                # this means that tree_delete actually removed the node's successor so we need to swap them in the list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = binary_tree_to_list(tree)
            self.assertEqual(sorted(actual_keys), sorted(keys))

    def test_inorder_sort(self):
        array, data = random_int_array()
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            inorder_sort(array)
        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        self.assertEqual(actual_output, sorted(data))
