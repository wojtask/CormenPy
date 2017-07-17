from chapter12.textbook import tree_delete


def safe_tree_delete(T, z):
    y = tree_delete(T, z)
    if y is not z:
        if z.left is not None:
            z.left.p = y
        if z.right is not None:
            z.right.p = y
        if z.p is None:
            T.root = y
        else:
            if z is z.p.left:
                z.p.left = y
            else:
                z.p.right = y
        _copy_all_fields(z, y)


def _copy_all_fields(z, y):
    y.key = z.key
    y.data = z.data
    y.left = z.left
    y.right = z.right
    y.p = z.p
