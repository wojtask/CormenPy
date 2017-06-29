from chapter02.textbook import merge_sort
from chapter02.ex2_3_5 import recursive_binary_search
from util import scope


def sum_search(S, x):
    n = S.length
    merge_sort(S, 1, n)
    for i in scope(1, n - 1):
        if recursive_binary_search(S, x - S[i], i + 1, n) is not None:
            return True
    return False
