import random
from unittest import TestCase

from hamcrest import *

from chapter13.textbook13_4 import rb_delete
from tree_util import get_binary_tree_keys, assert_red_black_tree, assert_parent_pointers_consistent, \
    get_random_red_black_tree, get_binary_tree_nodes


class TestTextbook13_4(TestCase):

    def test_rb_delete(self):
        tree, _, keys = get_random_red_black_tree()
        nodes = get_binary_tree_nodes(tree, sentinel=tree.nil)

        while nodes:
            node = random.choice(nodes)
            keys.remove(node.key)

            rb_delete(tree, node, sentinel=tree.nil)

            assert_red_black_tree(tree, sentinel=tree.nil)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
            assert_that(actual_keys, contains_inanyorder(*keys))
            nodes = get_binary_tree_nodes(tree, sentinel=tree.nil)
