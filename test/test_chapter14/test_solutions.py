import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.ex14_1_3 import iterative_os_select
from chapter14.ex14_1_4 import os_key_rank
from chapter14.ex14_1_5 import os_successor
from chapter14.ex14_1_7 import os_count_inversions
from tree_util import get_random_os_tree, get_binary_tree_nodes


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
