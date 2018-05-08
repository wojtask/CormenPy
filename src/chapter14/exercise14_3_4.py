from chapter14.textbook14_3 import overlap


def interval_search_all(T, x, i):
    if x.left is not T.nil and x.left.max >= i.low:
        interval_search_all(T, x.left, i)
    if x is not T.nil and overlap(i, x.int):
        print(x.int)
    if x.right is not T.nil and x.right.max >= i.low and x.int.low <= i.high:
        interval_search_all(T, x.right, i)
