import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter12.exercise12_2_3 import tree_predecessor
from tree_util import get_random_binary_search_tree, get_binary_tree_inorder_keys


class TestExercise12_2_3(TestCase):

    def test_tree_predecessor(self):
        tree, inorder_nodes, inorder_keys = get_random_binary_search_tree()
        original = copy.deepcopy(tree)
        given_node = random.choice(inorder_nodes)

        actual_predecessor = tree_predecessor(given_node)

        if not actual_predecessor:
            assert_that(given_node.key, is_(equal_to(min(inorder_keys))))
        else:
            assert_that(actual_predecessor, is_in(inorder_nodes))
            assert_that(actual_predecessor.key, is_(less_than_or_equal_to(given_node.key)))
            for node in inorder_nodes:
                assert_that(node.key, is_not(all_of(greater_than(actual_predecessor.key), less_than(given_node.key))))
        actual_tree_keys = get_binary_tree_inorder_keys(tree)
        original_tree_keys = get_binary_tree_inorder_keys(original)
        assert_that(actual_tree_keys, is_(equal_to(original_tree_keys)))
