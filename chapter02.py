from util import irange


def insertion_sort(A):
    for j in irange(2, A.length):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def nonincreasing_insertion_sort(A):
    for j in irange(2, A.length):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def linear_search(A, v):
    i = 1
    while i <= A.length and A[i] != v:
        i += 1
    if i <= A.length:
        return i
    return None
