from chapter14.textbook import os_insert, os_rank
from datastructures.red_black_tree import RedBlackTree, OSNode
from util import between


def os_count_inversions(A):
    n = A.length
    inversions = 0
    tree = RedBlackTree(sentinel=OSNode(None))
    for i in between(1, n):
        x = OSNode(A[i])
        os_insert(tree, x)
        inversions += i - os_rank(tree, x)
    return inversions
