def single_array_allocate_object(L):
    if L.free is None:
        raise ValueError('out of space')
    x = L.free
    L.free = L.A[x + 1]
    return x


def single_array_free_object(L, x):
    L.A[x + 1] = L.free
    L.free = x
