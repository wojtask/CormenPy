from chapter13.exercise13_2_1 import right_rotate
from chapter13.textbook13_2 import rb_search, left_rotate, rb_successor
from datastructures.red_black_tree import Color, IntervalPomNode


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
    z.color = Color.RED
    z.overlap = z.low - z.high
    z.max_overlap = z.low
    z.pom = z.key
    x = y
    while x is not T.nil:
        _update_additional_fields(x)
        x = x.p
    _interval_pom_insert_fixup(T, z)


def _update_additional_fields(x):
    x.overlap = x.left.overlap + (x.low - x.high) + x.right.overlap
    x.max_overlap = max(x.left.max_overlap, x.left.overlap + x.low, x.left.overlap + (x.low - x.high) + x.right.max_overlap)
    if x.max_overlap == x.left.max_overlap:
        x.pom = x.left.pom
    elif x.max_overlap == x.left.overlap + x.low:
        x.pom = x.key
    else:
        x.pom = x.right.pom


def _interval_pom_insert_fixup(T, z):
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
                    interval_pom_left_rotate(T, z)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                interval_pom_right_rotate(T, z.p.p)
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
                    interval_pom_right_rotate(T, z)
                z.p.color = Color.BLACK
                z.p.p.color = Color.RED
                interval_pom_left_rotate(T, z.p.p)
    T.root.color = Color.BLACK


def interval_pom_left_rotate(T, x):
    left_rotate(T, x, sentinel=T.nil)
    _update_additional_fields(x)
    _update_additional_fields(x.p)


def interval_pom_right_rotate(T, x):
    right_rotate(T, x, sentinel=T.nil)
    _update_additional_fields(x)
    _update_additional_fields(x.p)


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
    if y.color == Color.BLACK:
        _interval_pom_delete_fixup(T, x)
    return y


def _interval_pom_delete_fixup(T, x):
    while x is not T.root and x.color == Color.BLACK:
        if x is x.p.left:
            w = x.p.right
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                interval_pom_left_rotate(T, x.p)
                w = x.p.right
            if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                w.color = Color.RED
                x = x.p
            else:
                if w.right.color == Color.BLACK:
                    w.left.color = Color.BLACK
                    w.color = Color.RED
                    interval_pom_right_rotate(T, w)
                    w = x.p.right
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.right.color = Color.BLACK
                interval_pom_left_rotate(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == Color.RED:
                w.color = Color.BLACK
                x.p.color = Color.RED
                interval_pom_right_rotate(T, x.p)
                w = x.p.left
            if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                w.color = Color.RED
                x = x.p
            else:
                if w.left.color == Color.BLACK:
                    w.right.color = Color.BLACK
                    w.color = Color.RED
                    interval_pom_left_rotate(T, w)
                    w = x.p.left
                w.color = x.p.color
                x.p.color = Color.BLACK
                w.left.color = Color.BLACK
                interval_pom_right_rotate(T, x.p)
                x = T.root
    x.color = Color.BLACK


def _copy_all_fields(z, y):
    y.key = z.key
    y.data = z.data
    y.low = z.low
    y.high = z.high
    y.overlap = z.overlap
    y.max_overlap = z.max_overlap
    y.pom = z.pom
    y.color = z.color
    y.left = z.left
    y.right = z.right
    y.p = z.p


def find_pom(T):
    return T.root.pom
