from datastructures.binary_tree import BinaryTree, Node
from util import between


def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)


def tree_search(x, k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right is not None:
        x = x.right
    return x


def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y


def _get_size(x):
    if x is None:
        return 0
    return 1 + _get_size(x.left) + _get_size(x.right)


def inorder_tree_walk_(T):
    if T.root is None:
        return
    n = _get_size(T.root)
    x = tree_minimum(T.root)
    print(x.key)
    for i in between(1, n - 1):
        x = tree_successor(x)
        print(x.key)
    
    
def tree_insert(T, z):
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        T.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z


def tree_delete(T, z):
    if z.left is None or z.right is None:
        y = z
    else:
        y = tree_successor(z)
    if y.left is not None:
        x = y.left
    else:
        x = y.right
    if x is not None:
        x.p = y.p
    if y.p is None:
        T.root = x
    else:
        if y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
    if y != z:
        z.key = y.key
        _copy_satellite_data(y, z)
    return y


def _copy_satellite_data(y, z):
    z.data = y.data


def inorder_sort(A):
    T = BinaryTree()
    for i in between(1, A.length):
        tree_insert(T, Node(A[i]))
    inorder_tree_walk(T.root)
