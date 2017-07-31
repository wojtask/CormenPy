import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter12.textbook import inorder_tree_walk, tree_search, iterative_tree_search, tree_minimum, tree_maximum, \
    tree_successor, inorder_tree_walk_, tree_insert, tree_delete, inorder_sort
from datastructures.binary_tree import BinaryTree, Node
from tree_util import get_binary_tree_keys, assert_binary_search_tree, \
    assert_parent_pointers_consistent, get_random_binary_search_tree


class Textbook12Test(TestCase):

    def test_inorder_tree_walk(self):
        tree, nodes, keys = get_random_binary_search_tree()
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            inorder_tree_walk(tree.root)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        expected_output = sorted(keys)
        assert_that(actual_output, is_(equal_to(expected_output)))

    def test_tree_search(self):
        tree, nodes, keys = get_random_binary_search_tree(min_size=10, max_size=20, max_value=20)
        key_to_find = random.randint(0, 20)

        actual_node = tree_search(tree.root, key_to_find)

        if key_to_find in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(key_to_find, is_(equal_to(actual_node.key)))
        else:
            assert_that(actual_node, is_(none()))

    def test_iterative_tree_search(self):
        tree, nodes, keys = get_random_binary_search_tree(min_size=10, max_size=20, max_value=20)
        key_to_find = random.randint(0, 20)

        actual_node = iterative_tree_search(tree.root, key_to_find)

        if key_to_find in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(key_to_find, is_(equal_to(actual_node.key)))
        else:
            assert_that(actual_node, is_(none()))

    def test_tree_minimum(self):
        tree, nodes, keys = get_random_binary_search_tree()

        actual_minimum = tree_minimum(tree.root)

        assert_that(actual_minimum, is_in(nodes))
        assert_that(actual_minimum.key, is_(equal_to(min(keys))))

    def test_tree_maximum(self):
        tree, nodes, keys = get_random_binary_search_tree()

        actual_maximum = tree_maximum(tree.root)

        assert_that(actual_maximum, is_in(nodes))
        assert_that(actual_maximum.key, is_(equal_to(max(keys))))

    def test_tree_successor(self):
        tree, nodes, keys = get_random_binary_search_tree()
        given_node = random.choice(nodes)

        actual_successor = tree_successor(given_node)

        if actual_successor is None:
            assert_that(given_node.key, is_(equal_to(max(keys))))
        else:
            assert_that(actual_successor, is_in(nodes))
            assert_that(actual_successor.key, is_(greater_than_or_equal_to(given_node.key)))
            for node in nodes:
                assert_that(node.key, is_not(all_of(greater_than(given_node.key), less_than(actual_successor.key))))

    def test_inorder_tree_walk_(self):
        tree, nodes, keys = get_random_binary_search_tree()
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            inorder_tree_walk_(tree)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        expected_output = sorted(keys)
        assert_that(actual_output, is_(equal_to(expected_output)))

    def test_tree_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = BinaryTree()

        for key in keys:

            tree_insert(tree, Node(key))

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_tree_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_tree_delete(self):
        tree, nodes, keys = get_random_binary_search_tree()
        random.shuffle(nodes)

        for i, node in enumerate(nodes):
            keys.remove(node.key)

            y = tree_delete(tree, node)

            if y is not node:
                # this means that tree_delete actually removed the node's successor so we need to swap them in the list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_tree_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*keys))

    def test_inorder_sort(self):
        array, data = get_random_array()
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            inorder_sort(array)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(actual_output, is_(equal_to(sorted(data))))
