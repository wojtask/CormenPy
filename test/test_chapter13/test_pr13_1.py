import random
from unittest import TestCase

from chapter13.pr13_1 import persistent_tree_insert
from datastructures.binary_tree import BinaryTree
from test.test_datastructures.tree_util import assert_binary_search_tree, binary_tree_to_list


class Problem13_1Test(TestCase):
    def test_persistent_tree_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = BinaryTree()
        for i, key in enumerate(keys):
            new_tree = persistent_tree_insert(tree, key)
            assert_binary_search_tree(new_tree)
            actual_keys_before_insertion = binary_tree_to_list(tree)
            actual_keys_after_insertion = binary_tree_to_list(new_tree)
            self.assertEqual(sorted(actual_keys_before_insertion), sorted(keys[:i]))
            self.assertEqual(sorted(actual_keys_after_insertion), sorted(keys[:i + 1]))
            tree = new_tree
