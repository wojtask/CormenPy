import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_unique_array
from chapter18.problem18_2 import tree_2_3_4_create, tree_2_3_4_insert, tree_2_3_4_search, tree_2_3_4_delete
from datastructures.b_tree import BTree
from util import between


def assert_2_3_4_tree(tree):
    assert_2_3_4_subtree(tree.root, min_keys=0)


def assert_2_3_4_subtree(node, min_keys):
    assert_that(node.n, is_(greater_than_or_equal_to(min_keys)))
    assert_that(node.n, is_(less_than_or_equal_to(3)))
    if node.height == 0:
        return
    assert_that(node.key.elements[:node.n], is_(equal_to(sorted(node.key.elements[:node.n]))))
    for i in between(1, node.n):
        left_child = node.c[i]
        right_child = node.c[i + 1]
        assert_that(node.key[i], is_(greater_than_or_equal_to(left_child.key[left_child.n])))
        assert_that(node.key[i], is_(less_than_or_equal_to(right_child.key[1])))
    for i in between(1, node.n + 1):
        child = node.c[i]
        assert_that(node.height, is_(equal_to(child.height + 1)))
        assert_2_3_4_subtree(child, min_keys=1)


def get_2_3_4_tree_elements(tree):
    return get_2_3_4_subtree_elements(tree.root)


def get_2_3_4_subtree_elements(node):
    if node.height == 0:
        return node.key.elements[:node.n]
    elements = []
    for i in between(1, node.n):
        elements += get_2_3_4_subtree_elements(node.c[i])
        elements.append(node.key[i])
    elements += get_2_3_4_subtree_elements(node.c[node.n + 1])
    return elements


class TestProblem18_2(TestCase):

    def test_tree_2_3_4(self):
        """
        Create an empty 2-3-4 tree. Keep adding new keys to the tree, and sometimes delete an existing key. After each
        operation assert that the actual tree is 2-3-4 tree and that it has all expected keys.
        """
        tree = BTree()
        tree_2_3_4_create(tree)
        assert_2_3_4_tree(tree)

        max_key_value = 10000
        keys, _ = get_random_unique_array(min_size=1000, max_size=1000, max_value=max_key_value)
        keys_in_tree = []
        for key in keys:
            tree_2_3_4_insert(tree, key)
            keys_in_tree.append(key)
            assert_2_3_4_tree(tree)
            actual_tree_elements = get_2_3_4_tree_elements(tree)
            assert_that(actual_tree_elements, is_(equal_to(sorted(keys_in_tree))))
            if random.random() <= 1 / 3:
                key_to_delete = random.choice(keys_in_tree)
                tree_2_3_4_delete(tree, key_to_delete)
                assert_2_3_4_tree(tree)
                keys_in_tree.remove(key_to_delete)
        for key in between(1, max_key_value):
            actual_result = tree_2_3_4_search(tree.root, key)
            if key in keys_in_tree:
                assert_that(actual_result, is_(not_none()))
                assert_that(actual_result[0].key[actual_result[1]], is_(equal_to(key)))
            else:
                assert_that(actual_result, is_(none()))
