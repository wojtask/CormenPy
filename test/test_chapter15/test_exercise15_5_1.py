import io
import re
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter15.exercise15_5_1 import construct_optimal_bst
from chapter15.textbook15_5 import optimal_bst
from datastructures.array import Array
from test_chapter15.test_textbook15_5 import get_probabilities_for_optimal_bst


def assert_optimal_bst_output(actual_output, root):
    n = root.length
    root_id = int(re.search(r'k(\d+) is the root', actual_output[1]).group(1))
    assert_that(root_id, is_(equal_to(root[1, n])))
    line_no = assert_child_output(actual_output, root, 1, root_id - 1, root_id, 2)
    line_no = assert_child_output(actual_output, root, root_id + 1, n, root_id, line_no + 1)
    assert_that(actual_output.length, is_(equal_to(line_no)))


def assert_child_output(actual_output, root, i, j, parent, line_no):
    comp = re.compile(r'([kd])(\d+) is the (\w+) child of k(\d+)')
    node_type = comp.search(actual_output[line_no]).group(1)
    node_id = int(comp.search(actual_output[line_no]).group(2))
    node_side = comp.search(actual_output[line_no]).group(3)
    actual_parent = int(comp.search(actual_output[line_no]).group(4))
    assert_that(actual_parent, is_(equal_to(parent)))
    if parent == j + 1:
        assert_that(node_side, is_(equal_to('left')))
    else:
        assert_that(node_side, is_(equal_to('right')))
    if i <= j:
        assert_that(node_type, is_(equal_to('k')))
        assert_that(node_id, is_(equal_to(root[i, j])))
        line_no = assert_child_output(actual_output, root, i, node_id - 1, node_id, line_no + 1)
        line_no = assert_child_output(actual_output, root, node_id + 1, j, node_id, line_no + 1)
    else:
        assert_that(node_type, is_(equal_to('d')))
        assert_that(node_id, is_(equal_to(j)))
    return line_no


class TestExercise15_5_1(TestCase):

    def test_construct_optimal_bst(self):
        p, q = get_probabilities_for_optimal_bst()
        _, root = optimal_bst(p, q, p.length)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            construct_optimal_bst(root)

        assert_that(p.is_modified(), is_(False))
        assert_that(q.is_modified(), is_(False))
        actual_output = Array(captured_output.getvalue().splitlines())
        assert_optimal_bst_output(actual_output, root)
