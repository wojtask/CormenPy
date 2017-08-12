import random
from unittest import TestCase

from hamcrest import *

from chapter13.ex13_3_6 import rb_parentless_insert
from chapter13.pr13_1 import persistent_tree_insert
from chapter13.pr13_3 import avl_insert_wrapper
from chapter13.pr13_4 import treap_insert
from datastructures import avl_tree as avl, treap as tp
from datastructures.avl_tree import AVLTree
from datastructures.binary_tree import BinaryTree
from datastructures.red_black_tree import RedBlackTree, Node
from datastructures.treap import Treap
from tree_util import assert_binary_search_tree, get_binary_tree_keys, assert_avl_tree, \
    assert_parent_pointers_consistent, assert_treap, assert_red_black_tree


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
