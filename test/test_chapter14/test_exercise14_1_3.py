import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_1_3 import iterative_os_select
from tree_util import get_random_os_tree


class TestExercise14_1_3(TestCase):

    def test_iterative_os_select(self):
        tree, nodes, keys = get_random_os_tree()
        i = random.randint(1, len(keys))

        actual_order_statistic = iterative_os_select(tree.root, i)

        assert_that(actual_order_statistic, is_in(nodes))
        expected_order_statistic = sorted(keys)[i - 1]
        assert_that(actual_order_statistic.key, is_(equal_to(expected_order_statistic)))
