from chapter10.textbook import push, pop
from datastructures.array import Array
from datastructures.red_black_tree import Red, Black


def parentless_rb_insert(T, z):
    y = T.nil
    x = T.root
    path_length = _get_path_length_from_root_to_leaf(T, z)
    S = Array.of_length(path_length + 1)
    S.top = 0
    push(S, T.nil)
    while x is not T.nil:
        y = x
        push(S, y)
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
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
    parentless_rb_insert_fixup(T, S, z)


def _get_path_length_from_root_to_leaf(T, z):
    path_length = 0
    x = T.root
    while x is not T.nil:
        path_length += 1
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    return path_length


def parentless_rb_insert_fixup(T, S, z):
    p = pop(S)
    while p.color == Red:
        r = pop(S)
        if p is r.left:
            y = r.right
            if y.color == Red:
                y.color = p.color = Black
                r.color = Red
                z = r
                p = pop(S)
            else:
                if z is p.right:
                    z, p = p, z
                    parentless_rb_left_rotate(T, z, r)
                p.color = Black
                r.color = Red
                parentless_rb_right_rotate(T, r, pop(S))
        else:
            y = r.left
            if y.color is Red:
                y.color = p.color = Black
                r.color = Red
                z = r
                p = pop(S)
            else:
                if z is p.left:
                    z, p = p, z
                    parentless_rb_right_rotate(T, z, r)
                p.color = Black
                r.color = Red
                parentless_rb_left_rotate(T, r, pop(S))
    T.root.color = Black


def parentless_rb_left_rotate(T, x, p):
    y = x.right
    x.right = y.left
    if p is T.nil:
        T.root = y
    else:
        if x is p.left:
            p.left = y
        else:
            p.right = y
    y.left = x


def parentless_rb_right_rotate(T, x, p):
    y = x.left
    x.left = y.right
    if p is T.nil:
        T.root = y
    else:
        if x is p.right:
            p.right = y
        else:
            p.left = y
    y.right = x
