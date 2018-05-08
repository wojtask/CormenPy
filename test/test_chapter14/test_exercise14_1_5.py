import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_1_5 import os_successor
from tree_util import get_random_os_tree, get_binary_tree_nodes


class TestExercise14_1_5(TestCase):

    def test_os_successor(self):
        tree, nodes, keys = get_random_os_tree()
        inorder_nodes = get_binary_tree_nodes(tree, sentinel=tree.nil)
        j = random.randrange(len(inorder_nodes))
        i = random.randrange(0, len(nodes) - j)

        actual_successor = os_successor(tree, inorder_nodes[j], i)

        expected_successor = inorder_nodes[j + i]
        assert_that(actual_successor, is_(expected_successor))
