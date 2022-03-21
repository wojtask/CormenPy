from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.problem13_4 import treap_insert
from datastructures.treap import Treap, Node
from tree_util import get_binary_search_tree_inorder_keys, assert_parent_pointers_consistent, assert_treap


class TestProblem13_4(TestCase):

    def test_treap_insert(self):
        keys = get_random_array()
        treap = Treap()

        for key in keys:
            treap_insert(treap, Node(key))

            assert_treap(treap)
            assert_parent_pointers_consistent(treap)

        actual_keys = get_binary_search_tree_inorder_keys(treap)
        assert_that(actual_keys, contains_inanyorder(*keys))
