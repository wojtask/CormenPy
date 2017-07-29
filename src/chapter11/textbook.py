def direct_address_search(T, k):
    return T[k]


def direct_address_insert(T, x):
    T[x.key] = x


def direct_address_delete(T, x):
    T[x.key] = None


def chained_hash_insert(T, x, h):
    m = T.length
    list_ = T[h(x.key, m)]
    x.next = list_
    if list_ is not None:
        list_.prev = x
    T[h(x.key, m)] = x
    x.prev = None


def chained_hash_search(T, k, h):
    m = T.length
    x = T[h(k, m)]
    while x is not None and x.key != k:
        x = x.next
    return x


def chained_hash_delete(T, x, h):
    m = T.length
    if x.prev is not None:
        x.prev.next = x.next
    else:
        T[h(x.key, m)] = x.next
    if x.next is not None:
        x.next.prev = x.prev


def hash_insert(T, k, h):
    m = T.length
    i = 0
    while True:
        j = h(k, i, m)
        if T[j] is None:
            T[j] = k
            return j
        else:
            i = i + 1
        if i == m:
            break
    raise RuntimeError('hash table overflow')


def hash_search(T, k, h):
    m = T.length
    i = 0
    while True:
        j = h(k, i, m)
        if T[j] == k:
            return j
        i = i + 1
        if T[j] is None or i == m:
            break
    return None


def quadratic_probing_search(T, k, h):
    m = T.length
    i = h(k, m)
    j = 0
    while True:
        if T[i] is None:
            return None
        if T[i] == k:
            return i
        j = j + 1
        if j == m:
            return None
        else:
            i = (i + j) % m
