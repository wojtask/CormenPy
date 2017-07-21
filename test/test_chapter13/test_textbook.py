import random
from unittest import TestCase

from chapter13.textbook import rb_insert, rb_delete
from datastructures.red_black_tree import RedBlackTree, Node
from test.test_datastructures.tree_util import binary_tree_to_list, assert_red_black_tree, \
    assert_parent_pointers_consistent, random_red_black_tree


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
        tree, nodes, keys = random_red_black_tree()
        random.shuffle(nodes)
        for i, node in enumerate(nodes):
            keys.remove(node.key)
            y = rb_delete(tree, node)
            if y is not node:
                # this means that rb_delete actually removed the node's successor so we need to swap them in nodes list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            actual_keys = binary_tree_to_list(tree, sentinel=tree.nil)
            self.assertEqual(sorted(actual_keys), sorted(keys))
