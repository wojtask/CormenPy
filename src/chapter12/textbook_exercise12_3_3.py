from chapter12.textbook12_1 import inorder_tree_walk
from chapter12.textbook12_3 import tree_insert
from datastructures.binary_tree import BinaryTree, Node
from util import between


def inorder_sort(A):
    T = BinaryTree()
    for i in between(1, A.length):
        tree_insert(T, Node(A[i]))
    inorder_tree_walk(T.root)
