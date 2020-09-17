from unittest import TestCase

from hamcrest import *

from chapter18.textbook18_2 import b_tree_search, b_tree_create, b_tree_split_child
from datastructures import b_tree
from datastructures.array import Array
from datastructures.b_tree import BTree, allocate_node


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
    child2.key[3] = 'E'
    child2.leaf = True
    child3.n = 1
    child3.key[1] = 'G'
    child3.leaf = True
    root.n = 2
    root.key[1] = 'B'
    root.key[2] = 'F'
    root.leaf = False
    root.c = Array([child1, child2, child3])

    # the B-tree procedures assume that the root of the B-tree is always in main memory; let's remove everything else
    b_tree.in_memory_nodes = {root}
    b_tree.unsaved_nodes = set()

    return BTree(root)


class TestTextbook18_2(TestCase):

    def test_b_tree_search(self):
        tree = get_b_tree()

        result = b_tree_search(tree.root, 'E')

        assert_that(result[0], is_(tree.root.c[2]))
        assert_that(result[1], is_(equal_to(3)))
        assert_that(b_tree.unsaved_nodes, is_(set()))

    def test_b_tree_search_unsuccessful(self):
        tree = get_b_tree()

        result = b_tree_search(tree.root, 'H')

        assert_that(result, is_(none()))

    def test_b_tree_create(self):
        T = BTree()

        b_tree_create(T)

        assert_that(T.root.n, is_(equal_to(0)))
        assert_that(T.root.leaf, is_(True))
        assert_that(b_tree.unsaved_nodes, is_(set()))

    def test_b_tree_split_child(self):
        x = allocate_node()
        y = allocate_node()
        y.n = 3
        y.key[1] = 'C'
        y.key[2] = 'D'
        y.key[3] = 'E'
        y.leaf = False
        y_children = [allocate_node() for _ in range(4)]
        y.c = Array(y_children)
        x.n = 2
        x.key[1] = 'B'
        x.key[2] = 'F'
        x.leaf = False
        x.c[2] = y
        b_tree.in_memory_nodes = {x, y}
        b_tree.unsaved_nodes = set()

        b_tree_split_child(x, 2, y)

        assert_that(x.n, is_(equal_to(3)))
        assert_that(x.key.elements[:3], contains_exactly('B', 'D', 'F'))
        y1 = x.c[2]
        y2 = x.c[3]
        assert_that(y1.n, is_(equal_to(1)))
        assert_that(y1.key.elements[:1], contains_exactly('C'))
        assert_that(y1.c.elements[:2], contains_exactly(y_children[0], y_children[1]))
        assert_that(y2.n, is_(equal_to(1)))
        assert_that(y2.key.elements[:1], contains_exactly('E'))
        assert_that(y2.c.elements[:2], contains_exactly(y_children[2], y_children[3]))
        assert_that(b_tree.unsaved_nodes, is_(set()))
