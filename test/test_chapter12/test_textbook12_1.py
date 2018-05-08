import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter12.textbook12_1 import inorder_tree_walk
from tree_util import get_random_binary_search_tree


class TestTextbook12_1(TestCase):

    def test_inorder_tree_walk(self):
        tree, nodes, keys = get_random_binary_search_tree(min_size=0)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            inorder_tree_walk(tree.root)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        expected_output = sorted(keys)
        assert_that(actual_output, is_(equal_to(expected_output)))
