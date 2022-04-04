from datastructures.array import Array
from util import between


def merge_(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = Array.indexed(1, n1)
    R = Array.indexed(1, n2)
    for i in between(1, n1):
        L[i] = A[p + i - 1]
    for j in between(1, n2):
        R[j] = A[q + j]
    i = 1
    j = 1
    for k in between(p, r):
        if j > n2 or (i <= n1 and L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
