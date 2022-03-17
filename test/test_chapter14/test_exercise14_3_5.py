import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.exercise14_3_5 import interval_insert_exactly, interval_search_exactly
from datastructures.array import Array
from datastructures.interval import Interval
from datastructures.red_black_tree import RedBlackTree, IntervalNode
from tree_util import assert_interval_tree


class TestExercise14_3_5(TestCase):

    def test_interval_search_exactly_positive(self):
        keys = get_random_array(max_size=100, max_value=89)
        tree = RedBlackTree(sentinel=IntervalNode(None, None))
        intervals = Array()

        for key in keys:
            i = Interval(key, key + random.randint(0, 10))
            intervals.append(i)
            interval_insert_exactly(tree, IntervalNode(key, i))
            assert_interval_tree(tree)

        interval = intervals.random_choice()

        actual_found = interval_search_exactly(tree, interval)

        assert_that(actual_found.int, is_(equal_to(interval)))

    def test_interval_search_exactly_random(self):
        keys = get_random_array(max_size=100, max_value=89)
        tree = RedBlackTree(sentinel=IntervalNode(None, None))
        intervals = Array()

        for key in keys:
            i = Interval(key, key + random.randint(0, 10))
            intervals.append(i)
            interval_insert_exactly(tree, IntervalNode(key, i))
            assert_interval_tree(tree)

        low_endpoint = random.randint(0, 89)
        high_endpoint = low_endpoint + random.randint(0, 10)
        interval = Interval(low_endpoint, high_endpoint)

        actual_found = interval_search_exactly(tree, interval)

        if actual_found is not tree.nil:
            assert_that(actual_found.int, is_(equal_to(interval)))
        else:
            for i in intervals:
                assert_that(interval, is_not(equal_to(i)))
