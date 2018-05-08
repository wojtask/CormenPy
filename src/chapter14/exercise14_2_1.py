from chapter13.textbook13_2 import rb_predecessor, rb_successor
from chapter14.textbook14_1 import os_left_rotate, os_right_rotate
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
    z.color = Red
    z.size = 1
    z.min = z.max = z
    x = y
    while x is not T.nil:
        _update_additional_fields(T, x)
        x = x.p
    effective_os_insert_fixup(T, z)
    z.pred = rb_predecessor(z, sentinel=T.nil)
    if z.pred is not T.nil:
        z.pred.succ = z
    z.succ = rb_successor(z, sentinel=T.nil)
    if z.succ is not T.nil:
        z.succ.pred = z


def _update_additional_fields(T, x):
    x.size = x.left.size + x.right.size + 1
    if x.left is not T.nil:
        x.min = x.left.min
    else:
        x.min = x
    if x.right is not T.nil:
        x.max = x.right.max
    else:
        x.max = x


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
    _update_additional_fields(T, x)
    _update_additional_fields(T, x.p)


def effective_os_right_rotate(T, x):
    os_right_rotate(T, x)
    _update_additional_fields(T, x)
    _update_additional_fields(T, x.p)


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
    w = x.p
    while w is not T.nil:
        _update_additional_fields(T, w)
        w = w.p
    if y.color == Black:
        effective_os_delete_fixup(T, x)
    if p is not T.nil:
        p.succ = s
    if s is not T.nil:
        s.pred = p
    return y


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
