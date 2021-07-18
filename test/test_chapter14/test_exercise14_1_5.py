import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_1_5 import os_successor
from tree_util import get_random_os_tree, get_binary_tree_inorder_nodes


class TestExercise14_1_5(TestCase):

    def test_os_successor(self):
        tree, inorder_nodes, _ = get_random_os_tree()
        j = random.randint(1, inorder_nodes.length)
        i = random.randint(0, inorder_nodes.length - j)

        actual_successor = os_successor(tree, inorder_nodes[j], i)

        expected_successor = inorder_nodes[j + i]
        assert_that(actual_successor, is_(expected_successor))
        actual_nodes = get_binary_tree_inorder_nodes(tree)
        assert_that(actual_nodes, is_(equal_to(inorder_nodes)))
