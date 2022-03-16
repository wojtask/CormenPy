from chapter13.exercise13_2_1 import right_rotate
from chapter13.textbook13_2 import rb_successor, left_rotate
from datastructures.red_black_tree import Color


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
    if y.color == Color.BLACK:
        rb_delete_fixup(T, x, sentinel)
    return y


def rb_delete_fixup(T, x, sentinel=None):
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
                x = T.root
    x.color = Color.BLACK
