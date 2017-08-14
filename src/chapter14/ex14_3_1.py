from chapter13.textbook import left_rotate


def interval_left_rotate(T, x):
    left_rotate(T, x, T.nil)
    y = x.p
    x.max = max(x.int.high, x.left.max, x.right.max)
    y.max = max(y.int.high, x.max, y.right.max)
