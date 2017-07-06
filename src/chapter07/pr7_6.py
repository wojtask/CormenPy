from chapter05.ex5_1_2 import random
from util import scope, rscope


def fuzzy_sort(A, p, r):
    if p < r:
        q1, q2 = fuzzy_partition(A, p, r)
        fuzzy_sort(A, p, q1 - 1)
        fuzzy_sort(A, q2 + 1, r)


def fuzzy_partition(A, p, r):
    j = random(p, r)
    A[r], A[j] = A[j], A[r]
    x = A[r].a
    i = p - 1
    for j in scope(p, r - 1):
        if A[j].a <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    q = i + 1
    for k in rscope(i, p):
        if A[k].b >= x:
            q = q - 1
            A[q], A[k] = A[k], A[q]
    return q, i + 1