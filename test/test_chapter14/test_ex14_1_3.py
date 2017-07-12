import random
from unittest import TestCase

from chapter14.ex14_1_3 import iterative_os_select
from chapter14.textbook import os_insert
from datastructures.red_black_tree import RedBlackTree, OSNode


class Ex14_1_3Test(TestCase):
    def test_iterative_os_select(self):
        tree_size = 20
        tree = RedBlackTree(nil=OSNode(None))
        keys = [random.randrange(1000) for _ in range(tree_size)]
        for i in range(tree_size):
            os_insert(tree, OSNode(keys[i]))
        sorted_keys = sorted(keys)
        for i in range(tree_size):
            x = iterative_os_select(tree.root, i + 1)
            self.assertEqual(x.key, sorted_keys[i])
