import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter12.textbook_exercise12_2_7 import inorder_tree_walk_
from tree_util import get_random_binary_search_tree


class TestTextbookExercise12_2_7(TestCase):

    def test_inorder_tree_walk_(self):
        tree, nodes, keys = get_random_binary_search_tree(min_size=0)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            inorder_tree_walk_(tree)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        expected_output = sorted(keys)
        assert_that(actual_output, is_(equal_to(expected_output)))
