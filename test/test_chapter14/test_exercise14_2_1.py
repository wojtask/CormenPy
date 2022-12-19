from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.textbook13_2 import rb_minimum, rb_maximum, rb_predecessor, rb_successor
from chapter14.exercise14_2_1 import chained_os_insert, chained_os_minimum, chained_os_maximum, \
    chained_os_predecessor, chained_os_successor, chained_os_delete
from datastructures.red_black_tree import RedBlackTree, ChainedOSNode
from tree_util import get_binary_search_tree_inorder_nodes, assert_os_tree, get_binary_search_tree_inorder_keys


class TestExercise14_2_1(TestCase):

    def test_chained_os_tree(self):
        keys = get_random_array()
        tree = RedBlackTree(sentinel=ChainedOSNode(None))

        for key in keys:
            chained_os_insert(tree, ChainedOSNode(key))

        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)

        while inorder_nodes:
            assert_os_tree(tree)
            inorder_keys = get_binary_search_tree_inorder_keys(tree)
            actual_minimum = chained_os_minimum(tree)
            actual_maximum = chained_os_maximum(tree)
            expected_minimum = rb_minimum(tree.root, sentinel=tree.nil)
            expected_maximum = rb_maximum(tree.root, sentinel=tree.nil)
            assert_that(actual_minimum, is_(expected_minimum))
            assert_that(actual_maximum, is_(expected_maximum))

            node = inorder_nodes.random_choice()
            actual_predecessor = chained_os_predecessor(tree, node)
            actual_successor = chained_os_successor(tree, node)
            expected_predecessor = rb_predecessor(node, sentinel=tree.nil)
            expected_successor = rb_successor(node, sentinel=tree.nil)
            assert_that(actual_predecessor, is_(expected_predecessor))
            assert_that(actual_successor, is_(expected_successor))
            actual_keys = get_binary_search_tree_inorder_keys(tree)
            assert_that(inorder_keys, is_(equal_to(actual_keys)))

            chained_os_delete(tree, node)

            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
