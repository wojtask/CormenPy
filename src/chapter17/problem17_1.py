import math

from util import between


def rev(k, a):
    return int(bin(a)[2:].zfill(k)[::-1], 2)


def bit_reversal(A):
    n = A.length
    k = int(math.log2(n))
    for i in between(1, n - 2):
        j = rev(k, i)
        if i < j:
            A[i], A[j] = A[j], A[i]


def bit_reversed_increment(a, k):
    m = 1 << (k - 1)
    while a & m != 0:
        a ^= m
        m >>= 1
    return a | m


def bit_reversal_(A):
    n = A.length
    k = int(math.log2(n))
    j = 0
    for i in between(1, n - 2):
        j = bit_reversed_increment(j, k)
        if i < j:
            A[i], A[j] = A[j], A[i]
