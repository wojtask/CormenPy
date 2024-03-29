import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_1_3 import iterative_os_select
from tree_util import get_random_os_tree, get_binary_search_tree_inorder_nodes, get_binary_search_tree_inorder_keys


class TestExercise14_1_3(TestCase):

    def test_iterative_os_select(self):
        tree = get_random_os_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)
        i = random.randint(1, inorder_keys.length)

        actual_order_statistic = iterative_os_select(tree.root, i)

        assert_that(actual_order_statistic, is_in(inorder_nodes))
        expected_order_statistic = inorder_keys.sort()[i]
        assert_that(actual_order_statistic.key, is_(equal_to(expected_order_statistic)))
        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(inorder_keys, is_(equal_to(actual_keys)))
