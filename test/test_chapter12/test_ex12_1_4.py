import unittest
from contextlib import redirect_stdout

import io

from chapter12.ex12_1_4 import preorder_tree_walk, postorder_tree_walk
from datastructures.binary_tree import BinaryTree, Node


class Ex12_1_4Test(unittest.TestCase):
    def test_preorder_tree_walk_empty_tree(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            preorder_tree_walk(None)
        self.assertEqual('', captured_output.getvalue())

    def test_preorder_tree_walk(self):
        tree = BinaryTree(Node(10, data='ten',
                               left=Node(4, data='four',
                                         left=Node(1, data='one')),
                               right=Node(14, data='fourteen',
                                          left=Node(11, data='eleven'),
                                          right=Node(19, data='nineteen',
                                                     right=Node(20, data='twenty')))))
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            preorder_tree_walk(tree.root)
        self.assertEqual(['10', '4', '1', '14', '11', '19', '20'], captured_output.getvalue().splitlines())

    def test_postorder_tree_walk_empty_tree(self):
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            postorder_tree_walk(None)
        self.assertEqual('', captured_output.getvalue())

    def test_postorder_tree_walk(self):
        tree = BinaryTree(Node(10, data='ten',
                               left=Node(4, data='four',
                                         left=Node(1, data='one')),
                               right=Node(14, data='fourteen',
                                          left=Node(11, data='eleven'),
                                          right=Node(19, data='nineteen',
                                                     right=Node(20, data='twenty')))))
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            postorder_tree_walk(tree.root)
        self.assertEqual(['1', '4', '11', '20', '19', '14', '10'], captured_output.getvalue().splitlines())
