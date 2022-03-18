def hash_insert(T, k, h):
    m = T.length
    i = 0
    while True:
        j = h(k, i)
        if T[j] is None:
            T[j] = k
            return j
        else:
            i += 1
        if i == m:
            break
    raise ValueError('hash table overflow')


def hash_search(T, k, h):
    m = T.length
    i = 0
    while True:
        j = h(k, i)
        if T[j] == k:
            return j
        i += 1
        if T[j] is None or i == m:
            break
    return None
