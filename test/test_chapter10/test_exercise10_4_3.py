import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_4_3 import iterative_inorder_tree_walk
from datastructures.array import Array
from tree_util import get_random_binary_search_tree


class TestExercise10_4_3(TestCase):

    def test_iterative_inorder_tree_walk(self):
        tree, _, keys = get_random_binary_search_tree(min_size=0)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            iterative_inorder_tree_walk(tree)

        actual_output = Array(int(x) for x in captured_output.getvalue().splitlines())
        expected_output = keys.sort()
        assert_that(actual_output, is_(equal_to(expected_output)))
