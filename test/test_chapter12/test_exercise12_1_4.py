import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter12.exercise12_1_4 import preorder_tree_walk, postorder_tree_walk
from datastructures.array import Array
from datastructures.binary_tree import BinaryTree, Node


class TestExercise12_1_4(TestCase):

    def setUp(self):
        self.tree = BinaryTree(Node(10,
                                    left=Node(4,
                                              left=Node(1)),
                                    right=Node(14,
                                               left=Node(11),
                                               right=Node(19,
                                                          right=Node(20)))))

    def test_preorder_tree_walk(self):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            preorder_tree_walk(self.tree.root)

        actual_output = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_that(actual_output, is_(equal_to(Array([10, 4, 1, 14, 11, 19, 20]))))

    def test_postorder_tree_walk(self):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            postorder_tree_walk(self.tree.root)

        actual_output = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_that(actual_output, is_(equal_to(Array([1, 4, 11, 20, 19, 14, 10]))))
