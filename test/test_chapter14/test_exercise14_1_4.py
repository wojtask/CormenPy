import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_1_4 import os_key_rank
from tree_util import get_random_os_tree


class TestExercise14_1_4(TestCase):

    def test_os_key_rank(self):
        tree, nodes, keys = get_random_os_tree()
        key_to_find = random.choice(keys)

        actual_rank = os_key_rank(tree.root, key_to_find)

        sorted_keys = sorted(keys)
        expected_ranks = [i + 1 for i, key in enumerate(sorted_keys) if key == key_to_find]
        assert_that(actual_rank, is_in(expected_ranks))
