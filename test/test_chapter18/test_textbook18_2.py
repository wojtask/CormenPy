from unittest import TestCase

from hamcrest import *

from chapter18.textbook18_2 import b_tree_search, b_tree_create, b_tree_split_child, b_tree_insert
from datastructures import b_tree
from datastructures.array import Array
from datastructures.b_tree import BTree, allocate_node, disk_read


def get_b_tree():
    child1 = allocate_node()
    child2 = allocate_node()
    child3 = allocate_node()
    root = allocate_node()
    child1.n = 1
    child1.key[1] = 'A'
    child1.leaf = True
    child2.n = 3
    child2.key[1] = 'C'
    child2.key[2] = 'D'
    child2.key[3] = 'F'
    child2.leaf = True
    child3.n = 1
    child3.key[1] = 'H'
    child3.leaf = True
    root.n = 2
    root.key[1] = 'B'
    root.key[2] = 'G'
    root.leaf = False
    root.c[1] = child1
    root.c[2] = child2
    root.c[3] = child3

    # the B-tree procedures assume that the root of the B-tree is always in main memory; let's remove everything else
    b_tree.in_memory_nodes = {root}
    b_tree.unsaved_nodes = set()

    return BTree(root)


class TestTextbook18_2(TestCase):

    def test_b_tree_search(self):
        T = get_b_tree()

        result = b_tree_search(T.root, 'F')

        assert_that(result[0], is_(T.root.c[2]))
        assert_that(result[1], is_(equal_to(3)))
        assert_that(b_tree.unsaved_nodes, is_(set()))

    def test_b_tree_search_unsuccessful(self):
        T = get_b_tree()

        result = b_tree_search(T.root, 'E')

        assert_that(result, is_(none()))

    def test_b_tree_create(self):
        T = BTree()

        b_tree_create(T)

        assert_that(T.root.n, is_(equal_to(0)))
        assert_that(T.root.leaf, is_(True))
        assert_that(b_tree.unsaved_nodes, is_(set()))

    def test_b_tree_split_child(self):
        T = get_b_tree()
        x = T.root
        y = T.root.c[2]
        b_tree.in_memory_nodes = {x, y}

        b_tree_split_child(x, 2, y)

        assert_that(x.n, is_(equal_to(3)))
        assert_that(x.key.elements[:3], contains_exactly('B', 'D', 'G'))
        c2 = x.c[2]
        c3 = x.c[3]
        assert_that(c2.n, is_(equal_to(1)))
        assert_that(c2.key.elements[:1], contains_exactly('C'))
        assert_that(c3.n, is_(equal_to(1)))
        assert_that(c3.key.elements[:1], contains_exactly('F'))
        assert_that(b_tree.unsaved_nodes, is_(set()))

    def test_b_tree_insert_full_root(self):
        x = allocate_node()
        x.n = 3
        x.key = Array(['A', 'D', 'F'])
        x.leaf = True
        T = BTree()
        T.root = x
        b_tree.in_memory_nodes = {T.root}
        b_tree.unsaved_nodes = set()

        b_tree_insert(T, 'B')

        assert_that(T.root.n, is_(equal_to(1)))
        assert_that(T.root.key.elements[:1], contains_exactly('D'))
        c1 = T.root.c[1]
        c2 = T.root.c[2]
        assert_that(c1.n, is_(equal_to(2)))
        assert_that(c1.key.elements[:2], contains_exactly('A', 'B'))
        assert_that(c2.n, is_(equal_to(1)))
        assert_that(c2.key.elements[:1], contains_exactly('F'))
        assert_that(b_tree.unsaved_nodes, is_(set()))

    def test_b_tree_insert_nonfull_root(self):
        T = get_b_tree()

        b_tree_insert(T, 'E')

        assert_that(T.root.n, is_(equal_to(3)))
        assert_that(T.root.key.elements[:3], contains_exactly('B', 'D', 'G'))
        child1 = T.root.c[1]
        child2 = T.root.c[2]
        child3 = T.root.c[3]
        child4 = T.root.c[4]
        b_tree.in_memory_nodes = {T.root, child1, child2, child3, child4}
        assert_that(child1.n, is_(equal_to(1)))
        assert_that(child1.key.elements[:1], contains_exactly('A'))
        assert_that(child2.n, is_(equal_to(1)))
        assert_that(child2.key.elements[:1], contains_exactly('C'))
        assert_that(child3.n, is_(equal_to(2)))
        assert_that(child3.key.elements[:2], contains_exactly('E', 'F'))
        assert_that(child4.n, is_(equal_to(1)))
        assert_that(child4.key.elements[:1], contains_exactly('H'))
        assert_that(b_tree.unsaved_nodes, is_(set()))
