def direct_address_search_(T, k):
    return T[k]


def direct_address_insert_(T, x):
    list_ = T[x.key]
    x.next = list_
    if list_ is not None:
        T[x.key].prev = x
    T[x.key] = x
    x.prev = None


def direct_address_delete_(T, x):
    if x.prev is not None:
        x.prev.next = x.next
    else:
        T[x.key] = x.next
    if x.next is not None:
        x.next.prev = x.prev
