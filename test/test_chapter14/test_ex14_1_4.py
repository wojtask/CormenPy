import random
from unittest import TestCase

from chapter14.ex14_1_4 import os_key_rank
from chapter14.textbook import os_insert
from datastructures.red_black_tree import RedBlackTree, OSNode


class Ex14_1_4Test(TestCase):
    def test_os_key_rank(self):
        keys = random.sample(range(1000), 20)
        tree = RedBlackTree(nil=OSNode(None))
        for key in keys:
            os_insert(tree, OSNode(key))
        for i, key in enumerate(sorted(keys)):
            rank = os_key_rank(tree.root, key)
            self.assertEqual(rank, i + 1)
