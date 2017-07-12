from chapter14.textbook import os_rank, os_select


def os_successor(T, x, i):
    r = os_rank(T, x)
    return os_select(T.root, r + i)
