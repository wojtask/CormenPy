from chapter05.exercise5_1_2 import random
from datastructures.array import Array
from util import between


def permute_by_sorting(A):
    n = A.length
    P = Array.indexed(1, n)
    for i in between(1, n):
        P[i] = random(1, n ** 3)
    A = _sort_using_priorities(A, P)
    return A


def _sort_using_priorities(A, P):
    return Array(x[0] for x in (sorted(zip(A, P), key=lambda x: x[1])))


def randomize_in_place(A):
    n = A.length
    for i in between(1, n):
        j = random(i, n)
        A[i], A[j] = A[j], A[i]
