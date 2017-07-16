import random
from unittest import TestCase

from chapter12.ex12_3_1 import recursive_tree_insert_wrapper
from datastructures.binary_tree import Node, BinaryTree
from test.test_datastructures.tree_util import binary_tree_to_list, assert_binary_search_tree, \
    assert_parent_pointers_consistent


class Ex12_3_1Test(TestCase):
    def test_recursive_tree_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = BinaryTree()
        for key in keys:
            recursive_tree_insert_wrapper(tree, Node(key))
            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
        actual_keys = binary_tree_to_list(tree)
        self.assertEqual(sorted(actual_keys), sorted(keys))
