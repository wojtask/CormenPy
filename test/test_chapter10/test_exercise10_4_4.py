import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_4_4 import tree_walk
from datastructures.array import Array
from datastructures.rooted_tree import Node, RootedTree
from util import between


def get_rooted_tree():
    nodes = Array(Node(key) for key in between(1, 7))
    nodes[1].left_child = nodes[2]
    nodes[2].right_sibling = nodes[3]
    nodes[3].right_sibling = nodes[4]
    nodes[2].left_child = nodes[5]
    nodes[4].left_child = nodes[6]
    nodes[6].right_sibling = nodes[7]
    return RootedTree(nodes[1])


class TestExercise10_4_4(TestCase):

    def test_tree_walk(self):
        tree = get_rooted_tree()
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tree_walk(tree.root)

        actual_output = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_that(actual_output, is_(equal_to(Array(1, 2, 5, 3, 4, 6, 7))))
