from chapter05.ex5_1_2 import random
from datastructures.array import Array
from util import between


def permute_by_sorting(A):
    n = A.length
    P = Array.of_length(n)
    for i in between(1, n):
        P[i] = random(1, n ** 3)
    _sort_using_priorities(A, P)
    return A


def _sort_using_priorities(A, P):
    sorted_list_with_priorities = sorted(zip(A, P), key=lambda x: x[1])
    A.elements = [x[0] for x in sorted_list_with_priorities]


def randomize_in_place(A):
    n = A.length
    for i in between(1, n):
        j = random(i, n)
        A[i], A[j] = A[j], A[i]
