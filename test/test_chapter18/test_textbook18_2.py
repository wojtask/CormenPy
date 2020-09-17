from unittest import TestCase

from hamcrest import *

from chapter18.textbook18_2 import b_tree_search, b_tree_create
from datastructures import b_tree
from datastructures.array import Array
from datastructures.b_tree import BTree, allocate_node, disk_write


def get_b_tree():
    child1 = allocate_node()
    child2 = allocate_node()
    child3 = allocate_node()
    root = allocate_node()
    child1.n = 1
    child1.key = Array([1])
    child1.leaf = True
    child2.n = 3
    child2.key = Array([3, 4, 5])
    child2.leaf = True
    child3.n = 2
    child3.key = Array([7, 8])
    child3.leaf = True
    root.n = 2
    root.key = Array([2, 6])
    root.leaf = False
    root.c = Array([child1, child2, child3])
    disk_write(child1)
    disk_write(child2)
    disk_write(child3)
    disk_write(root)

    # the B-tree procedures assume that the root of the B-tree is always in main memory; let's remove everything else
    b_tree.in_memory_nodes = {root}

    return BTree(root)


class TestTextbook18_2(TestCase):

    def test_b_tree_search(self):
        tree = get_b_tree()

        result = b_tree_search(tree.root, 5)

        assert_that(result, is_not(None))
        assert_that(result[0], is_(tree.root.c[2]))
        assert_that(result[1], is_(equal_to(3)))
        assert_that(b_tree.unsaved_nodes, is_(set()))

    def test_b_tree_search_unsuccessful(self):
        tree = get_b_tree()

        result = b_tree_search(tree.root, 9)

        assert_that(result, is_(None))

    def test_b_tree_create(self):
        T = BTree()

        b_tree_create(T)

        assert_that(T.root, is_(not_(None)))
        assert_that(T.root.n, is_(equal_to(0)))
        assert_that(T.root.leaf, is_(True))
        assert_that(b_tree.unsaved_nodes, is_(set()))
