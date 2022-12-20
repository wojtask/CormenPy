from chapter13.exercise13_2_1 import right_rotate
from chapter13.textbook13_2 import left_rotate, rb_successor
from datastructures.red_black_tree import Color


def bh_rb_insert(T, z, sentinel=None):
    y = sentinel
    x = T.root
    while x is not sentinel:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is sentinel:
        T.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
    z.left = sentinel
    z.right = sentinel
    z.color = Color.RED
    z.bh = 1
    bh_rb_insert_fixup(T, z, sentinel)


def bh_rb_insert_fixup(T, z, sentinel=None):
    while z.p.color == Color.RED:
        if z.p is z.p.p.left:
            y = z.p.p.right
            if y.color == Color.RED:
                z.p.color = Color.BLACK
                y.color = Color.BLACK
                z.p.p.color = Color.RED
                z.p.p.bh += 1
                z = z.p.p
            else:
                if z is z.p.right:
                    z = z.p
                    left_rotate(T, z, sentinel)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                right_rotate(T, z.p.p, sentinel)
        else:
            y = z.p.p.left
            if y.color == Color.RED:
                z.p.color = Color.BLACK
                y.color = Color.BLACK
                z.p.p.color = Color.RED
                z.p.p.bh += 1
                z = z.p.p
            else:
                if z is z.p.left:
                    z = z.p
                    right_rotate(T, z, sentinel)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                left_rotate(T, z.p.p, sentinel)
    T.root.color = Color.BLACK


def bh_rb_delete(T, z, sentinel=None):
    if z.left is sentinel or z.right is sentinel:
        y = z
    else:
        y = rb_successor(z, sentinel)
    if y.left is not sentinel:
        x = y.left
    else:
        x = y.right
    x.p = y.p
    if y.p is sentinel:
        T.root = x
    else:
        if y is y.p.left:
            y.p.left = x
        else:
            y.p.right = x
    if y is not z:
        z.key = y.key
        z.data = y.data
    if y.color == Color.BLACK:
        bh_rb_delete_fixup(T, x, sentinel)
    return y


def bh_rb_delete_fixup(T, x, sentinel=None):
    while x is not T.root and x.color == Color.BLACK:
        if x is x.p.left:
            w = x.p.right
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                left_rotate(T, x.p, sentinel)
                w = x.p.right
            if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                w.color = Color.RED
                x.p.bh = x.bh + 1
                x = x.p
            else:
                if w.right.color == Color.BLACK:
                    w.left.color = Color.BLACK
                    w.color = Color.RED
                    right_rotate(T, w, sentinel)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.right.color = Color.BLACK
                left_rotate(T, x.p, sentinel)
                x.p.bh = x.bh + 1
                x.p.p.bh = x.p.bh + 1
                x = T.root
        else:
            w = x.p.left
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                right_rotate(T, x.p, sentinel)
                w = x.p.left
            if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                w.color = Color.RED
                x.p.bh = x.bh + 1
                x = x.p
            else:
                if w.left.color == Color.BLACK:
                    w.right.color = Color.BLACK
                    w.color = Color.RED
                    left_rotate(T, w, sentinel)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.left.color = Color.BLACK
                right_rotate(T, x.p, sentinel)
                x.p.bh = x.bh + 1
                x.p.p.bh = x.p.bh + 1
                x = T.root
    x.color = Color.BLACK
