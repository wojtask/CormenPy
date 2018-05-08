from chapter13.exercise13_2_1 import right_rotate
from chapter13.textbook13_2 import left_rotate
from datastructures.red_black_tree import Red, Black


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
