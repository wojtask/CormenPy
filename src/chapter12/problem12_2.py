from datastructures.binary_tree import RadixNode, BinaryTree
from util import between


def bit_strings_sort(S):
    tree = BinaryTree()
    for i in between(1, S.length):
        _radix_tree_insert(tree, S[i])
    _preorder_radix_tree_walk(tree.root, '')


def _radix_tree_insert(T, key):
    if T.root is None:
        T.root = RadixNode()
    x = T.root
    for d in key:
        if d == '0':
            if x.left is None:
                x.left = RadixNode()
            x = x.left
        else:
            if x.right is None:
                x.right = RadixNode()
            x = x.right
    x.in_tree = True


def _preorder_radix_tree_walk(x, key):
    if x is not None:
        if x.in_tree:
            print(key)
        _preorder_radix_tree_walk(x.left, key + '0')
        _preorder_radix_tree_walk(x.right, key + '1')
