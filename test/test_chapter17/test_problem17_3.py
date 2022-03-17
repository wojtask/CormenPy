import random
from unittest import TestCase

from hamcrest import *

from chapter17.problem17_3 import balance_subtree
from tree_util import get_random_binary_search_tree, assert_binary_search_tree


def assign_size_attributes(node):
    node.size = 1
    if node.left:
        node.size += assign_size_attributes(node.left)
    if node.right:
        node.size += assign_size_attributes(node.right)
    return node.size


def assert_subtree_weight_balanced(node, alpha=.5):
    assert_node_weight_balanced(node, alpha)
    if node.left:
        assert_subtree_weight_balanced(node.left, alpha)
    if node.right:
        assert_subtree_weight_balanced(node.right, alpha)


def assert_node_weight_balanced(node, alpha=.5):
    left_size = node.left.size if node.left else 0
    right_size = node.right.size if node.right else 0
    assert_that(left_size, is_(less_than_or_equal_to(alpha * node.size)))
    assert_that(right_size, is_(less_than_or_equal_to(alpha * node.size)))


class TestProblem17_3(TestCase):

    def test_balance_subtree(self):
        tree, inorder_nodes, _ = get_random_binary_search_tree()
        assign_size_attributes(tree.root)
        node = inorder_nodes.random_choice()

        actual_balanced_node = balance_subtree(tree, node)

        assert_binary_search_tree(tree)
        assert_subtree_weight_balanced(actual_balanced_node)
