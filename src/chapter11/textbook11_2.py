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
