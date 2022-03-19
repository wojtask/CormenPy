import io
import random
import re
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_3_4 import interval_search_all
from chapter14.textbook14_3 import overlap
from datastructures.array import Array
from datastructures.interval import Interval
from tree_util import get_random_interval_tree, get_binary_search_tree_inorder_nodes


class TestExercise14_3_4(TestCase):

    def test_interval_search_all(self):
        tree = get_random_interval_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        low_endpoint = random.randint(0, 899)
        high_endpoint = low_endpoint + random.randint(0, 100)
        interval = Interval(low_endpoint, high_endpoint)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            interval_search_all(tree, tree.root, interval)

        actual_output = Array(captured_output.getvalue().splitlines())
        actual_intervals = Array()
        p = re.compile(r'\[(\d+), (\d+)]')
        for line in actual_output:
            m = p.match(line)
            i = Interval(int(m.group(1)), int(m.group(2)))
            actual_intervals.append(i)

        for actual_interval in actual_intervals:
            assert_that(overlap(actual_interval, interval))
        actual_nodes = get_binary_search_tree_inorder_nodes(tree)
        assert_that(actual_nodes, is_(equal_to(inorder_nodes)))
