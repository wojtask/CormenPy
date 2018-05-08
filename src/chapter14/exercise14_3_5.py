from chapter13.exercise13_2_1 import right_rotate
from chapter14.exercise14_3_1 import interval_left_rotate
from datastructures.red_black_tree import Black, Red


def interval_right_rotate(T, x):
    right_rotate(T, x, T.nil)
    _update_max_field(x)
    _update_max_field(x.p)


def interval_insert_exactly(T, z):
    y = T.nil
    x = T.root
    while x is not T.nil:
        y = x
        if z.int.low < x.int.low or (z.int.low == x.int.low and z.int.high < x.int.high):
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is T.nil:
        T.root = z
    else:
        if z.int.low < y.int.low or (z.int.low == y.int.low and z.int.high < y.int.high):
            y.left = z
        else:
            y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = Red
    z.max = z.int.high
    x = y
    while x is not T.nil:
        _update_max_field(x)
        x = x.p
    interval_insert_exactly_fixup(T, z)


def _update_max_field(x):
    x.max = max(x.int.high, x.left.max, x.right.max)


def interval_insert_exactly_fixup(T, z):
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
                    interval_left_rotate(T, z)
                z.p.color = Black
                z.p.p.color = Red
                interval_right_rotate(T, z.p.p)
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
                    interval_right_rotate(T, z)
                z.p.color = Black
                z.p.p.color = Red
                interval_left_rotate(T, z.p.p)
    T.root.color = Black


def interval_search_exactly(T, i):
    x = T.root
    while x is not T.nil and x.int != i:
        if i.low < x.int.low or (i.low == x.int.low and i.high < x.int.high):
            x = x.left
        else:
            x = x.right
    return x
