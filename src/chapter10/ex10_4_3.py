from chapter10.textbook import push, stack_empty, pop
from datastructures.array import Array


def _get_tree_size(node):
    size = 1
    if node.left is not None:
        size += _get_tree_size(node.left)
    if node.right is not None:
        size += _get_tree_size(node.right)
    return size


def iterative_preorder_tree_walk(T):
    if T.root is None:
        return
    S = Array.of_length(_get_tree_size(T.root))
    S.top = 0
    push(S, T.root)
    while not stack_empty(S):
        x = pop(S)
        print(x.key)
        if x.right is not None:
            push(S, x.right)
        if x.left is not None:
            push(S, x.left)
