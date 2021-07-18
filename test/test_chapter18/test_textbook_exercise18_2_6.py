from unittest import TestCase

from hamcrest import *

from chapter18.textbook_exercise18_2_6 import b_tree_binary_search
from datastructures import b_tree
from test_chapter18.test_textbook18_2 import get_b_tree


class TestTextbookExercise18_2_6(TestCase):

    def test_b_tree_binary_search(self):
        T = get_b_tree()

        result = b_tree_binary_search(T.root, 'F')

        assert_that(result[0], is_(T.root.c[2]))
        assert_that(result[1], is_(equal_to(3)))
        assert_that(b_tree.unsaved_node_ids, is_(empty()))

    def test_b_tree_binary_search_unsuccessful(self):
        T = get_b_tree()

        result = b_tree_binary_search(T.root, 'E')

        assert_that(result, is_(none()))
