from util import between


def fair_partition(A, p, r):
    x = A[r]
    i = p - 1
    d = 1
    for j in between(p, r - 1):
        if A[j] <= x:
            if A[j] == x:
                d += 1
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1 - d // 2
