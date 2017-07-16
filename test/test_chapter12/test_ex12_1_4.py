import io
from contextlib import redirect_stdout
from unittest import TestCase

from chapter12.ex12_1_4 import preorder_tree_walk, postorder_tree_walk
from datastructures.binary_tree import BinaryTree, Node


class Ex12_1_4Test(TestCase):
    def test_preorder_tree_walk(self):
        tree = BinaryTree(Node(10,
                               left=Node(4,
                                         left=Node(1)),
                               right=Node(14,
                                          left=Node(11),
                                          right=Node(19,
                                                     right=Node(20)))))
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            preorder_tree_walk(tree.root)
        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        self.assertEqual(actual_output, [10, 4, 1, 14, 11, 19, 20])

    def test_postorder_tree_walk(self):
        tree = BinaryTree(Node(10,
                               left=Node(4,
                                         left=Node(1)),
                               right=Node(14,
                                          left=Node(11),
                                          right=Node(19,
                                                     right=Node(20)))))
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            postorder_tree_walk(tree.root)
        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        self.assertEqual(actual_output, [1, 4, 11, 20, 19, 14, 10])
