from chapter10.textbook import allocate_object, free_object


def compact_list_allocate_object(L):
    return allocate_object(L)


def compact_list_free_object(L, x):
    if L.free is None:
        y = L.key.length
    else:
        y = L.free - 1
    if L.next[x] is not None:
        L.prev[L.next[x]] = L.prev[x]
    if L.prev[x] is not None:
        L.next[L.prev[x]] = L.next[x]
    if x != y:
        if L.next[y] is not None:
            L.prev[L.next[y]] = x
        if L.prev[y] is not None:
            L.next[L.prev[y]] = x
    _copy_all_fields(L, y, x)
    if L.head == y:
        L.head = x
    free_object(L, y)


def _copy_all_fields(L, y, x):
    L.key[x] = L.key[y]
    L.next[x] = L.next[y]
    L.prev[x] = L.prev[y]
