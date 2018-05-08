from chapter05.exercise5_1_2 import random
from datastructures.array import Array
from util import between


def random_search(A, x):
    n = A.length
    B = Array.indexed(1, n)
    for k in between(1, n):
        B[k] = False
    checked = 0
    while checked < n:
        i = random(1, n)
        if A[i] == x:
            return i
        if not B[i]:
            B[i] = True
            checked = checked + 1
    return None
