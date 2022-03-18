from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.problem13_4 import treap_insert
from datastructures import treap as tp
from datastructures.treap import Treap
from tree_util import get_binary_search_tree_inorder_keys, assert_parent_pointers_consistent, assert_treap


class TestProblem13_4(TestCase):

    def test_treap_insert(self):
        keys = get_random_array(min_size=1, max_size=20)
        treap = Treap()

        for key in keys:
            treap_insert(treap, tp.Node(key))

            assert_treap(treap)
            assert_parent_pointers_consistent(treap)

        actual_keys = get_binary_search_tree_inorder_keys(treap)
        assert_that(actual_keys, contains_inanyorder(*keys))
