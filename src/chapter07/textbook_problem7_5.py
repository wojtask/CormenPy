from chapter05.exercise5_1_2 import random
from chapter07.textbook7_1 import partition
from datastructures.array import Array


def median_of_3_partition(A, p, r):
    i1, i2, i3 = random(p, r), random(p, r), random(p, r)
    median = Array.of(A[i1], A[i2], A[i3]).sort()[2]
    if median == A[i1]:
        A[r], A[i1] = A[i1], A[r]
    elif median == A[i2]:
        A[r], A[i2] = A[i2], A[r]
    else:
        A[r], A[i3] = A[i3], A[r]
    return partition(A, p, r)
