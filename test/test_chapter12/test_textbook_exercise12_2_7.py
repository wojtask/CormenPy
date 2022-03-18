import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter12.textbook_exercise12_2_7 import inorder_tree_walk_
from datastructures.array import Array
from tree_util import get_random_binary_search_tree, get_binary_search_tree_inorder_keys


class TestTextbookExercise12_2_7(TestCase):

    def test_inorder_tree_walk_(self):
        tree = get_random_binary_search_tree(min_size=0)
        original_keys = get_binary_search_tree_inorder_keys(tree)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            inorder_tree_walk_(tree)

        actual_output = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_that(actual_output, is_(equal_to(original_keys)))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, is_(equal_to(original_keys)))
