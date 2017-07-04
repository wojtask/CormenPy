from chapter05.ex5_1_2 import random
from util import scope


def randomize_in_place_(A):
    n = A.length
    j = random(1, n)
    A[1], A[j] = A[j], A[1]
    for i in scope(2, n):
        j = random(i, n)
        A[i], A[j] = A[j], A[i]
