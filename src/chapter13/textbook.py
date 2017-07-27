from chapter13.ex13_2_1 import right_rotate
from datastructures.red_black_tree import Color, RedBlackTree


def rb_tree_minimum(T, x):
    while x.left is not T.nil:
        x = x.left
    return x


def rb_tree_successor(T, x):
    if x.right is not T.nil:
        return rb_tree_minimum(T, x.right)
    y = x.p
    while y is not T.nil and x is y.right:
        x = y
        y = y.p
    return y


def left_rotate(T, x):
    # make sure the function works correctly for binary search trees and for red-black trees
    sentinel = T.nil if isinstance(T, RedBlackTree) else None

    y = x.right
    x.right = y.left
    if y.left is not sentinel:
        y.left.p = x
    y.p = x.p
    if x.p is sentinel:
        T.root = y
    else:
        if x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
    y.left = x
    x.p = y


def rb_insert(T, z):
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
    z.left = T.nil
    z.right = T.nil
    z.color = Color.RED
    rb_insert_fixup(T, z)


def rb_insert_fixup(T, z):
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
                    left_rotate(T, z)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                right_rotate(T, z.p.p)
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
                    right_rotate(T, z)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                left_rotate(T, z.p.p)
    T.root.color = Color.BLACK


def rb_delete(T, z):
    if z.left is T.nil or z.right is T.nil:
        y = z
    else:
        y = rb_tree_successor(T, z)
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
    if y.color == Color.BLACK:
        rb_delete_fixup(T, x)
    return y


def rb_delete_fixup(T, x):
    while x is not T.root and x.color == Color.BLACK:
        if x is x.p.left:
            w = x.p.right
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                left_rotate(T, x.p)
                w = x.p.right
            if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                w.color = Color.RED
                x = x.p
            else:
                if w.right.color == Color.BLACK:
                    w.left.color = Color.BLACK
                    w.color = Color.RED
                    right_rotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.right.color = Color.BLACK
                left_rotate(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                right_rotate(T, x.p)
                w = x.p.left
            if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                w.color = Color.RED
                x = x.p
            else:
                if w.left.color == Color.BLACK:
                    w.right.color = Color.BLACK
                    w.color = Color.RED
                    left_rotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.left.color = Color.BLACK
                right_rotate(T, x.p)
                x = T.root
    x.color = Color.BLACK
