from chapter12.textbook import tree_delete


def safe_tree_delete(T, z):
    y = tree_delete(T, z)
    if y != z:
        z.left.p = z.right.p = y
        if z.p is not None:
            if z == z.p.left:
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
