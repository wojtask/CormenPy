from chapter10.textbook import push, pop


def huge_array_search(T, S, k):
    if T[k] is not None and 1 <= T[k] <= S.top and S[T[k]].key == k:
        return S[T[k]]
    else:
        return None


def huge_array_insert(T, S, x):
    push(S, x)
    T[x.key] = S.top


def huge_array_delete(T, S, x):
    k = x.key
    y = pop(S)
    S[T[k]] = y
    T[y.key] = T[k]
