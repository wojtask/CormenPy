import math

from chapter11.textbook11_4 import hash_search

Deleted = math.inf


def hash_delete(T, k, h):
    i = hash_search(T, k, h)
    if i is not None:
        T[i] = Deleted


def hash_insert_(T, k, h):
    m = T.length
    i = 0
    while True:
        j = h(k, i)
        if T[j] is None or T[j] is Deleted:
            T[j] = k
            return j
        else:
            i += 1
        if i == m:
            break
    raise ValueError('hash table overflow')
