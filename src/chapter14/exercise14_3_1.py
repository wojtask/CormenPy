from chapter13.textbook13_2 import left_rotate


def interval_left_rotate(T, x):
    left_rotate(T, x, T.nil)
    x.p.max = x.max
    x.max = max(x.int.high, x.left.max, x.right.max)
