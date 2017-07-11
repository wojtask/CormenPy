import random
from unittest import TestCase

from chapter13.pr13_3 import avl_insert_wrapper
from datastructures.avl_tree import AVLTree, Node
from test.test_datastructures.tree_util import assert_avl_tree, binary_tree_to_list, assert_parent_pointers_consistent


class Problem13_3Test(TestCase):
    def test_avl_insert(self):
        tree_size = 20
        tree = AVLTree()
        keys = [random.randrange(1000) for _ in range(tree_size)]
        for i in range(tree_size):
            avl_insert_wrapper(tree, Node(keys[i]))
            assert_avl_tree(tree)
            assert_parent_pointers_consistent(tree)
        actual_keys = binary_tree_to_list(tree)
        self.assertEqual(sorted(keys), sorted(actual_keys))
