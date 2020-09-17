from unittest import TestCase

from hamcrest import *

from datastructures.b_tree import BTree


class TestBTree(TestCase):
    def test_create_empty_b_tree(self):
        tree = BTree()
        assert_that(tree.root, is_(none()))
