import math


def multiary_parent(d, i):
    return math.ceil((i - 1) / d)


def multiary_child(d, i, k):
    return d * (i - 1) + k + 1


def multiary_max_heapify(A, d, i):
    largest = i
    k = 1
    child = multiary_child(d, i, 1)
    while k <= d and child <= A.heap_size:
        if A[child] > A[largest]:
            largest = child
        k = k + 1
        child = multiary_child(d, i, k)
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        multiary_max_heapify(A, d, largest)


def multiary_max_heap_insert(A, d, key):
    A.heap_size = A.heap_size + 1
    A[A.heap_size] = -math.inf
    multiary_heap_increase_key(A, d, A.heap_size, key)


def multiary_heap_increase_key(A, d, i, k):
    A[i] = max(A[i], k)
    while i > 1 and A[multiary_parent(d, i)] < A[i]:
        A[i], A[multiary_parent(d, i)] = A[multiary_parent(d, i)], A[i]
        i = multiary_parent(d, i)
