import random
from unittest import TestCase

from chapter13.pr13_4 import treap_insert
from datastructures.treap import Treap, Node
from test.test_datastructures.tree_util import assert_treap, binary_tree_to_list, assert_parent_pointers_consistent


class Problem13_4Test(TestCase):
    def test_treap_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        treap = Treap()
        for key in keys:
            treap_insert(treap, Node(key))
            assert_treap(treap)
            assert_parent_pointers_consistent(treap)
        actual_keys = binary_tree_to_list(treap)
        self.assertEqual(sorted(actual_keys), sorted(keys))
