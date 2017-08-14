import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.ex14_1_3 import iterative_os_select
from chapter14.ex14_1_4 import os_key_rank
from chapter14.ex14_1_5 import os_successor
from chapter14.ex14_1_7 import os_count_inversions
from chapter14.ex14_3_1 import interval_left_rotate
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
