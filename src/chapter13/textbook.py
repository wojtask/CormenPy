from chapter13.ex13_2_1 import right_rotate
from datastructures.red_black_tree import Red, Black


def rb_minimum(x, sentinel=None):
    while x.left is not sentinel:
        x = x.left
    return x


def rb_maximum(x, sentinel=None):
    while x.right is not sentinel:
        x = x.right
    return x


def rb_predecessor(x, sentinel=None):
    if x.left is not sentinel:
        return rb_maximum(x.left, sentinel)
    y = x.p
    while y is not sentinel and x is y.left:
        x = y
        y = y.p
    return y


def rb_successor(x, sentinel=None):
    if x.right is not sentinel:
        return rb_minimum(x.right, sentinel)
    y = x.p
    while y is not sentinel and x is y.right:
        x = y
        y = y.p
    return y


def left_rotate(T, x, sentinel=None):
    y = x.right
    x.right = y.left
    if y.left is not sentinel:
        y.left.p = x
    y.p = x.p
    if x.p is sentinel:
        T.root = y
    else:
        if x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
    y.left = x
    x.p = y


def rb_insert(T, z, sentinel=None):
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
    z.color = Red
    rb_insert_fixup(T, z, sentinel)


def rb_insert_fixup(T, z, sentinel=None):
    while z.p.color == Red:
        if z.p is z.p.p.left:
            y = z.p.p.right
            if y.color == Red:
                z.p.color = Black
                y.color = Black
                z.p.p.color = Red
                z = z.p.p
            else:
                if z is z.p.right:
                    z = z.p
                    left_rotate(T, z, sentinel)
                z.p.color = Black
                z.p.p.color = Red
                right_rotate(T, z.p.p, sentinel)
        else:
            y = z.p.p.left
            if y.color == Red:
                z.p.color = Black
                y.color = Black
                z.p.p.color = Red
                z = z.p.p
            else:
                if z is z.p.left:
                    z = z.p
                    right_rotate(T, z, sentinel)
                z.p.color = Black
                z.p.p.color = Red
                left_rotate(T, z.p.p, sentinel)
    T.root.color = Black


def rb_delete(T, z, sentinel=None):
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
    if y.color == Black:
        rb_delete_fixup(T, x, sentinel)
    return y


def rb_delete_fixup(T, x, sentinel=None):
    while x is not T.root and x.color == Black:
        if x is x.p.left:
            w = x.p.right
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                left_rotate(T, x.p, sentinel)
                w = x.p.right
            if w.left.color == Black and w.right.color == Black:
                w.color = Red
                x = x.p
            else:
                if w.right.color == Black:
                    w.left.color = Black
                    w.color = Red
                    right_rotate(T, w, sentinel)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Black
                w.right.color = Black
                left_rotate(T, x.p, sentinel)
                x = T.root
        else:
            w = x.p.left
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                right_rotate(T, x.p, sentinel)
                w = x.p.left
            if w.right.color == Black and w.left.color == Black:
                w.color = Red
                x = x.p
            else:
                if w.left.color == Black:
                    w.right.color = Black
                    w.color = Red
                    left_rotate(T, w, sentinel)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Black
                w.left.color = Black
                right_rotate(T, x.p, sentinel)
                x = T.root
    x.color = Black
