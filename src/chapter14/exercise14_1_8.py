from chapter13.textbook13_2 import rb_search
from chapter14.textbook14_1 import os_insert, os_rank, os_delete
from datastructures.array import Array
from datastructures.red_black_tree import RedBlackTree, OSNode
from util import between


def os_search(T, k):
    return rb_search(T.root, k, sentinel=T.nil)


def intersecting_chords(C):
    n = C.length // 2
    P = Array.indexed(1, n)
    for k in between(1, n):
        P[k] = 0
    intersections = 0
    T = RedBlackTree(sentinel=OSNode(None))
    for k in between(1, 2 * n):
        j = C[k]
        if P[j] == 0:
            P[j] = k
            os_insert(T, OSNode(k))
        else:
            x = os_search(T, P[j])
            intersections = intersections + T.root.size - os_rank(T, x)
            os_delete(T, x)
    return intersections
