from unittest import TestCase

from hamcrest import *

from chapter18.exercise18_2_3 import b_tree_minimum, b_tree_predecessor
from datastructures import b_tree
from test_chapter18.test_textbook18_2 import get_b_tree


class TestExercise18_2_3(TestCase):

    def test_b_tree_minimum(self):
        T = get_b_tree()

        actual_minimum = b_tree_minimum(T.root)

        assert_that(actual_minimum, is_(equal_to('A')))

    def test_b_tree_predecessor_in_subtree(self):
        T = get_b_tree()

        actual_predecessor = b_tree_predecessor(T, T.root, 2)
        assert_that(actual_predecessor, is_(equal_to('F')))

    def test_b_tree_predecessor_in_the_same_node(self):
        T = get_b_tree()

        b_tree.in_memory_nodes = {T.root, T.root.c[2]}
        actual_predecessor = b_tree_predecessor(T, T.root.c[2], 3)
        assert_that(actual_predecessor, is_(equal_to('D')))

    def test_b_tree_predecessor_in_ancestor(self):
        T = get_b_tree()

        b_tree.in_memory_nodes = {T.root, T.root.c[3]}
        actual_predecessor = b_tree_predecessor(T, T.root.c[3], 1)
        assert_that(actual_predecessor, is_(equal_to('G')))

    def test_b_tree_predecessor_nonexistent(self):
        T = get_b_tree()

        b_tree.in_memory_nodes = {T.root, T.root.c[1]}
        actual_predecessor = b_tree_predecessor(T, T.root.c[1], 1)
        assert_that(actual_predecessor, is_(none()))
