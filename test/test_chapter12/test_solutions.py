import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter12.ex12_1_4 import preorder_tree_walk, postorder_tree_walk
from chapter12.ex12_2_2 import recursive_tree_minimum, recursive_tree_maximum
from chapter12.ex12_2_3 import tree_predecessor
from chapter12.ex12_3_1 import recursive_tree_insert_wrapper
from chapter12.ex12_3_4 import safe_tree_delete
from chapter12.ex12_3_6 import fair_tree_delete
from chapter12.pr12_2 import bit_strings_sort
from chapter12.pr12_3 import randomly_built_tree_quicksort
from datastructures.array import Array
from datastructures.binary_tree import BinaryTree, Node
from tree_util import assert_binary_search_tree, assert_parent_pointers_consistent, \
    get_binary_tree_keys, get_random_binary_search_tree


def random_bit_string():
    return ''.join(random.choice('01') for _ in range(random.randint(1, 10)))


class Solutions12Test(TestCase):

    def setUp(self):
        self.tree = BinaryTree(Node(10,
                                    left=Node(4,
                                              left=Node(1)),
                                    right=Node(14,
                                               left=Node(11),
                                               right=Node(19,
                                                          right=Node(20)))))

    def test_preorder_tree_walk(self):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            preorder_tree_walk(self.tree.root)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(actual_output, is_(equal_to([10, 4, 1, 14, 11, 19, 20])))

    def test_postorder_tree_walk(self):
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            postorder_tree_walk(self.tree.root)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(actual_output, is_(equal_to([1, 4, 11, 20, 19, 14, 10])))

    def test_recursive_tree_minimum(self):
        tree, nodes, keys = get_random_binary_search_tree()

        actual_minimum = recursive_tree_minimum(tree.root)

        assert_that(actual_minimum, is_in(nodes))
        assert_that(actual_minimum.key, is_(equal_to(min(keys))))

    def test_recursive_tree_maximum(self):
        tree, nodes, keys = get_random_binary_search_tree()

        actual_maximum = recursive_tree_maximum(tree.root)

        assert_that(actual_maximum, is_in(nodes))
        assert_that(actual_maximum.key, is_(equal_to(max(keys))))

    def test_tree_predecessor(self):
        tree, nodes, keys = get_random_binary_search_tree()
        given_node = random.choice(nodes)

        actual_predecessor = tree_predecessor(given_node)

        if actual_predecessor is None:
            assert_that(given_node.key, is_(equal_to(min(keys))))
        else:
            assert_that(actual_predecessor, is_in(nodes))
            assert_that(actual_predecessor.key, is_(less_than_or_equal_to(given_node.key)))
            for node in nodes:
                assert_that(node.key, is_not(all_of(greater_than(actual_predecessor.key), less_than(given_node.key))))

    def test_recursive_tree_insert(self):
        keys = [random.randrange(1000) for _ in range(20)]
        tree = BinaryTree()

        for key in keys:
            recursive_tree_insert_wrapper(tree, Node(key))

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)

        actual_keys = get_binary_tree_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_safe_tree_delete(self):
        tree, nodes, keys = get_random_binary_search_tree()
        random.shuffle(nodes)

        for node in nodes:
            keys.remove(node.key)

            safe_tree_delete(tree, node)

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_tree_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*keys))

    def test_fair_tree_delete(self):
        tree, nodes, keys = get_random_binary_search_tree()
        random.shuffle(nodes)

        for i, node in enumerate(nodes):
            keys.remove(node.key)

            y = fair_tree_delete(tree, node)

            if y != node:
                # this means that tree_delete actually removed the node's successor so we need to swap them in the list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]

            assert_binary_search_tree(tree)
            assert_parent_pointers_consistent(tree)
            actual_keys = get_binary_tree_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*keys))

    def test_bit_strings_sort(self):
        n = random.randint(1, 20)
        # generate a set of random non-empty bit strings of lengths <= 10
        bit_strings = {random_bit_string() for _ in range(n)}
        array = Array(bit_strings)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            bit_strings_sort(array)

        actual_output = captured_output.getvalue().splitlines()
        expected_output = sorted(bit_strings)
        assert_that(actual_output, is_(equal_to(expected_output)))

    def test_randomly_built_tree_quicksort(self):
        array, elements = get_random_array()

        randomly_built_tree_quicksort(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
