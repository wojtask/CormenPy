import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_3_2 import open_interval_search, open_overlap
from datastructures.interval import Interval
from tree_util import get_random_interval_tree


class TestExercise14_3_2(TestCase):

    def test_open_interval_search(self):
        tree, nodes, keys = get_random_interval_tree()
        low_endpoint = random.randint(0, 949)
        high_endpoint = low_endpoint + random.randint(0, 50)
        interval = Interval(low_endpoint, high_endpoint)

        actual_found = open_interval_search(tree, interval)

        if actual_found is not tree.nil:
            assert_that(open_overlap(actual_found.int, interval))
        else:
            for node in nodes:
                assert_that(not_(open_overlap(node.int, interval)))
