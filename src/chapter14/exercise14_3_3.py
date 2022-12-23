from chapter14.textbook14_3 import overlap


def interval_search_lowest(T, i):
    x = T.root
    y = T.nil
    while x is not T.nil:
        if overlap(i, x.int) and (y is T.nil or x.int.low < y.int.low):
            y = x
        if x.left is not T.nil and x.left.max >= i.low:
            x = x.left
        else:
            x = x.right
    return y
