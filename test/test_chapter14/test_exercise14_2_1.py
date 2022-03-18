import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.textbook13_2 import rb_minimum, rb_maximum, rb_predecessor, rb_successor
from chapter14.exercise14_2_1 import effective_os_insert, effective_os_minimum, effective_os_maximum, \
    effective_os_predecessor, effective_os_successor, effective_os_delete
from datastructures.red_black_tree import RedBlackTree, OSNode
from tree_util import get_binary_search_tree_inorder_nodes


class TestExercise14_2_1(TestCase):

    def test_effective_os_tree(self):
        keys = get_random_array()
        tree = RedBlackTree(sentinel=OSNode(None))
        tree.nil.min = tree.nil.max = tree.nil.pred = tree.nil.succ = tree.nil

        for key in keys:
            effective_os_insert(tree, OSNode(key))

        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)

        while inorder_nodes:
            actual_minimum = effective_os_minimum(tree)
            actual_maximum = effective_os_maximum(tree)
            expected_minimum = rb_minimum(tree.root, sentinel=tree.nil)
            expected_maximum = rb_maximum(tree.root, sentinel=tree.nil)
            assert_that(actual_minimum, is_(expected_minimum))
            assert_that(actual_maximum, is_(expected_maximum))

            node = inorder_nodes.random_choice()
            actual_predecessor = effective_os_predecessor(tree, node)
            actual_successor = effective_os_successor(tree, node)
            expected_predecessor = rb_predecessor(node, sentinel=tree.nil)
            expected_successor = rb_successor(node, sentinel=tree.nil)
            assert_that(actual_predecessor, is_(expected_predecessor))
            assert_that(actual_successor, is_(expected_successor))

            effective_os_delete(tree, node)

            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
