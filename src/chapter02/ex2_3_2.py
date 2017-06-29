from datastructures.array import Array
from util import scope


def merge_(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = Array.of_length(n1)
    R = Array.of_length(n2)
    for i in scope(1, n1):
        L[i] = A[p + i - 1]
    for j in scope(1, n2):
        R[j] = A[q + j]
    i = 1
    j = 1
    for k in scope(p, r):
        if j > n2 or L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
