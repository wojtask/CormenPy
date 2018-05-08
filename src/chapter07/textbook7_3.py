from chapter05.exercise5_1_2 import random
from chapter07.textbook7_1 import partition


def randomized_partition(A, p, r):
    i = random(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)
