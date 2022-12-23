def open_overlap(i, i_):
    return i.low < i_.high and i_.low < i.high


def open_interval_search(T, i):
    x = T.root
    while x is not T.nil and not open_overlap(i, x.int):
        if x.left is not T.nil and x.left.max > i.low:
            x = x.left
        else:
            x = x.right
    return x
