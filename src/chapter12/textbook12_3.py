from chapter12.textbook12_2 import tree_successor


def tree_insert(T, z):
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        T.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z


def tree_delete(T, z):
    if z.left is None or z.right is None:
        y = z
    else:
        y = tree_successor(z)
    if y.left is not None:
        x = y.left
    else:
        x = y.right
    if x is not None:
        x.p = y.p
    if y.p is None:
        T.root = x
    else:
        if y is y.p.left:
            y.p.left = x
        else:
            y.p.right = x
    if y is not z:
        z.key = y.key
        z.data = y.data
    return y
