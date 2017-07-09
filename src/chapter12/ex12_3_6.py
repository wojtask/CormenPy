from chapter05.ex5_1_2 import random
from chapter12.ex12_2_3 import tree_predecessor
from chapter12.textbook import tree_successor


def fair_tree_delete(T, z):
    if z.left is None or z.right is None:
        y = z
    else:
        if random(0, 1) == 0:
            y = tree_predecessor(z)
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
        if y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
    if y != z:
        z.key = y.key
        _copy_satellite_data(y, z)
    return y


def _copy_satellite_data(y, z):
    z.data = y.data
