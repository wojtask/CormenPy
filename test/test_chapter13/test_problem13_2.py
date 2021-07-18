import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter13.problem13_2 import joinable_rb_insert, joinable_rb_delete, rb_join
from datastructures.red_black_tree import Black, RedBlackTree, Node
from tree_util import assert_red_black_tree, assert_parent_pointers_consistent, get_binary_tree_inorder_keys, \
    get_random_red_black_tree, get_binary_tree_inorder_nodes


def calculate_black_height(node):
    black_height = 0
    while node:
        if node.color == Black:
            black_height += 1
        node = node.left  # it doesn't matter which path we choose as long as the tree fulfills property 5
    return black_height


class TestProblem13_2(TestCase):

    def test_joinable_rb_insert(self):
        keys = get_random_array(min_size=1, max_size=20)
        tree = RedBlackTree(sentinel=None)
        tree.bh = 0

        for key in keys:
            joinable_rb_insert(tree, Node(key))

            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))
        actual_black_height = calculate_black_height(tree.root)
        assert_that(tree.bh, is_(equal_to(actual_black_height)))

    def test_joinable_rb_delete(self):
        tree, inorder_nodes, inorder_keys = get_random_red_black_tree(sentinel=None)
        tree.bh = calculate_black_height(tree.root)

        while inorder_nodes:
            node = random.choice(inorder_nodes)
            inorder_keys.remove(node.key)

            joinable_rb_delete(tree, node)

            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_tree_inorder_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*inorder_keys))
            actual_black_height = calculate_black_height(tree.root)
            assert_that(tree.bh, is_(equal_to(actual_black_height)))
            inorder_nodes = get_binary_tree_inorder_nodes(tree)

    def test_rb_join(self):
        tree1, _, inorder_keys1 = get_random_red_black_tree(black_height=random.randint(0, 4),
                                                            min_value=0, max_value=999, sentinel=None)
        tree1.bh = calculate_black_height(tree1.root)
        middle_key = random.randint(1000, 1999)
        x = Node(middle_key)
        tree2, _, inorder_keys2 = get_random_red_black_tree(black_height=random.randint(0, 4),
                                                            min_value=2000, max_value=2999, sentinel=None)
        tree2.bh = calculate_black_height(tree2.root)

        actual_joined_tree = rb_join(tree1, x, tree2)

        assert_red_black_tree(actual_joined_tree)
        actual_keys = get_binary_tree_inorder_keys(actual_joined_tree)
        assert_that(actual_keys, contains_exactly(*inorder_keys1, middle_key, *inorder_keys2))
