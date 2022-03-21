from datastructures.array import Array
from datastructures.binary_tree import Node


class NodeWithSize(Node):
    def __init__(self, key):
        super().__init__(key)
        self.size = 0


def _subtree_inorder_keys(x):
    return Array() if x is None else _subtree_inorder_keys(x.left) + [x.key] + _subtree_inorder_keys(x.right)


def _balance_node(x, A, p, r):
    if p <= r:
        q = (p + r) // 2
        y = NodeWithSize(A[q])
        y.left = _balance_node(y, A, p, q - 1)
        y.right = _balance_node(y, A, q + 1, r)
        y.p = x
        y.size = 1
        y.size += y.left.size if y.left is not None else 0
        y.size += y.right.size if y.right is not None else 0
        return y
    return None


def balance_subtree(T, x):
    A = _subtree_inorder_keys(x)
    y = _balance_node(x.p, A, 1, A.length)
    if x.p is None:
        T.root = y
    else:
        if x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
    return y
