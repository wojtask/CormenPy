from chapter05.exercise5_1_2 import random
from util import between


def jugs_group(R, B):
    n = R.length
    for i in between(1, n - 1):
        j = i
        while R[i] != B[j]:
            j += 1
        B[i], B[j] = B[j], B[i]


def jugs_match(R, B, p, r):
    if p < r:
        q = jugs_partition(R, B, p, r)
        jugs_match(R, B, p, q - 1)
        jugs_match(R, B, q + 1, r)


def jugs_partition(R, B, p, r):
    j = random(p, r)
    R[r], R[j] = R[j], R[r]
    x = R[r]
    i = p
    while B[i] != x:
        i += 1
    B[i], B[r] = B[r], B[i]
    i = p - 1
    for j in between(p, r - 1):
        if B[j] < x:
            i += 1
            B[i], B[j] = B[j], B[i]
    B[i + 1], B[r] = B[r], B[i + 1]
    i = p - 1
    for j in between(p, r - 1):
        if R[j] < x:
            i += 1
            R[i], R[j] = R[j], R[i]
    R[i + 1], R[r] = R[r], R[i + 1]
    return i + 1
