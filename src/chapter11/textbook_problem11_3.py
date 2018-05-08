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
