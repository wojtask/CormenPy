import random
from unittest import TestCase

from hamcrest import *

from chapter12.exercise12_3_4 import safe_tree_delete
from tree_util import get_random_binary_search_tree, assert_binary_search_tree, assert_parent_pointers_consistent, \
    get_binary_tree_keys


class TestExercise12_3_4(TestCase):

    def test_safe_tree_delete(self):
        tree, nodes, keys = get_random_binary_search_tree()
        random.shuffle(nodes)

        for node in nodes:
            keys.remove(node.key)

            safe_tree_delete(tree, node)

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_tree_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*keys))
