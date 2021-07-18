import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_3_1 import interval_left_rotate
from tree_util import get_random_interval_tree, get_binary_tree_inorder_keys
from util import between


def pick_node_with_right_child(nodes, tree):
    random.shuffle(nodes)
    for i in between(1, nodes.length):
        node = nodes[i]
        if node.right is not tree.nil:
            return node
    return tree.nil


class TestExercise14_3_1(TestCase):

    def test_interval_left_rotate(self):
        tree, inorder_nodes, inorder_keys = get_random_interval_tree()
        node = pick_node_with_right_child(inorder_nodes, tree)  # node != tree.nil because the tree has black_height = 3

        interval_left_rotate(tree, node)

        expected_node_max = max(node.int.high, node.left.max, node.right.max)
        assert_that(node.max, is_(equal_to(expected_node_max)))
        node_parent = node.p
        expected_node_parent_max = max(node_parent.int.high, node.max, node_parent.right.max)
        assert_that(node_parent.max, is_(equal_to(expected_node_parent_max)))
        actual_inorder_keys = get_binary_tree_inorder_keys(tree)
        assert_that(actual_inorder_keys, is_(equal_to(inorder_keys)))
