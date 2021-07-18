import copy
import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter12.textbook12_1 import inorder_tree_walk
from datastructures.array import Array
from tree_util import get_random_binary_search_tree, get_binary_tree_inorder_keys


class TestTextbook12_1(TestCase):

    def test_inorder_tree_walk(self):
        tree, inorder_nodes, inorder_keys = get_random_binary_search_tree(min_size=0)
        original = copy.deepcopy(tree)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            inorder_tree_walk(tree.root)

        actual_output = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_that(actual_output, is_(equal_to(inorder_keys)))
        original_keys = get_binary_tree_inorder_keys(original)
        assert_that(original_keys, is_(equal_to(inorder_keys)))
