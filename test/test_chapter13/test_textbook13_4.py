import random
from unittest import TestCase

from hamcrest import *

from chapter13.textbook13_4 import rb_delete
from tree_util import get_binary_tree_inorder_keys, assert_red_black_tree, assert_parent_pointers_consistent, \
    get_random_red_black_tree, get_binary_tree_inorder_nodes


class TestTextbook13_4(TestCase):

    def test_rb_delete(self):
        tree, inorder_nodes, inorder_keys = get_random_red_black_tree()

        while inorder_nodes:
            node = inorder_nodes.random_choice()
            inorder_keys.remove(node.key)

            rb_delete(tree, node, sentinel=tree.nil)

            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_tree_inorder_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*inorder_keys))
            inorder_nodes = get_binary_tree_inorder_nodes(tree)
