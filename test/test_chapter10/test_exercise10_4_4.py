import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_4_4 import tree_walk
from datastructures.rooted_tree import Node, RootedTree


def get_rooted_tree():
    nodes = [Node(key) for key in range(7)]
    nodes[0].left_child = nodes[1]
    nodes[1].right_sibling = nodes[2]
    nodes[2].right_sibling = nodes[3]
    nodes[1].left_child = nodes[4]
    nodes[3].left_child = nodes[5]
    nodes[5].right_sibling = nodes[6]
    return RootedTree(nodes[0])


class TestExercise10_4_4(TestCase):

    def test_tree_walk(self):
        tree = get_rooted_tree()
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tree_walk(tree.root)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        expected_output = [0, 1, 4, 2, 3, 5, 6]
        assert_that(actual_output, is_(equal_to(expected_output)))
