from chapter10.textbook import push, stack_empty, pop
from datastructures.array import Array


def _get_tree_size(node):
    if node is None:
        return 0
    return _get_tree_size(node.left) + _get_tree_size(node.right) + 1


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
