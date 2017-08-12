from chapter13.ex13_2_1 import right_rotate
from chapter13.textbook import left_rotate
from datastructures.red_black_tree import Black, RedBlackTree, Red


def rb_join_point(T1, T2):
    y = T1.root
    b = T1.bh
    while b > T2.bh:
        if y.right is not None:
            y = y.right
        else:
            y = y.left
        if y is None or y.color == Black:
            b = b - 1
    return y


def rb_symmetric_join_point(T1, T2):
    y = T2.root
    b = T2.bh
    while b > T1.bh:
        if y.left is not None:
            y = y.left
        else:
            y = y.right
        if y is None or y.color == Black:
            b = b - 1
    return y


def rb_join(T1, x, T2):
    T = RedBlackTree(sentinel=None)
    if T1.bh >= T2.bh:
        if T2.root is None:
            _rb_insert(T1, x)
            return T1
        T.root = x
        T.bh = T1.bh
        y = rb_join_point(T1, T2)
        x.left = y
        x.right = T2.root
        if y is not T1.root:
            if y is y.p.left:
                y.p.left = x
            else:
                y.p.right = x
            T.root = T1.root
            x.p = y.p
        T2.root.p = y.p = x
    else:
        if T1.root is None:
            _rb_insert(T2, x)
            return T2
        T.root = x
        T.bh = T2.bh
        y = rb_symmetric_join_point(T1, T2)
        x.right = y
        x.left = T1.root
        if y is not T2.root:
            if y is y.p.right:
                y.p.right = x
            else:
                y.p.left = x
            T.root = T2.root
            x.p = y.p
        T1.root.p = y.p = x
    x.color = Red
    _rb_insert_fixup(T, x)
    return T


def _rb_insert(T, z):
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
    z.left = None
    z.right = None
    z.color = Red
    _rb_insert_fixup(T, z)


def _rb_insert_fixup(T, z):
    while z.p is not None and z.p.color == Red:
        if z.p is z.p.p.left:
            y = z.p.p.right
            if y is not None and y.color == Red:
                z.p.color = Black
                y.color = Black
                z.p.p.color = Red
                z = z.p.p
            else:
                if z is z.p.right:
                    z = z.p
                    left_rotate(T, z)
                z.p.color = Black
                z.p.p.color = Red
                right_rotate(T, z.p.p)
        else:
            y = z.p.p.left
            if y is not None and y.color == Red:
                z.p.color = Black
                y.color = Black
                z.p.p.color = Red
                z = z.p.p
            else:
                if z is z.p.left:
                    z = z.p
                    right_rotate(T, z)
                z.p.color = Black
                z.p.p.color = Red
                left_rotate(T, z.p.p)
    if T.root.color == Red:
        T.bh = T.bh + 1
    T.root.color = Black
