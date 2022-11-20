def compactify_list(L):
    k = 1
    l = L.head
    while l is not None:
        _swap_elements(L, k, l)
        if L.free == k:
            L.free = l
        l = L.next[k]
        L.next[k] = k + 1
        L.prev[k] = k - 1
        k += 1
    L.prev[1] = L.next[k - 1] = None
    L.head = 1


def _swap_elements(L, x, y):
    z = L.next[y]
    if L.prev[x] is not None:
        L.next[L.prev[x]] = y
    if L.next[x] is not None:
        L.prev[L.next[x]] = y
    if z is not None:
        L.prev[z] = x
    L.next[x], L.next[y] = L.next[y], L.next[x]
    L.prev[x], L.prev[y] = L.prev[y], L.prev[x]
    L.key[x], L.key[y] = L.key[y], L.key[x]
