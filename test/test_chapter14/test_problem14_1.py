import random
from unittest import TestCase

from hamcrest import *

from chapter14.problem14_1 import interval_pom_insert, find_pom, interval_pom_delete
from chapter14.textbook14_3 import overlap
from datastructures.array import Array
from datastructures.interval import Interval
from datastructures.red_black_tree import RedBlackTree, IntervalPomNode
from tree_util import assert_interval_pom_tree
from util import between


def get_expected_poms(intervals):
    poms = set()
    max_overlaps = 0
    for i in intervals:
        overlaps = 0
        low_endpoint_interval = Interval(i.low, i.low)
        for j in intervals:
            if overlap(j, low_endpoint_interval):
                overlaps += 1
        if overlaps > max_overlaps:
            max_overlaps = overlaps
            poms = {i.low}
        elif overlaps == max_overlaps:
            poms.add(i.low)
    return poms


class TestProblem14_1(TestCase):

    def test_find_pom_tree(self):
        n = random.randint(1, 30)
        tree = RedBlackTree(sentinel=IntervalPomNode(None))
        intervals = Array()
        node_pairs = Array()
        for _ in between(1, n):
            low_endpoint = random.randint(0, 899)
            high_endpoint = low_endpoint + random.randint(0, 100)
            interval = Interval(low_endpoint, high_endpoint)
            intervals.append(interval)
            node_pair = interval_pom_insert(tree, interval)
            node_pairs.append(node_pair)
            assert_interval_pom_tree(tree)

        while node_pairs:
            actual_pom = find_pom(tree)

            expected_poms = get_expected_poms(intervals)
            assert_that(actual_pom, is_in(expected_poms))

            node_pair = node_pairs[random.randint(1, node_pairs.length)]
            node_pairs.remove(node_pair)
            interval_to_delete = Interval(node_pair[0].key, node_pair[1].key)
            intervals.remove(interval_to_delete)

            interval_pom_delete(tree, *node_pair)

            assert_interval_pom_tree(tree)
