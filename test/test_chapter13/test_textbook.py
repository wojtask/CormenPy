import random
from unittest import TestCase

from chapter13.textbook import rb_insert, rb_delete
from datastructures.red_black_tree import RedBlackTree, Node
from test.test_datastructures.tree_util import binary_tree_to_list, assert_red_black_tree, \
    assert_parent_pointers_consistent, build_random_red_black_tree


class Chapter13Test(TestCase):
    def test_rb_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = RedBlackTree()
        for key in keys:
            rb_insert(tree, Node(key))
            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
        actual_keys = binary_tree_to_list(tree, sentinel=tree.nil)
        self.assertEqual(sorted(actual_keys), sorted(keys))

    def test_rb_delete(self):
        tree, nodes, keys = build_random_red_black_tree()
        random.shuffle(nodes)
        for i, node in enumerate(nodes):
            y = rb_delete(tree, nodes[i])
            if y is not nodes[i]:
                # this means that rb_delete actually removed the node's successor so we need to swap them in nodes list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            actual_keys = binary_tree_to_list(tree, sentinel=tree.nil)
            self.assertEqual(len(actual_keys), len(nodes) - i - 1)
            self.assertTrue(all(x in keys for x in actual_keys))
