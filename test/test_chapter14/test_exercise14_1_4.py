import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_1_4 import os_key_rank
from tree_util import get_random_os_tree, get_binary_tree_inorder_nodes


class TestExercise14_1_4(TestCase):

    def test_os_key_rank(self):
        tree, inorder_nodes, inorder_keys = get_random_os_tree()
        key_to_find = random.choice(inorder_keys)

        actual_rank = os_key_rank(tree.root, key_to_find)

        expected_ranks = [i for i, key in enumerate(inorder_keys, start=1) if key == key_to_find]
        assert_that(actual_rank, is_in(expected_ranks))
        actual_nodes = get_binary_tree_inorder_nodes(tree)
        assert_that(actual_nodes, is_(equal_to(inorder_nodes)))
