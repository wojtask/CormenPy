import math

Deleted = math.inf


def hash_delete(T, k, h):
    m = T.length
    i = 0
    while True:
        j = h(k, i, m)
        if T[j] == k:
            T[j] = Deleted
            return
        i = i + 1
        if T[j] is None or i == m:
            break


def hash_insert_(T, k, h):
    m = T.length
    i = 0
    while True:
        j = h(k, i, m)
        if T[j] is None or T[j] is Deleted:
            T[j] = k
            return j
        else:
            i = i + 1
        if i == m:
            break
    raise ValueError('hash table overflow')
