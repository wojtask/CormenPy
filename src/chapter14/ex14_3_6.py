import math

from chapter13.ex13_2_1 import right_rotate
from chapter13.textbook import rb_search, left_rotate, rb_successor
from datastructures.red_black_tree import Red, Black


def min_gap_insert(Q, z):
    y = Q.nil
    x = Q.root
    while x is not Q.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is Q.nil:
        Q.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
    z.left = z.right = Q.nil
    z.color = Red
    z.min_key = z.max_key = z.key
    z.min_gap = math.inf
    x = y
    while x is not Q.nil:
        _update_additional_fields(x)
        x = x.p
    min_gap_insert_fixup(Q, z)


def _update_additional_fields(x):
    x.min_key = min(x.key, x.left.min_key)
    x.max_key = max(x.key, x.right.max_key)
    x.min_gap = min(x.left.min_gap, x.right.min_gap, x.key - x.left.max_key, x.right.min_key - x.key)


def min_gap_left_rotate(Q, x):
    left_rotate(Q, x, sentinel=Q.nil)
    _update_additional_fields(x)
    _update_additional_fields(x.p)


def min_gap_right_rotate(Q, x):
    right_rotate(Q, x, sentinel=Q.nil)
    _update_additional_fields(x)
    _update_additional_fields(x.p)


def min_gap_insert_fixup(Q, z):
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
                    min_gap_left_rotate(Q, z)
                z.p.color = Black
                z.p.p.color = Red
                min_gap_right_rotate(Q, z.p.p)
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
                    min_gap_right_rotate(Q, z)
                z.p.color = Black
                z.p.p.color = Red
                min_gap_left_rotate(Q, z.p.p)
    Q.root.color = Black


def min_gap_delete(Q, z):
    if z.left is Q.nil or z.right is Q.nil:
        y = z
    else:
        y = rb_successor(z, sentinel=Q.nil)
    if y.left is not Q.nil:
        x = y.left
    else:
        x = y.right
    x.p = y.p
    if y.p is Q.nil:
        Q.root = x
    else:
        if y is y.p.left:
            y.p.left = x
        else:
            y.p.right = x
    if y is not z:
        z.key = y.key
        z.data = y.data
    w = x.p
    while w is not Q.nil:
        _update_additional_fields(w)
        w = w.p
    if y.color == Black:
        min_gap_delete_fixup(Q, x)
    return y


def min_gap_delete_fixup(Q, x):
    while x is not Q.root and x.color == Black:
        if x is x.p.left:
            w = x.p.right
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                min_gap_left_rotate(Q, x.p)
                w = x.p.right
            if w.left.color == Black and w.right.color == Black:
                w.color = Red
                x = x.p
            else:
                if w.right.color == Black:
                    w.left.color = Black
                    w.color = Red
                    min_gap_right_rotate(Q, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Black
                w.right.color = Black
                min_gap_left_rotate(Q, x.p)
                x = Q.root
        else:
            w = x.p.left
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                min_gap_right_rotate(Q, x.p)
                w = x.p.left
            if w.right.color == Black and w.left.color == Black:
                w.color = Red
                x = x.p
            else:
                if w.left.color == Black:
                    w.right.color = Black
                    w.color = Red
                    min_gap_left_rotate(Q, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Black
                w.left.color = Black
                min_gap_right_rotate(Q, x.p)
                x = Q.root
    x.color = Black


def min_gap_search(Q, k):
    return rb_search(Q.root, k, sentinel=Q.nil)


def min_gap(Q):
    return Q.root.min_gap
