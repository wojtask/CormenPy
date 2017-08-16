import io
import random
import re
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.ex14_1_3 import iterative_os_select
from chapter14.ex14_1_4 import os_key_rank
from chapter14.ex14_1_5 import os_successor
from chapter14.ex14_1_7 import os_count_inversions
from chapter14.ex14_3_1 import interval_left_rotate
from chapter14.ex14_3_2 import open_interval_search, open_overlap
from chapter14.ex14_3_3 import min_interval_search
from chapter14.ex14_3_4 import interval_search_all
from chapter14.ex14_3_5 import interval_search_exactly, interval_insert_exactly
from chapter14.pr14_2 import josephus_simulate, josephus
from chapter14.textbook import overlap
from datastructures.interval import Interval
from datastructures.red_black_tree import RedBlackTree, IntervalNode
from tree_util import get_random_os_tree, get_binary_tree_nodes, get_random_interval_tree, get_binary_tree_keys


def pick_node_with_right_child(nodes, tree):
    random.shuffle(nodes)
    node = tree.nil
    i = 0
    while i < len(nodes):
        node = nodes[i]
        if node.right is not tree.nil:
            break
        i += 1
    return node


class Solutions14Test(TestCase):

    def test_iterative_os_select(self):
        tree, nodes, keys = get_random_os_tree()
        i = random.randint(1, len(keys))

        actual_order_statistic = iterative_os_select(tree.root, i)

        assert_that(actual_order_statistic, is_in(nodes))
        expected_order_statistic = sorted(keys)[i - 1]
        assert_that(actual_order_statistic.key, is_(equal_to(expected_order_statistic)))

    def test_os_key_rank(self):
        tree, nodes, keys = get_random_os_tree()
        key_to_find = random.choice(keys)

        actual_rank = os_key_rank(tree.root, key_to_find)

        sorted_keys = sorted(keys)
        expected_ranks = [i + 1 for i, key in enumerate(sorted_keys) if key == key_to_find]
        assert_that(actual_rank, is_in(expected_ranks))

    def test_os_successor(self):
        tree, nodes, keys = get_random_os_tree()
        inorder_nodes = get_binary_tree_nodes(tree, sentinel=tree.nil)
        j = random.randrange(len(inorder_nodes))
        i = random.randrange(0, len(nodes) - j)

        actual_successor = os_successor(tree, inorder_nodes[j], i)

        expected_successor = inorder_nodes[j + i]
        assert_that(actual_successor, is_(expected_successor))

    def test_os_count_inversions(self):
        array, elements = get_random_array()

        actual_inversions = os_count_inversions(array)

        expected_inversions = sum(len([y for y in elements[i + 1:] if y < x]) for i, x in enumerate(elements))
        assert_that(actual_inversions, is_(equal_to(expected_inversions)))

    def test_interval_left_rotate(self):
        tree, nodes, keys = get_random_interval_tree()
        node = pick_node_with_right_child(nodes, tree)  # node is for sure != tree.nil as the tree has black_height = 3

        interval_left_rotate(tree, node)

        actual_inorder_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
        assert_that(actual_inorder_keys, is_(equal_to(sorted(keys))))
        expected_node_max = max(node.int.high, node.left.max, node.right.max)
        assert_that(node.max, is_(equal_to(expected_node_max)))
        node_parent = node.p
        expected_node_parent_max = max(node_parent.int.high, node.max, node_parent.right.max)
        assert_that(node_parent.max, is_(equal_to(expected_node_parent_max)))

    def test_open_interval_search(self):
        tree, nodes, keys = get_random_interval_tree()
        low_endpoint = random.randint(0, 949)
        high_endpoint = low_endpoint + random.randint(0, 50)
        endpoints = [low_endpoint, high_endpoint]
        interval = Interval(min(endpoints), max(endpoints))

        actual_found = open_interval_search(tree, interval)

        if actual_found is not tree.nil:
            assert_that(open_overlap(actual_found.int, interval))
        else:
            for node in nodes:
                assert_that(not_(open_overlap(node.int, interval)))

    def test_min_interval_search(self):
        tree, nodes, keys = get_random_interval_tree()
        low_endpoint = random.randint(0, 949)
        high_endpoint = low_endpoint + random.randint(0, 50)
        endpoints = [low_endpoint, high_endpoint]
        interval = Interval(min(endpoints), max(endpoints))

        actual_found = min_interval_search(tree, interval)

        if actual_found is not tree.nil:
            assert_that(overlap(actual_found.int, interval))
            for node in nodes:
                if node.int.low < actual_found.int.low:
                    assert_that(not_(overlap(node.int, interval)))
        else:
            for node in nodes:
                assert_that(not_(overlap(node.int, interval)))

    def test_interval_search_all(self):
        tree, nodes, keys = get_random_interval_tree()
        low_endpoint = random.randint(0, 899)
        high_endpoint = low_endpoint + random.randint(0, 100)
        endpoints = [low_endpoint, high_endpoint]
        interval = Interval(min(endpoints), max(endpoints))

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            interval_search_all(tree, tree.root, interval)

        actual_output = captured_output.getvalue().splitlines()
        actual_intervals = []
        p = re.compile('\[(\d+), (\d+)\]')
        for line in actual_output:
            m = p.match(line)
            i = Interval(int(m.group(1)), int(m.group(2)))
            actual_intervals.append(i)

        for actual_interval in actual_intervals:
            assert_that(overlap(actual_interval, interval))

    def test_interval_search_exactly_positive(self):
        _, keys = get_random_array(max_size=100, max_value=89)
        tree = RedBlackTree(sentinel=IntervalNode(None, None))
        intervals = []

        for key in keys:
            i = Interval(key, key + random.randint(0, 10))
            intervals.append(i)
            interval_insert_exactly(tree, IntervalNode(key, i))

        interval = random.choice(intervals)

        actual_found = interval_search_exactly(tree, interval)

        assert_that(actual_found.int, is_(equal_to(interval)))

    def test_interval_search_exactly_random(self):
        _, keys = get_random_array(max_size=100, max_value=89)
        tree = RedBlackTree(sentinel=IntervalNode(None, None))
        intervals = []

        for key in keys:
            i = Interval(key, key + random.randint(0, 10))
            intervals.append(i)
            interval_insert_exactly(tree, IntervalNode(key, i))

        low_endpoint = random.randint(0, 89)
        high_endpoint = low_endpoint + random.randint(0, 10)
        interval = Interval(low_endpoint, high_endpoint)

        actual_found = interval_search_exactly(tree, interval)

        if actual_found is not tree.nil:
            assert_that(actual_found.int, is_(equal_to(interval)))
        else:
            for i in intervals:
                assert_that(interval, is_not(equal_to(i)))

    def test_josephus_simulate(self):
        n = random.randint(1, 20)
        m = random.randint(1, n)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            josephus_simulate(n, m)

        persons = list(range(1, n + 1))
        expected_permutation = []
        idx = 0
        while persons:
            idx = (idx + m) % len(persons)
            expected_permutation.append(persons.pop(idx))
        actual_permutation = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(actual_permutation, is_(equal_to(expected_permutation)))

    def test_josephus(self):
        n = random.randint(1, 20)
        m = random.randint(1, n)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            josephus(n, m)

        persons = list(range(1, n + 1))
        expected_permutation = []
        idx = 0
        while persons:
            idx = (idx + m) % len(persons)
            expected_permutation.append(persons.pop(idx))
        actual_permutation = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(actual_permutation, is_(equal_to(expected_permutation)))
