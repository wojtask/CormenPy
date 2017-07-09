def recursive_tree_minimum(x):
    if x.left is not None:
        return recursive_tree_minimum(x.left)
    else:
        return x


def recursive_tree_maximum(x):
    if x.right is not None:
        return recursive_tree_maximum(x.right)
    else:
        return x
