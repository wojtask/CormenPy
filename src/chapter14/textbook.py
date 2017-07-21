from chapter13.textbook import rb_tree_successor
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
    while y != T.root:
        if y == y.p.right:
            r += y.p.left.size + 1
        y = y.p
    return r


def os_insert(T, z):
    y = T.nil
    x = T.root
    while x != T.nil:
        x.size += 1
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == T.nil:
        T.root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = Color.RED
    z.size = 1
    os_insert_fixup(T, z)


def os_insert_fixup(T, z):
    while z.p.color == Color.RED:
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == Color.RED:
                z.p.color = Color.BLACK
                y.color = Color.BLACK
                z.p.p.color = Color.RED
                z = z.p.p
            else:
                if z == z.p.right:
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
                if z == z.p.left:
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
        if x == x.p.left:
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
        if x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
    y.right = x
    x.p = y
    y.size = x.size
    x.size = x.left.size + x.right.size + 1


def os_delete(T, z):
    if z.left == T.nil or z.right == T.nil:
        y = z
    else:
        y = rb_tree_successor(T, z)
    if y.left != T.nil:
        x = y.left
    else:
        x = y.right
    x.p = y.p
    if y.p == T.nil:
        T.root = x
    else:
        if y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
    if y != z:
        z.key = y.key
        z.data = y.data
    _update_size_fields(T, y)
    if y.color == Color.BLACK:
        os_delete_fixup(T, x)
    return y


def _update_size_fields(tree, y):
    while y is not tree.nil:
        y.size -= 1
        y = y.p


def os_delete_fixup(T, x):
    while x != T.root and x.color == Color.BLACK:
        if x == x.p.left:
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


def _overlap(i, i_):
    return i.low <= i_.high and i_.low <= i.high


def interval_search(T, i):
    x = T.root
    while x != T.nil and not _overlap(i, x.int):
        if x.left != T.nil and x.left.max >= i.low:
            x = x.left
        else:
            x = x.right
    return x