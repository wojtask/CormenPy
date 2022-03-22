import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.problem13_2 import joinable_rb_insert, joinable_rb_delete, rb_join
from datastructures.red_black_tree import Color, Node, JoinableRedBlackTree
from tree_util import assert_red_black_tree, assert_parent_pointers_consistent, get_binary_search_tree_inorder_keys, \
    get_binary_search_tree_inorder_nodes, get_random_joinable_red_black_tree


def get_black_height(subtree_root):
    black_height = 0
    while subtree_root:
        if subtree_root.color == Color.BLACK:
            black_height += 1
        # it doesn't matter which path we choose as long as the tree fulfills property 5
        subtree_root = subtree_root.left
    return black_height


class TestProblem13_2(TestCase):

    def test_joinable_rb_insert(self):
        keys = get_random_array()
        tree = JoinableRedBlackTree()

        for key in keys:
            joinable_rb_insert(tree, Node(key))

            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))
        actual_black_height = get_black_height(tree.root)
        assert_that(tree.bh, is_(equal_to(actual_black_height)))

    def test_joinable_rb_delete(self):
        tree = get_random_joinable_red_black_tree()
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)

        while inorder_nodes:
            node = inorder_nodes.random_choice()
            inorder_keys.remove(node.key)

            joinable_rb_delete(tree, node)

            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_search_tree_inorder_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*inorder_keys))
            actual_black_height = get_black_height(tree.root)
            assert_that(tree.bh, is_(equal_to(actual_black_height)))
            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)

    def test_rb_join(self):
        tree1 = get_random_joinable_red_black_tree(black_height=random.randint(0, 4), min_value=0, max_value=999)
        inorder_keys1 = get_binary_search_tree_inorder_keys(tree1)
        middle_key = random.randint(1000, 1999)
        x = Node(middle_key)
        tree2 = get_random_joinable_red_black_tree(black_height=random.randint(0, 4), min_value=2000, max_value=2999)
        tree2.bh = get_black_height(tree2.root)
        inorder_keys2 = get_binary_search_tree_inorder_keys(tree2)

        actual_joined_tree = rb_join(tree1, x, tree2)

        assert_red_black_tree(actual_joined_tree)
        actual_keys = get_binary_search_tree_inorder_keys(actual_joined_tree)
        assert_that(actual_keys, contains_exactly(*inorder_keys1, middle_key, *inorder_keys2))
        actual_black_height = get_black_height(actual_joined_tree.root)
        assert_that(actual_joined_tree.bh, is_(equal_to(actual_black_height)))
