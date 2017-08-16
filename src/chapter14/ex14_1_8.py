from chapter14.textbook import os_insert, os_delete, os_rank
from datastructures.array import Array
from datastructures.red_black_tree import RedBlackTree, OSNode
from util import between


def os_search(T, k):
    x = T.root
    while x is not T.nil and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def intersecting_chords(C):
    n = C.length // 2
    P = Array.of_length(n)
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
