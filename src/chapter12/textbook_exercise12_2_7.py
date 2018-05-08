from chapter12.textbook12_2 import tree_minimum, tree_successor
from util import between


def inorder_tree_walk_(T):
    if T.root is None:
        return
    n = _get_size(T.root)
    x = tree_minimum(T.root)
    print(x.key)
    for i in between(1, n - 1):
        x = tree_successor(x)
        print(x.key)


def _get_size(x):
    if x is None:
        return 0
    return 1 + _get_size(x.left) + _get_size(x.right)
