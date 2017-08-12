import random
from unittest import TestCase

from hamcrest import *

from chapter13.ex13_3_6 import rb_parentless_insert
from chapter13.pr13_1 import persistent_tree_insert
from chapter13.pr13_2 import rb_join, joinable_rb_delete, joinable_rb_insert
from chapter13.pr13_3 import avl_insert_wrapper
from chapter13.pr13_4 import treap_insert
from datastructures import avl_tree as avl, treap as tp
from datastructures.avl_tree import AVLTree
from datastructures.binary_tree import BinaryTree
from datastructures.red_black_tree import RedBlackTree, Node, Black
from datastructures.treap import Treap
from tree_util import assert_binary_search_tree, get_binary_tree_keys, assert_avl_tree, \
    assert_parent_pointers_consistent, assert_treap, assert_red_black_tree, get_random_red_black_tree


def calculate_black_height(node):
    black_height = 0
    while node is not None:
        if node.color == Black:
            black_height += 1
        node = node.left  # it doesn't matter which path we choose as long as the tree fulfills property 5
    return black_height


class Solutions13Test(TestCase):

    def test_rb_parentless_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = RedBlackTree()

        for key in keys:

            rb_parentless_insert(tree, Node(key))

            assert_red_black_tree(tree, sentinel=tree.nil)

        actual_keys = get_binary_tree_keys(tree, sentinel=tree.nil)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_persistent_tree_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = BinaryTree()

        for i, key in enumerate(keys):

            new_tree = persistent_tree_insert(tree, key)

            assert_binary_search_tree(new_tree)
            actual_keys_before_insertion = get_binary_tree_keys(tree)
            actual_keys_after_insertion = get_binary_tree_keys(new_tree)
            assert_that(actual_keys_before_insertion, contains_inanyorder(*keys[:i]))
            assert_that(actual_keys_after_insertion, contains_inanyorder(*keys[:i + 1]))
            tree = new_tree

    def test_joinable_rb_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = RedBlackTree(sentinel=None)
        tree.bh = 0

        for key in keys:

            joinable_rb_insert(tree, Node(key))

            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_tree_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))
        actual_black_height = calculate_black_height(tree.root)
        assert_that(tree.bh, is_(equal_to(actual_black_height)))

    def test_joinable_rb_delete(self):
        tree, nodes, keys = get_random_red_black_tree(black_height=4, sentinel=None)
        tree.bh = calculate_black_height(tree.root)
        random.shuffle(nodes)

        for i, node in enumerate(nodes):
            keys.remove(node.key)

            y = joinable_rb_delete(tree, node)

            if y is not node:
                # this means that rb_delete actually removed the node's successor so we need to swap them in nodes list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_tree_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*keys))
            actual_black_height = calculate_black_height(tree.root)
            assert_that(tree.bh, is_(equal_to(actual_black_height)))

    def test_rb_join(self):
        tree1, _, keys1 = get_random_red_black_tree(black_height=random.randint(0, 4), max_value=999, sentinel=None)
        tree1.bh = calculate_black_height(tree1.root)
        middle_key = random.randint(1000, 1999)
        x = Node(middle_key)
        tree2, _, keys2 = get_random_red_black_tree(black_height=random.randint(0, 4), min_value=2000, max_value=2999,
                                                    sentinel=None)
        tree2.bh = calculate_black_height(tree2.root)

        actual_joined_tree = rb_join(tree1, x, tree2)

        assert_red_black_tree(actual_joined_tree)
        actual_keys = get_binary_tree_keys(actual_joined_tree)
        assert_that(actual_keys, contains_inanyorder(*(keys1 + [middle_key] + keys2)))

    def test_avl_insert(self):

        keys = [random.randrange(1000) for _ in range(20)]
        tree = AVLTree()

        for key in keys:

            avl_insert_wrapper(tree, avl.Node(key))

            assert_avl_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_tree_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_treap_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        treap = Treap()

        for key in keys:

            treap_insert(treap, tp.Node(key))

            assert_treap(treap)
            assert_parent_pointers_consistent(treap)

        actual_keys = get_binary_tree_keys(treap)
        assert_that(actual_keys, contains_inanyorder(*keys))
