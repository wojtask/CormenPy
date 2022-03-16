from chapter13.textbook13_4 import rb_successor
from chapter14.exercise14_3_1 import interval_left_rotate
from chapter14.exercise14_3_5 import interval_right_rotate
from datastructures.red_black_tree import Color


def overlap(i, i_):
    return i.low <= i_.high and i_.low <= i.high


def interval_insert(T, z):
    y = T.nil
    x = T.root
    while x is not T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is T.nil:
        T.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
    z.left = z.right = T.nil
    z.color = Color.RED
    z.max = z.int.high
    x = y
    while x is not T.nil:
        _update_max_field(x)
        x = x.p
    interval_insert_fixup(T, z)


def _update_max_field(x):
    x.max = max(x.int.high, x.left.max, x.right.max)


def interval_insert_fixup(T, z):
    while z.p.color == Color.RED:
        if z.p is z.p.p.left:
            y = z.p.p.right
            if y.color == Color.RED:
                z.p.color = Color.BLACK
                y.color = Color.BLACK
                z.p.p.color = Color.RED
                z = z.p.p
            else:
                if z is z.p.right:
                    z = z.p
                    interval_left_rotate(T, z)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                interval_right_rotate(T, z.p.p)
        else:
            y = z.p.p.left
            if y.color == Color.RED:
                z.p.color = Color.BLACK
                y.color = Color.BLACK
                z.p.p.color = Color.RED
                z = z.p.p
            else:
                if z is z.p.left:
                    z = z.p
                    interval_right_rotate(T, z)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                interval_left_rotate(T, z.p.p)
    T.root.color = Color.BLACK


def interval_delete(T, z):
    if z.left is T.nil or z.right is T.nil:
        y = z
    else:
        y = rb_successor(z, sentinel=T.nil)
    if y.left is not T.nil:
        x = y.left
    else:
        x = y.right
    x.p = y.p
    if y.p is T.nil:
        T.root = x
    else:
        if y is y.p.left:
            y.p.left = x
        else:
            y.p.right = x
    if y is not z:
        z.key = y.key
        z.int = y.int
    w = x.p
    while w is not T.nil:
        _update_max_field(w)
        w = w.p
    if y.color == Color.BLACK:
        interval_delete_fixup(T, x)
    return y


def interval_delete_fixup(T, x):
    while x is not T.root and x.color == Color.BLACK:
        if x is x.p.left:
            w = x.p.right
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                interval_left_rotate(T, x.p)
                w = x.p.right
            if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                w.color = Color.RED
                x = x.p
            else:
                if w.right.color == Color.BLACK:
                    w.left.color = Color.BLACK
                    w.color = Color.RED
                    interval_right_rotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.right.color = Color.BLACK
                interval_left_rotate(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                interval_right_rotate(T, x.p)
                w = x.p.left
            if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                w.color = Color.RED
                x = x.p
            else:
                if w.left.color == Color.BLACK:
                    w.right.color = Color.BLACK
                    w.color = Color.RED
                    interval_left_rotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.left.color = Color.BLACK
                interval_right_rotate(T, x.p)
                x = T.root
    x.color = Color.BLACK


def interval_search(T, i):
    x = T.root
    while x is not T.nil and not overlap(i, x.int):
        if x.left is not T.nil and x.left.max >= i.low:
            x = x.left
        else:
            x = x.right
    return x
