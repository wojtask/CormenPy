from chapter13.ex13_2_1 import right_rotate
from chapter13.textbook import left_rotate, rb_successor, rb_search
from datastructures.red_black_tree import Red, Black, IntervalPomNode


def interval_pom_search(T, k):
    return rb_search(T.root, k, sentinel=T.nil)


def interval_pom_insert(T, i):
    low_endpoint_node = interval_pom_search(T, i.low)
    if low_endpoint_node is not T.nil:
        low_endpoint_node.low += 1
        y = low_endpoint_node
        while y is not T.nil:
            _update_additional_fields(y)
            y = y.p
    else:
        low_endpoint_node = IntervalPomNode(i.low)
        low_endpoint_node.low = 1
        _interval_pom_insert_node(T, low_endpoint_node)

    high_endpoint_node = interval_pom_search(T, i.high)
    if high_endpoint_node is not T.nil:
        high_endpoint_node.high += 1
        y = high_endpoint_node
        while y is not T.nil:
            _update_additional_fields(y)
            y = y.p
    else:
        high_endpoint_node = IntervalPomNode(i.high)
        high_endpoint_node.high = 1
        _interval_pom_insert_node(T, high_endpoint_node)

    return low_endpoint_node, high_endpoint_node


def _interval_pom_insert_node(T, z):
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
    z.color = Red
    z.sum = z.low - z.high
    z.max = z.low
    z.pom = z.key
    x = y
    while x is not T.nil:
        _update_additional_fields(x)
        x = x.p
    _interval_pom_insert_fixup(T, z)


def _update_additional_fields(x):
    x.sum = x.left.sum + (x.low - x.high) + x.right.sum
    x.max = max(x.left.max, x.left.sum + x.low, x.left.sum + (x.low - x.high) + x.right.max)
    if x.max == x.left.max:
        x.pom = x.left.pom
    elif x.max == x.left.sum + x.low:
        x.pom = x.key
    else:
        x.pom = x.right.pom


def interval_pom_left_rotate(T, x):
    left_rotate(T, x, sentinel=T.nil)
    _update_additional_fields(x)
    _update_additional_fields(x.p)


def interval_pom_right_rotate(T, x):
    right_rotate(T, x, sentinel=T.nil)
    _update_additional_fields(x)
    _update_additional_fields(x.p)


def _interval_pom_insert_fixup(T, z):
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
                    interval_pom_left_rotate(T, z)
                z.p.color = Black
                z.p.p.color = Red
                interval_pom_right_rotate(T, z.p.p)
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
                    interval_pom_right_rotate(T, z)
                z.p.color = Black
                z.p.p.color = Red
                interval_pom_left_rotate(T, z.p.p)
    T.root.color = Black


def interval_pom_delete(T, z1, z2):
    z1.low -= 1
    if z1.low > 0 or z1.high > 0:
        y = z1
        while y is not T.nil:
            _update_additional_fields(y)
            y = y.p
    else:
        _interval_pom_safe_delete_node(T, z1)
    z2.high -= 1
    if z2.low > 0 or z2.high > 0:
        y = z2
        while y is not T.nil:
            _update_additional_fields(y)
            y = y.p
    else:
        _interval_pom_safe_delete_node(T, z2)


def _interval_pom_safe_delete_node(T, z):
    y = _interval_pom_delete(T, z)
    if y is not z:
        if z.left is not T.nil:
            z.left.p = y
        if z.right is not T.nil:
            z.right.p = y
        if z.p is T.nil:
            T.root = y
        else:
            if z is z.p.left:
                z.p.left = y
            else:
                z.p.right = y
        _copy_all_fields(z, y)


def _copy_all_fields(z, y):
    y.key = z.key
    y.data = z.data
    y.low = z.low
    y.high = z.high
    y.sum = z.sum
    y.max = z.max
    y.pom = z.pom
    y.color = z.color
    y.left = z.left
    y.right = z.right
    y.p = z.p


def _interval_pom_delete(T, z):
    if z.left is T.nil or z.right is T.nil:
        y = z
    else:
        y = rb_successor(z, sentinel=T.nil)
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
        z.low = y.low
        z.high = y.high
    w = x.p
    while w is not T.nil:
        _update_additional_fields(w)
        w = w.p
    if y.color == Black:
        _interval_pom_delete_fixup(T, x)
    return y


def _interval_pom_delete_fixup(T, x):
    while x is not T.root and x.color == Black:
        if x is x.p.left:
            w = x.p.right
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                interval_pom_left_rotate(T, x.p)
                w = x.p.right
            if w.left.color == Black and w.right.color == Black:
                w.color = Red
                x = x.p
            else:
                if w.right.color == Black:
                    w.left.color = Black
                    w.color = Red
                    interval_pom_right_rotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Black
                w.right.color = Black
                interval_pom_left_rotate(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == Red:
                w.color = Black
                x.p.color = Red
                interval_pom_right_rotate(T, x.p)
                w = x.p.left
            if w.right.color == Black and w.left.color == Black:
                w.color = Red
                x = x.p
            else:
                if w.left.color == Black:
                    w.right.color = Black
                    w.color = Red
                    interval_pom_left_rotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Black
                w.left.color = Black
                interval_pom_right_rotate(T, x.p)
                x = T.root
    x.color = Black


def find_pom(T):
    return T.root.pom
