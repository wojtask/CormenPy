import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_3_1 import interval_left_rotate
from tree_util import get_random_interval_tree, get_binary_tree_keys


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


class TestExercise14_3_1(TestCase):

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
