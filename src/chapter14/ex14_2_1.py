from chapter13.textbook import rb_predecessor, rb_successor
from chapter14.textbook import os_left_rotate, os_right_rotate
from datastructures.red_black_tree import Red, Black


def effective_os_minimum(T):
    return T.root.min


def effective_os_maximum(T):
    return T.root.max


def effective_os_predecessor(T, x):
    return x.pred


def effective_os_successor(T, x):
    return x.succ


def effective_os_insert(T, z):
    y = T.nil
    x = T.root
    while x is not T.nil:
        x.size += 1
        y = x
        if z.key < x.key:
            if z.key < x.min.key:
                x.min = z
            x = x.left
        else:
            if z.key > x.max.key:
                x.max = z
            x = x.right
    z.p = y
    if y is T.nil:
        T.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = Red
    z.size = 1
    z.min = z.max = z
    effective_os_insert_fixup(T, z)
    z.pred = rb_predecessor(z, sentinel=T.nil)
    if z.pred is not T.nil:
        z.pred.succ = z
    z.succ = rb_successor(z, sentinel=T.nil)
    if z.succ is not T.nil:
        z.succ.pred = z


def effective_os_insert_fixup(T, z):
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
                    effective_os_left_rotate(T, z)
                z.p.color = Black
                z.p.p.color = Red
                effective_os_right_rotate(T, z.p.p)
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
                    effective_os_right_rotate(T, z)
                z.p.color = Black
                z.p.p.color = Red
                effective_os_left_rotate(T, z.p.p)
    T.root.color = Black


def effective_os_left_rotate(T, x):
    os_left_rotate(T, x)
    if x.left is not T.nil:
        x.min = x.left.min
    else:
        x.min = x
    if x.right is not T.nil:
        x.max = x.right.max
    else:
        x.max = x
    y = x.p
    y.min = x.min  # x is y's left child
    if y.right is not T.nil:
        y.max = y.right.max


def effective_os_right_rotate(T, x):
    os_right_rotate(T, x)
    if x.left is not T.nil:
        x.min = x.left.min
    else:
        x.min = x
    if x.right is not T.nil:
        x.max = x.right.max
    else:
        x.max = x
    y = x.p
    if y.left is not T.nil:
        y.min = y.left.min
    y.max = x.max  # x is y's right child


def effective_os_delete(T, z):
    if z.left is T.nil or z.right is T.nil:
        y = z
    else:
        y = rb_successor(z, T.nil)
    p = rb_predecessor(y, T.nil)
    s = rb_successor(y, T.nil)
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
        z.data = y.data
    _update_additional_fields(T, y)
    if y.color == Black:
        effective_os_delete_fixup(T, x)
    if p is not T.nil:
        p.succ = s
    if s is not T.nil:
        s.pred = p
    return y


def _update_additional_fields(tree, y):
    while y is not tree.nil:
        y.size -= 1
        if y.left.min is not tree.nil:
            y.min = y.left.min
        else:
            y.min = y
        if y.right.max is not tree.nil:
            y.max = y.right.max
        else:
            y.max = y
        y = y.p


def effective_os_delete_fixup(T, x):
    while x is not T.root and x.color == Black:
        if x is x.p.left:
            w = x.p.right
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                effective_os_left_rotate(T, x.p)
                w = x.p.right
            if w.left.color == Black and w.right.color == Black:
                w.color = Red
                x = x.p
            else:
                if w.right.color == Black:
                    w.left.color = Black
                    w.color = Red
                    effective_os_right_rotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Black
                w.right.color = Black
                effective_os_left_rotate(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                effective_os_right_rotate(T, x.p)
                w = x.p.left
            if w.right.color == Black and w.left.color == Black:
                w.color = Red
                x = x.p
            else:
                if w.left.color == Black:
                    w.right.color = Black
                    w.color = Red
                    effective_os_left_rotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Black
                w.left.color = Black
                effective_os_right_rotate(T, x.p)
                x = T.root
    x.color = Black