from chapter13.textbook13_2 import rb_successor
from datastructures.red_black_tree import Color


def os_select(x, i):
    r = x.left.size + 1
    if i == r:
        return x
    elif i < r:
        return os_select(x.left, i)
    else:
        return os_select(x.right, i - r)


def os_rank(T, x):
    r = x.left.size + 1
    y = x
    while y is not T.root:
        if y is y.p.right:
            r += y.p.left.size + 1
        y = y.p
    return r


def os_insert(T, z):
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
    z.size = 1
    x = y
    while x is not T.nil:
        x.size += 1
        x = x.p
    os_insert_fixup(T, z)


def os_insert_fixup(T, z):
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
                    os_left_rotate(T, z)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                os_right_rotate(T, z.p.p)
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
                    os_right_rotate(T, z)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                os_left_rotate(T, z.p.p)
    T.root.color = Color.BLACK


def os_left_rotate(T, x):
    y = x.right
    x.right = y.left
    if y.left is not T.nil:
        y.left.p = x
    y.p = x.p
    if x.p is T.nil:
        T.root = y
    else:
        if x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
    y.left = x
    x.p = y
    y.size = x.size
    x.size = x.left.size + x.right.size + 1


def os_right_rotate(T, x):
    y = x.left
    x.left = y.right
    if y.right is not T.nil:
        y.right.p = x
    y.p = x.p
    if x.p is T.nil:
        T.root = y
    else:
        if x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
    y.right = x
    x.p = y
    y.size = x.size
    x.size = x.left.size + x.right.size + 1


def os_delete(T, z):
    if z.left is T.nil or z.right is T.nil:
        y = z
    else:
        y = rb_successor(z, T.nil)
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
        w.size -= 1
        w = w.p
    if y.color == Color.BLACK:
        os_delete_fixup(T, x)
    return y


def os_delete_fixup(T, x):
    while x is not T.root and x.color == Color.BLACK:
        if x is x.p.left:
            w = x.p.right
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                os_left_rotate(T, x.p)
                w = x.p.right
            if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                w.color = Color.RED
                x = x.p
            else:
                if w.right.color == Color.BLACK:
                    w.left.color = Color.BLACK
                    w.color = Color.RED
                    os_right_rotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.right.color = Color.BLACK
                os_left_rotate(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                os_right_rotate(T, x.p)
                w = x.p.left
            if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                w.color = Color.RED
                x = x.p
            else:
                if w.left.color == Color.BLACK:
                    w.right.color = Color.BLACK
                    w.color = Color.RED
                    os_left_rotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.left.color = Color.BLACK
                os_right_rotate(T, x.p)
                x = T.root
    x.color = Color.BLACK
