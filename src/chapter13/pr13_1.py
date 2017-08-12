from datastructures import binary_tree as bt
from datastructures.binary_tree import BinaryTree


def new_node(k):
    return bt.ParentlessNode(k)


def copy_node(x):
    return bt.ParentlessNode(x.key, left=x.left, right=x.right)


def persistent_subtree_insert(x, k):
    if x is None:
        z = new_node(k)
    else:
        z = copy_node(x)
        if k < x.key:
            z.left = persistent_subtree_insert(x.left, k)
        else:
            z.right = persistent_subtree_insert(x.right, k)
    return z


def persistent_tree_insert(T, k):
    T_ = BinaryTree()
    T_.root = persistent_subtree_insert(T.root, k)
    return T_
