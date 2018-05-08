def rb_search(x, k, sentinel=None):
    if x is sentinel or k == x.key:
        return x
    if k < x.key:
        return rb_search(x.left, k, sentinel)
    else:
        return rb_search(x.right, k, sentinel)


def rb_minimum(x, sentinel=None):
    while x.left is not sentinel:
        x = x.left
    return x


def rb_maximum(x, sentinel=None):
    while x.right is not sentinel:
        x = x.right
    return x


def rb_predecessor(x, sentinel=None):
    if x.left is not sentinel:
        return rb_maximum(x.left, sentinel)
    y = x.p
    while y is not sentinel and x is y.left:
        x = y
        y = y.p
    return y


def rb_successor(x, sentinel=None):
    if x.right is not sentinel:
        return rb_minimum(x.right, sentinel)
    y = x.p
    while y is not sentinel and x is y.right:
        x = y
        y = y.p
    return y


def left_rotate(T, x, sentinel=None):
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
