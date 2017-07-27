from chapter12.textbook import tree_maximum


def tree_predecessor(x):
    if x.left is not None:
        return tree_maximum(x.left)
    y = x.p
    while y is not None and x is y.left:
        x = y
        y = y.p
    return y
