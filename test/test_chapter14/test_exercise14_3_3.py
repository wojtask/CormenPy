import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_3_3 import min_interval_search
from chapter14.textbook14_3 import overlap
from datastructures.interval import Interval
from tree_util import get_random_interval_tree, get_binary_tree_inorder_nodes


class TestExercise14_3_3(TestCase):

    def test_min_interval_search(self):
        tree, inorder_nodes, inorder_keys = get_random_interval_tree()
        low_endpoint = random.randint(0, 949)
        high_endpoint = low_endpoint + random.randint(0, 50)
        interval = Interval(low_endpoint, high_endpoint)

        actual_found = min_interval_search(tree, interval)

        if actual_found is not tree.nil:
            assert_that(overlap(actual_found.int, interval))
            for node in inorder_nodes:
                if node.int.low < actual_found.int.low:
                    assert_that(not overlap(node.int, interval))
        else:
            for node in inorder_nodes:
                assert_that(not overlap(node.int, interval))
        actual_nodes = get_binary_tree_inorder_nodes(tree)
        assert_that(actual_nodes, is_(equal_to(inorder_nodes)))
