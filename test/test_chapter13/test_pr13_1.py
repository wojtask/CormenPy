import random
from unittest import TestCase

from chapter13.pr13_1 import persistent_tree_insert
from datastructures.binary_tree import BinaryTree
from test.test_datastructures.tree_util import assert_binary_search_tree, binary_tree_to_list


class Problem13_1Test(TestCase):
    def test_persistent_tree_insert(self):
        tree_size = 20
        tree = BinaryTree()
        keys = [random.randrange(1000) for _ in range(tree_size)]
        for i in range(tree_size):
            new_tree = persistent_tree_insert(tree, keys[i])
            assert_binary_search_tree(new_tree)
            actual_keys_before_insertion = binary_tree_to_list(tree)
            actual_keys_after_insertion = binary_tree_to_list(new_tree)
            self.assertEqual(sorted(keys[:i]), sorted(actual_keys_before_insertion))
            self.assertEqual(sorted(keys[:i + 1]), sorted(actual_keys_after_insertion))
            tree = new_tree
