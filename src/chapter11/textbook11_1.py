def direct_address_search(T, k):
    return T[k]


def direct_address_insert(T, x):
    T[x.key] = x


def direct_address_delete(T, x):
    T[x.key] = None
