def compactify_list(L):
    m = _mark_prev_fields(L)
    x = L.head
    x_ = None
    y = 1
    while x is not None:
        if x <= m:
            x_ = x
            x = L.next[x]
        else:
            while L.prev[y] == -1:
                y = y + 1
            _swap_all_fields(L, x, y)
            if L.next[x] is not None:
                L.prev[L.next[x]] = x
            if L.prev[x] is not None:
                L.next[L.prev[x]] = x
            else:
                L.free = x
            if x_ is not None:
                L.next[x_] = y
            else:
                L.head = y
            x_ = y
            x = L.next[y]
    _restore_prev_fields(L)


def _mark_prev_fields(L):
    size = 0
    x = L.head
    while x is not None:
        L.prev[x] = -1
        size += 1
        x = L.next[x]
    return size


def _swap_all_fields(L, x, y):
    L.key[x], L.key[y] = L.key[y], L.key[x]
    L.next[x], L.next[y] = L.next[y], L.next[x]
    L.prev[x], L.prev[y] = L.prev[y], L.prev[x]


def _restore_prev_fields(L):
    if L.head is None:
        return
    L.prev[L.head] = None
    x = L.head
    while L.next[x] is not None:
        L.prev[L.next[x]] = x
        x = L.next[x]
