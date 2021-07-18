from unittest import TestCase

from hamcrest import *

from chapter18.exercise18_3_2 import b_tree_delete
from datastructures import b_tree
from datastructures.b_tree import allocate_node, BTree


def get_b_tree():
    leaf1_1 = allocate_node(t=3)
    leaf1_1.n = 2
    leaf1_1.key[1] = 'A'
    leaf1_1.key[2] = 'B'

    leaf1_2 = allocate_node(t=3)
    leaf1_2.n = 3
    leaf1_2.key[1] = 'D'
    leaf1_2.key[2] = 'E'
    leaf1_2.key[3] = 'F'

    leaf1_3 = allocate_node(t=3)
    leaf1_3.n = 3
    leaf1_3.key[1] = 'J'
    leaf1_3.key[2] = 'K'
    leaf1_3.key[3] = 'L'
    leaf1_3.leaf = True

    leaf1_4 = allocate_node(t=3)
    leaf1_4.n = 2
    leaf1_4.key[1] = 'N'
    leaf1_4.key[2] = 'O'

    leaf2_1 = allocate_node(t=3)
    leaf2_1.n = 3
    leaf2_1.key[1] = 'Q'
    leaf2_1.key[2] = 'R'
    leaf2_1.key[3] = 'S'

    leaf2_2 = allocate_node(t=3)
    leaf2_2.n = 2
    leaf2_2.key[1] = 'U'
    leaf2_2.key[2] = 'V'

    leaf2_3 = allocate_node(t=3)
    leaf2_3.n = 2
    leaf2_3.key[1] = 'Y'
    leaf2_3.key[2] = 'Z'

    internal1 = allocate_node(t=3)
    internal1.n = 3
    internal1.leaf = False
    internal1.key[1] = 'C'
    internal1.key[2] = 'G'
    internal1.key[3] = 'M'
    internal1.c[1] = leaf1_1
    internal1.c[2] = leaf1_2
    internal1.c[3] = leaf1_3
    internal1.c[4] = leaf1_4

    internal2 = allocate_node(t=3)
    internal2.n = 2
    internal2.leaf = False
    internal2.key[1] = 'T'
    internal2.key[2] = 'X'
    internal2.c[1] = leaf2_1
    internal2.c[2] = leaf2_2
    internal2.c[3] = leaf2_3

    root = allocate_node(t=3)
    root.n = 1
    root.leaf = False
    root.key[1] = 'P'
    root.c[1] = internal1
    root.c[2] = internal2

    # the B-tree procedures assume that the root of the B-tree is always in main memory; let's remove everything else
    b_tree.in_memory_node_ids = {id(root)}
    b_tree.unsaved_node_ids = set()

    return BTree(root)


class TestExercise18_3_2(TestCase):

    def test_b_tree_delete(self):
        T = get_b_tree()

        b_tree_delete(T, 'F', t=3)
        b_tree_delete(T, 'M', t=3)
        b_tree_delete(T, 'G', t=3)
        b_tree_delete(T, 'D', t=3)
        b_tree_delete(T, 'B', t=3)

        for child in T.root.c:
            b_tree.in_memory_node_ids.add(id(child))
        assert_that(T.root.n, is_(equal_to(5)))
        assert_that(T.root.key[:5], contains_exactly('E', 'L', 'P', 'T', 'X'))
        assert_that(T.root.c[1].n, is_(equal_to(2)))
        assert_that(T.root.c[1].key[:2], contains_exactly('A', 'C'))
        assert_that(T.root.c[2].n, is_(equal_to(2)))
        assert_that(T.root.c[2].key[:2], contains_exactly('J', 'K'))
        assert_that(T.root.c[3].n, is_(equal_to(2)))
        assert_that(T.root.c[3].key[:2], contains_exactly('N', 'O'))
        assert_that(T.root.c[4].n, is_(equal_to(3)))
        assert_that(T.root.c[4].key[:3], contains_exactly('Q', 'R', 'S'))
        assert_that(T.root.c[5].n, is_(equal_to(2)))
        assert_that(T.root.c[5].key[:2], contains_exactly('U', 'V'))
        assert_that(T.root.c[6].n, is_(equal_to(2)))
        assert_that(T.root.c[6].key[:2], contains_exactly('Y', 'Z'))
        assert_that(b_tree.unsaved_node_ids, is_(empty()))
