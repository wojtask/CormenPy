import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter18.problem18_2 import tree_2_3_4_create, tree_2_3_4_insert, tree_2_3_4_search, tree_2_3_4_delete, \
    tree_2_3_4_join, tree_2_3_4_split
from datastructures.array import Array
from datastructures.b_tree import Tree234
from util import between


def assert_2_3_4_tree(tree):
    assert_2_3_4_subtree(tree.root, min_keys=0)


def assert_2_3_4_subtree(node, min_keys):
    assert_that(node.n, is_(greater_than_or_equal_to(min_keys)))
    assert_that(node.n, is_(less_than_or_equal_to(3)))
    if node.height == 0:
        return
    assert_that(node.key[:node.n], is_(equal_to(node.key[:node.n].sort())))
    for i in between(1, node.n):
        left_child = node.c[i]
        right_child = node.c[i + 1]
        assert_that(node.key[i], is_(greater_than_or_equal_to(left_child.key[left_child.n])))
        assert_that(node.key[i], is_(less_than_or_equal_to(right_child.key[1])))
    for i in between(1, node.n + 1):
        child = node.c[i]
        assert_that(node.height, is_(equal_to(child.height + 1)))
        assert_2_3_4_subtree(child, min_keys=1)


def get_2_3_4_tree_keys(tree):
    return get_2_3_4_subtree_keys(tree.root)


def get_2_3_4_subtree_keys(node):
    if node.height == 0:
        return node.key[:node.n]
    elements = Array()
    for i in between(1, node.n):
        elements += get_2_3_4_subtree_keys(node.c[i])
        elements.append(node.key[i])
    elements += get_2_3_4_subtree_keys(node.c[node.n + 1])
    return elements


class TestProblem18_2(TestCase):

    def test_tree_2_3_4(self):
        """
        Create an empty 2-3-4 tree. Keep adding new keys to the tree, and sometimes delete an existing key. After each
        operation assert that the actual tree is 2-3-4 tree and that it has all expected keys.
        """
        tree = Tree234()
        tree_2_3_4_create(tree)
        assert_2_3_4_tree(tree)

        max_key_value = 10000
        keys = get_random_array(size=1000, max_value=max_key_value, unique=True)
        keys_in_tree = Array()
        for key in keys:
            tree_2_3_4_insert(tree, key)
            keys_in_tree.append(key)
            assert_2_3_4_tree(tree)
            actual_tree_keys = get_2_3_4_tree_keys(tree)
            assert_that(actual_tree_keys, is_(equal_to(keys_in_tree.sort())))
            if random.uniform(0, 1) <= 1 / 3:
                key_to_delete = keys_in_tree.random_choice()
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

    def test_tree_2_3_4_join_random(self):
        """
        Select a key k and create 2-3-4 trees T' and T'', s.t. for each key k' in T' and for each key k'' in T'',
        k' < k < k''. Join T' and T'' with k. Assert that the resulting tree is a valid 2-3-4 tree with all keys merged.
        """
        tree1 = Tree234()
        tree2 = Tree234()
        tree_2_3_4_create(tree1)
        tree_2_3_4_create(tree2)

        max_value = 1000
        k = random.randint(1, max_value - 1)
        keys1 = get_random_array(min_size=0, max_size=k - 1, min_value=0, max_value=k - 1, unique=True)
        keys2 = get_random_array(min_size=0, max_size=max_value - k, min_value=k + 1, max_value=max_value, unique=True)
        for key in keys1:
            tree_2_3_4_insert(tree1, key)
        for key in keys2:
            tree_2_3_4_insert(tree2, key)

        actual_tree = tree_2_3_4_join(tree1, tree2, k)

        assert_2_3_4_tree(actual_tree)
        actual_tree_keys = get_2_3_4_tree_keys(actual_tree)
        expected_tree_keys = keys1.sort() + [k] + keys2.sort()
        assert_that(actual_tree_keys, is_(equal_to(expected_tree_keys)))

    def test_tree_2_3_4_join_empty(self):
        """
        Same scenario as in test_tree_2_3_4_join_random but at least one of the trees is empty.
        """
        tree1 = Tree234()
        tree2 = Tree234()
        tree_2_3_4_create(tree1)
        tree_2_3_4_create(tree2)

        max_value = 1000
        k = random.randint(1, max_value - 1)
        r = random.random()
        max_size1 = 0 if r < 0.6 else k - 1
        max_size2 = 0 if r > 0.4 else max_value - k
        keys1 = get_random_array(min_size=0, max_size=max_size1, min_value=0, max_value=k - 1, unique=True)
        keys2 = get_random_array(min_size=0, max_size=max_size2, min_value=k + 1, max_value=max_value, unique=True)
        for key in keys1:
            tree_2_3_4_insert(tree1, key)
        for key in keys2:
            tree_2_3_4_insert(tree2, key)

        actual_tree = tree_2_3_4_join(tree1, tree2, k)

        assert_2_3_4_tree(actual_tree)
        actual_tree_keys = get_2_3_4_tree_keys(actual_tree)
        expected_tree_keys = keys1.sort() + [k] + keys2.sort()
        assert_that(actual_tree_keys, is_(equal_to(expected_tree_keys)))

    def test_tree_2_3_4_split_random(self):
        """
        Generate a random 2-3-4 tree T (create empty, then insert a random set of keys). Pick a key k in T at random.
        Split T around k and expect that returned trees T', T'' are both valid 2-3-4 trees, T' has no greater key
        than k, T'' has no less key than k, and the union of keys in T', T'', along with k, is the same set of keys
        as in T.
        """
        tree = Tree234()
        tree_2_3_4_create(tree)
        max_key_value = 10000
        keys = get_random_array(size=1000, max_value=max_key_value, unique=True)
        for key in keys:
            tree_2_3_4_insert(tree, key)
        split_key = random.choice(keys.elements)

        actual_tree1, actual_tree2 = tree_2_3_4_split(tree, split_key)

        assert_2_3_4_tree(actual_tree1)
        assert_2_3_4_tree(actual_tree2)
        actual_tree1_keys = get_2_3_4_tree_keys(actual_tree1)
        actual_tree2_keys = get_2_3_4_tree_keys(actual_tree2)
        for key in actual_tree1_keys:
            assert_that(key, is_(less_than_or_equal_to(split_key)))
        for key in actual_tree2_keys:
            assert_that(key, is_(greater_than_or_equal_to(split_key)))
        assert_that(actual_tree1_keys + [split_key] + actual_tree2_keys, contains_inanyorder(*keys))
