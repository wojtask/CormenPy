from chapter13.exercise13_2_1 import right_rotate
from chapter13.textbook13_2 import left_rotate, rb_successor
from datastructures.red_black_tree import Black, RedBlackTree, Red, Node


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
            joinable_rb_insert(T1, x)
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
            joinable_rb_insert(T2, x)
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
    joinable_rb_insert_fixup(T, x)
    return T


def joinable_rb_insert(T, z):
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
    joinable_rb_insert_fixup(T, z)


def joinable_rb_insert_fixup(T, z):
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


def joinable_rb_delete(T, z):
    if z.left is None or z.right is None:
        y = z
    else:
        y = rb_successor(z)
    if y.left is not None:
        x = y.left
    else:
        x = y.right
    if x is None:
        x = Node(None)  # create a dummy node that will mimic sentinel
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
    if y.color == Black:
        joinable_rb_delete_fixup(T, x)
    if x.key is None:  # if x is the dummy node replace it with None
        if x is T.root:
            T.root = None
            T.bh = 0
        else:
            if x is x.p.left:
                x.p.left = None
            else:
                x.p.right = None
    return y


def joinable_rb_delete_fixup(T, x):
    while x is not T.root and x.color == Black:
        if x is x.p.left:
            w = x.p.right
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                left_rotate(T, x.p)
                w = x.p.right
            if (w.left is None or w.left.color == Black) and (w.right is None or w.right.color == Black):
                w.color = Red
                x = x.p
                if x is T.root:
                    T.bh = T.bh - 1
            else:
                if w.right is None or w.right.color == Black:
                    if w.left is not None:
                        w.left.color = Black
                    w.color = Red
                    right_rotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Black
                if w.right is not None:
                    w.right.color = Black
                left_rotate(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                right_rotate(T, x.p)
                w = x.p.left
            if (w.right is None or w.right.color == Black) and (w.left is None or w.left.color == Black):
                w.color = Red
                x = x.p
                if x is T.root:
                    T.bh = T.bh - 1
            else:
                if w.left is None or w.left.color == Black:
                    if w.right is not None:
                        w.right.color = Black
                    w.color = Red
                    left_rotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Black
                if w.left is not None:
                    w.left.color = Black
                right_rotate(T, x.p)
                x = T.root
    x.color = Black
