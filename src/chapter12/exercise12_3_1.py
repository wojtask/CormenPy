def recursive_subtree_insert(x, z):
    if x is None:
        return z
    if z.key < x.key:
        x.left = recursive_subtree_insert(x.left, z)
        x.left.p = x
    else:
        x.right = recursive_subtree_insert(x.right, z)
        x.right.p = x
    return x


def recursive_tree_insert(T, z):
    T.root = recursive_subtree_insert(T.root, z)
