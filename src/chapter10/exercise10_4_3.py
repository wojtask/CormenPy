from chapter10.textbook10_1 import stack_empty, push, pop
from datastructures.array import Array


def iterative_inorder_tree_walk(T):
    S = Array.indexed(1, _get_tree_size(T.root))
    S.top = 0
    x = T.root
    while not stack_empty(S) or x is not None:
        if x is not None:
            push(S, x)
            x = x.left
        else:
            x = pop(S)
            print(x.key)
            x = x.right


def _get_tree_size(node):
    if node is None:
        return 0
    return _get_tree_size(node.left) + _get_tree_size(node.right) + 1
