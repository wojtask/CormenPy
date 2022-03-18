import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_4_5 import stackless_inorder_tree_walk
from datastructures.array import Array
from tree_util import get_random_binary_search_tree, get_binary_search_tree_inorder_keys


class TestExercise10_4_5(TestCase):

    def test_stackless_inorder_tree_walk(self):
        tree = get_random_binary_search_tree(min_size=0)
        original_keys = get_binary_search_tree_inorder_keys(tree)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            stackless_inorder_tree_walk(tree)

        actual_output = Array(int(x) for x in captured_output.getvalue().splitlines())
        expected_output = original_keys.sort()
        assert_that(actual_output, is_(equal_to(expected_output)))
