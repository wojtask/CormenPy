from chapter13.textbook13_2 import rb_successor


def rb_search_at_least(x, y, k, sentinel=None):
    if x is sentinel:
        return y
    if k == x.key:
        return x
    if k < x.key:
        return rb_search_at_least(x.left, x, k, sentinel=sentinel)
    else:
        return rb_search_at_least(x.right, y, k, sentinel=sentinel)


def rb_enumerate(T, a, b):
    x = rb_search_at_least(T.root, T.nil, a, sentinel=T.nil)
    while x is not T.nil and x.key <= b:
        print(x.key)
        x = rb_successor(x, sentinel=T.nil)
