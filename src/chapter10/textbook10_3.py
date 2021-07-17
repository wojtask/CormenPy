def allocate_object(L):
    if L.free is None:
        raise ValueError('out of space')
    else:
        x = L.free
        L.free = L.next[x]
        return x


def free_object(L, x):
    L.next[x] = L.free
    L.free = x
