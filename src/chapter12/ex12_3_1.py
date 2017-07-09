def recursive_tree_insert(x, z):
    if x is None:
        return z
    if z.key < x.key:
        x.left = recursive_tree_insert(x.left, z)
        x.left.p = x
    else:
        x.right = recursive_tree_insert(x.right, z)
        x.right.p = x
    return x


def recursive_tree_insert_wrapper(T, z):
    T.root = recursive_tree_insert(T.root, z)
