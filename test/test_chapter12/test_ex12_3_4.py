import random
from unittest import TestCase

from chapter12.ex12_3_4 import safe_tree_delete
from test.test_datastructures.tree_util import binary_tree_to_list, assert_binary_search_tree, \
    assert_parent_pointers_consistent, build_random_binary_search_tree


class Ex12_3_4Test(TestCase):
    def test_safe_tree_delete(self):
        tree, nodes, keys = build_random_binary_search_tree()
        random.shuffle(nodes)
        for i, node in enumerate(nodes):
            safe_tree_delete(tree, node)
            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = binary_tree_to_list(tree)
            self.assertEqual(len(actual_keys), len(nodes) - i - 1)
            self.assertTrue(all(x in keys for x in actual_keys))
