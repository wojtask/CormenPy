from chapter14.textbook import interval_search, overlap


def min_interval_search(T, i):
    x = interval_search(T, i)
    if x is not T.nil:
        y = x.left
        while y is not T.nil:
            if overlap(i, y.int):
                x = y
                y = x.left
            else:
                if y.left is not T.nil and y.left.max >= i.low:
                    y = y.left
                else:
                    y = y.right
    return x
