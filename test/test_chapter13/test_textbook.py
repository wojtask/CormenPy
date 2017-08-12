import random
from unittest import TestCase

from hamcrest import *

from chapter13.textbook import rb_insert, rb_delete
from datastructures.red_black_tree import RedBlackTree, Node
from tree_util import get_binary_tree_keys, assert_red_black_tree, assert_parent_pointers_consistent, \
    get_random_red_black_tree


class Textbook13Test(TestCase):

    def test_rb_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = RedBlackTree()

        for key in keys:

            rb_insert(tree, Node(key), sentinel=tree.nil)

            assert_red_black_tree(tree, sentinel=tree.nil)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)

        actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_rb_delete(self):
        tree, nodes, keys = get_random_red_black_tree()
        random.shuffle(nodes)

        for i, node in enumerate(nodes):
            keys.remove(node.key)

            y = rb_delete(tree, node, sentinel=tree.nil)

            if y is not node:
                # this means that rb_delete actually removed the node's successor so we need to swap them in nodes list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_red_black_tree(tree, sentinel=tree.nil)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
            assert_that(actual_keys, contains_inanyorder(*keys))
