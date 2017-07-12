import random
from unittest import TestCase

from chapter14.textbook import *
from datastructures.red_black_tree import RedBlackTree, OSNode
from test.test_datastructures.tree_util import assert_parent_pointers_consistent, binary_tree_to_list, assert_os_tree


class Chapter14Test(TestCase):
    def test_os_insert(self):
        tree_size = 20
        tree = RedBlackTree(nil=OSNode(None))
        keys = [random.randrange(1000) for _ in range(tree_size)]
        for i in range(tree_size):
            os_insert(tree, OSNode(keys[i]))
            assert_os_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
        actual_keys = binary_tree_to_list(tree, sentinel=tree.nil)
        self.assertEqual(sorted(keys), sorted(actual_keys))

    def test_os_delete(self):
        # first we build an order statistic tree using os_insert
        tree_size = 20
        tree = RedBlackTree(nil=OSNode(None))
        keys = [random.randrange(1000) for _ in range(tree_size)]
        nodes = [OSNode(key) for key in keys]
        for i in range(tree_size):
            os_insert(tree, nodes[i])

        # then we are removing nodes from the tree in random order
        random.shuffle(nodes)
        for i in range(tree_size):
            y = os_delete(tree, nodes[i])
            if y != nodes[i]:
                # this means that os_delete actually removed the node's successor so we need to swap them in nodes list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_os_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            actual_keys = binary_tree_to_list(tree, sentinel=tree.nil)
            self.assertEqual(tree_size - i - 1, len(actual_keys))
            self.assertTrue(all(x in keys for x in actual_keys))

    def test_os_select(self):
        tree_size = 20
        tree = RedBlackTree(nil=OSNode(None))
        keys = [random.randrange(1000) for _ in range(tree_size)]
        for i in range(tree_size):
            os_insert(tree, OSNode(keys[i]))
        sorted_keys = sorted(keys)
        for i in range(tree_size):
            x = os_select(tree.root, i + 1)
            self.assertEqual(sorted_keys[i], x.key)

    def test_os_rank(self):
        tree_size = 20
        tree = RedBlackTree(nil=OSNode(None))
        nodes = [OSNode(random.randrange(1000)) for _ in range(tree_size)]
        for i in range(tree_size):
            os_insert(tree, nodes[i])
        sorted_nodes = sorted(nodes, key=lambda x: x.key)
        for i in range(tree_size):
            rank = os_rank(tree, sorted_nodes[i])
            self.assertEqual(i + 1, rank)
