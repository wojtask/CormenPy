import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_3_3 import interval_search_lowest
from chapter14.textbook14_3 import overlap
from datastructures.array import Array
from datastructures.essential import Interval
from tree_util import get_random_interval_tree, get_binary_search_tree_inorder_nodes


class TestExercise14_3_3(TestCase):

    def test_interval_search_lowest(self):
        tree = get_random_interval_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_intervals = Array(node.int for node in inorder_nodes)
        low_endpoint = random.randint(0, 949)
        high_endpoint = low_endpoint + random.randint(0, 50)
        interval = Interval(low_endpoint, high_endpoint)

        actual_found = interval_search_lowest(tree, interval)

        if actual_found is not tree.nil:
            assert_that(overlap(actual_found.int, interval))
            for node in inorder_nodes:
                if node.int.low < actual_found.int.low:
                    assert_that(not overlap(node.int, interval))
        else:
            for node in inorder_nodes:
                assert_that(not overlap(node.int, interval))
        actual_nodes = get_binary_search_tree_inorder_nodes(tree)
        actual_intervals = Array(node.int for node in actual_nodes)
        assert_that(actual_intervals, is_(equal_to(inorder_intervals)))
