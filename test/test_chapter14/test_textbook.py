import random
from unittest import TestCase

from chapter14.textbook import os_insert, os_delete, os_select, os_rank
from datastructures.red_black_tree import RedBlackTree, OSNode
from test.test_datastructures.tree_util import assert_parent_pointers_consistent, binary_tree_to_list, assert_os_tree


class Chapter14Test(TestCase):
    def test_os_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = RedBlackTree(nil=OSNode(None))
        for key in keys:
            os_insert(tree, OSNode(key))
            assert_os_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
        actual_keys = binary_tree_to_list(tree, sentinel=tree.nil)
        self.assertEqual(sorted(actual_keys), sorted(keys))

    def test_os_delete(self):
        # first we build an order statistic tree using os_insert
        n = 20
        tree = RedBlackTree(nil=OSNode(None))
        keys = [random.randrange(1000) for _ in range(n)]
        nodes = [OSNode(key) for key in keys]
        for node in nodes:
            os_insert(tree, node)

        # then we are removing nodes from the tree in random order
        random.shuffle(nodes)
        for i, node in enumerate(nodes):
            y = os_delete(tree, node)
            if y is not node:
                # this means that os_delete actually removed the node's successor so we need to swap them in nodes list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_os_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            actual_keys = binary_tree_to_list(tree, sentinel=tree.nil)
            self.assertEqual(len(actual_keys), n - i - 1)
            self.assertTrue(all(x in keys for x in actual_keys))

    def test_os_select(self):
        n = 20
        keys = [random.randrange(1000) for _ in range(n)]
        tree = RedBlackTree(nil=OSNode(None))
        for key in keys:
            os_insert(tree, OSNode(key))
        sorted_keys = sorted(keys)
        for i in range(n):
            x = os_select(tree.root, i + 1)
            self.assertEqual(x.key, sorted_keys[i])

    def test_os_rank(self):
        n = 20
        nodes = [OSNode(random.randrange(1000)) for _ in range(n)]
        tree = RedBlackTree(nil=OSNode(None))
        for node in nodes:
            os_insert(tree, node)
        sorted_nodes = sorted(nodes, key=lambda x: x.key)
        for i in range(n):
            rank = os_rank(tree, sorted_nodes[i])
            self.assertEqual(rank, i + 1)
