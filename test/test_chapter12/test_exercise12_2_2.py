from unittest import TestCase

from hamcrest import *

from chapter12.exercise12_2_2 import recursive_tree_minimum, recursive_tree_maximum
from tree_util import get_random_binary_search_tree


class TestExercise12_2_2(TestCase):

    def test_recursive_tree_minimum(self):
        tree, nodes, keys = get_random_binary_search_tree()

        actual_minimum = recursive_tree_minimum(tree.root)

        assert_that(actual_minimum, is_in(nodes))
        assert_that(actual_minimum.key, is_(equal_to(min(keys))))

    def test_recursive_tree_maximum(self):
        tree, nodes, keys = get_random_binary_search_tree()

        actual_maximum = recursive_tree_maximum(tree.root)

        assert_that(actual_maximum, is_in(nodes))
        assert_that(actual_maximum.key, is_(equal_to(max(keys))))
