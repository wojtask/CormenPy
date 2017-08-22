from chapter10.textbook import push, pop
from chapter13.ex13_3_6 import parentless_rb_right_rotate, parentless_rb_left_rotate
from chapter13.textbook import rb_successor
from datastructures import binary_tree as bt
from datastructures import red_black_tree as rb
from datastructures.array import Array
from datastructures.binary_tree import BinaryTree
from datastructures.red_black_tree import Red, Black, RedBlackTree


def new_node(k):
    return bt.ParentlessNode(k)


def copy_node(x):
    return bt.ParentlessNode(x.key, left=x.left, right=x.right)


def persistent_subtree_insert(x, k):
    if x is None:
        z = new_node(k)
    else:
        z = copy_node(x)
        if k < x.key:
            z.left = persistent_subtree_insert(x.left, k)
        else:
            z.right = persistent_subtree_insert(x.right, k)
    return z


def persistent_tree_insert(T, k):
    T_ = BinaryTree()
    T_.root = persistent_subtree_insert(T.root, k)
    return T_


def persistent_rb_insert(T, z):
    path_length = _get_path_length_from_root_to_node(T, z)
    S = Array.of_length(path_length + 1)
    S.top = 0
    y = T.nil
    x = T.root
    T_ = RedBlackTree(sentinel=T.nil)
    y_ = T_.nil
    push(S, y_)
    while x is not T.nil:
        y = x
        x_ = rb.ParentlessNode.clone(x)
        if y_ is T_.nil:
            T_.root = x_
        else:
            if x is y_.left:
                y_.left = x_
            else:
                y_.right = x_
        y_ = x_
        push(S, y_)
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    if y is T.nil:
        T_.root = z
    else:
        if z.key < y.key:
            y_.left = z
        else:
            y_.right = z
    z.left = z.right = T.nil
    z.color = Red
    _persistent_rb_insert_fixup(T_, S, z)
    return T_


def _get_path_length_from_root_to_node(T, z):
    path_length = 0
    x = T.root
    while x is not z and x is not T.nil:
        path_length += 1
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    return path_length


def _persistent_rb_insert_fixup(T, S, z):
    p = pop(S)
    while p.color == Red:
        r = pop(S)
        if p is r.left:
            y = r.right
            if y.color == Red:
                r.right = rb.ParentlessNode.clone(y)
                r.right.color = Black
                p.color = Black
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
                r.left = rb.ParentlessNode.clone(y)
                r.left.color = Black
                p.color = Black
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


def persistent_rb_delete(T, z):
    T_ = RedBlackTree()
    T_.root = T_.nil = T.nil
    if z.left is T.nil or z.right is T.nil:
        y = z
    else:
        y = rb_successor(z, T.nil)
    path_length = _get_path_length_from_root_to_node(T, y)
    S = Array.of_length(path_length + 1)
    S.top = 0
    p = T.root
    r = T.nil
    p_ = r_ = T_.nil
    push(S, p_)
    z_ = T.nil
    while p is not y:
        p_ = rb.ParentlessNode.clone(p)
        push(S, p_)
        if p is z:
            z_ = p_
        if r_ is T_.nil:
            T_.root = p_
        else:
            if p is r_.left:
                r_.left = p_
            else:
                r_.right = p_
        r = p
        r_ = p_
        if y.key < p.key:
            p = p.left
        else:
            p = p.right
    if y.left is not T.nil:
        x = y.left
    else:
        x = y.right
    if y.color == Black:
        if x is not T.nil:
            x_ = rb.ParentlessNode.clone(x)
        else:
            x_ = T.nil
        if y is T.root:
            T_.root = x_
        else:
            if y is r.left:
                p_.left = x_
            else:
                p_.right = x_
        if y is not z:
            z_.key = y.key
            z_.data = y.data
        persistent_rb_delete_fixup(T_, S, x_)
    else:
        if y is r.left:
            p_.left = x
        else:
            p_.right = x
        if y is not z:
            z_.key = y.key
            z_.data = y.data
    return T_


def persistent_rb_delete_fixup(T, S, x):
    p = pop(S)
    while x is not T.root and x.color == Black:
        r = pop(S)
        if x is p.left:
            w = rb.ParentlessNode.clone(p.right)
            p.right = w
            if w.color == Red:
                w.color = Black
                p.color = Red
                parentless_rb_left_rotate(T, p, r)
                r = w
                w = rb.ParentlessNode.clone(p.right)
                p.right = w
            if w.left.color == Black and w.right.color == Black:
                w.color = Red
                x = p
            else:
                if w.right.color == Black:
                    w.left = rb.ParentlessNode.clone(w.left)
                    w.left.color = Black
                    w.color = Red
                    parentless_rb_right_rotate(T, w, p)
                    w = p.right
                w.color = p.color
                p.color = Black
                w.right = rb.ParentlessNode.clone(w.right)
                w.right.color = Black
                parentless_rb_left_rotate(T, p, r)
                x = T.root
        else:
            w = rb.ParentlessNode.clone(p.left)
            p.left = w
            if w.color == Red:
                w.color = Black
                p.color = Red
                parentless_rb_right_rotate(T, p, r)
                r = w
                w = rb.ParentlessNode.clone(p.left)
                p.left = w
            if w.left.color == Black and w.right.color == Black:
                w.color = Red
                x = p
            else:
                if w.left.color == Black:
                    w.right = rb.ParentlessNode.clone(w.right)
                    w.right.color = Black
                    w.color = Red
                    parentless_rb_left_rotate(T, w, p)
                    w = p.left
                w.color = p.color
                p.color = Black
                w.left = rb.ParentlessNode.clone(w.left)
                w.left.color = Black
                parentless_rb_right_rotate(T, p, r)
                x = T.root
        p = r
    x.color = Black
