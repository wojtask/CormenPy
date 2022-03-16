from chapter13.exercise13_2_1 import right_rotate
from chapter13.textbook13_2 import left_rotate
from datastructures.red_black_tree import Color


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
    z.color = Color.RED
    rb_insert_fixup(T, z, sentinel)


def rb_insert_fixup(T, z, sentinel=None):
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
                z = z.p.p
            else:
                if z is z.p.left:
                    z = z.p
                    right_rotate(T, z, sentinel)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                left_rotate(T, z.p.p, sentinel)
    T.root.color = Color.BLACK
