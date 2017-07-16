import random
from unittest import TestCase

from chapter14.ex14_1_5 import os_successor
from chapter14.textbook import os_insert
from datastructures.red_black_tree import RedBlackTree, OSNode


class Ex14_1_5Test(TestCase):
    def test_os_successor(self):
        n = 20
        keys = [random.randrange(1000) for _ in range(n)]
        tree = RedBlackTree(nil=OSNode(None))
        nodes = [OSNode(key) for key in keys]
        for node in nodes:
            os_insert(tree, node)

        sorted_nodes = sorted(nodes, key=lambda x: x.key)
        starting_node = random.choice(sorted_nodes[:-1])  # randomly pick node except for the maximum in the tree
        starting_node_rank = sorted_nodes.index(starting_node) + 1
        i = random.randrange(n - starting_node_rank) + 1
        successor = os_successor(tree, starting_node, i)
        self.assertEqual(successor.key, sorted_nodes[starting_node_rank - 1 + i].key)
