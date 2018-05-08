from chapter02.exercise2_3_5 import recursive_binary_search
from chapter02.textbook2_3 import merge_sort
from util import between


def sum_search(S, x):
    n = S.length
    merge_sort(S, 1, n)
    for i in between(1, n - 1):
        if recursive_binary_search(S, x - S[i], i + 1, n) is not None:
            return True
    return False
