from datastructures.array import Array
from util import between


def merge_(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = Array.of_length(n1)
    R = Array.of_length(n2)
    for i in between(1, n1):
        L[i] = A[p + i - 1]
    for j in between(1, n2):
        R[j] = A[q + j]
    i = j = 1
    k = p
    while i <= n1 and j <= n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1
    while i <= n1:
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while j <= n2:
        A[k] = R[j]
        j = j + 1
        k = k + 1
